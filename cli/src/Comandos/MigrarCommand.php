<?php

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos\Comandos;

use Danilocgsilva\BairrosBrasileirosLinhaDeComandos\MigrationInput;
use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputDefinition;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use GuzzleHttp\Client;
use Doctrine\DBAL\DriverManager;
use Doctrine\Migrations\Configuration\Migration\ConfigurationArray;
use Doctrine\Migrations\DependencyFactory;
use Doctrine\Migrations\Configuration\Migration\ExistingConfiguration;
use Doctrine\Migrations\Configuration\Configuration;
use Doctrine\Migrations\Metadata\Storage\TableMetadataStorageConfiguration;
use Doctrine\Migrations\Configuration\Connection\ExistingConnection;
use Doctrine\Migrations\Tools\Console\Command\MigrateCommand;
use Symfony\Component\Console\Input\InputArgument;
// use Symfony\Component\Console\Command\Command;


#[AsCommand(
    name: 'banco:migrar',
    description: 'Faz a migração do banco de dados.',
)]
class MigrarCommand extends Command
{
    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        // $customInput = new MigrationInput(
        //     ['zero' => null, 'version' => 'latest'], 
        //     new InputDefinition([new InputArgument('arg1')])
        // );
        $customInput = new MigrationInput();

        // $customInput->setArgument('version', 'latest');
        // $input->setArgument('version', 'latest');

        // $guzzleClient = new Client();
        // $resposta = $guzzleClient->get("http://bairros_brasileiros_python:5000/banco/migrar");
        
        // $output->writeln($resposta->getBody()->getContents());
        // return Command::SUCCESS;

        $customInput->setInteractive(false);
        // $input->setArgument('--version', 'Danilocgsilva\BairrosBrasileirosLinhaDeComandos\Version20241006202116');
        // $input->setOption('--version', 'Danilocgsilva\BairrosBrasileirosLinhaDeComandos\Version20241006202116');
        // $input->setArgument('version', 'latest');
        // $input->getFirstArgument();

        $connection = DriverManager::getConnection([
            'dbname' => 'bairros_brasileiros',
            'user' => 'root',
            'password' => 'bairros_brasileiros',
            'host' => 'bairros_brasileiros_banco_de_dados',
            'driver' => 'pdo_mysql', // or your preferred driver
        ]);

        // Configure Doctrine Migrations
        $configuration = new Configuration();
        $configuration->addMigrationsDirectory('Danilocgsilva\BairrosBrasileirosLinhaDeComandos', './migrations');
        $configuration->setAllOrNothing(true);
        $configuration->setCheckDatabasePlatform(false);
        $configuration->setMigrationOrganization('none');
        $configuration->setTransactional(true);

        // Set up table storage configuration
        $storageConfiguration = new TableMetadataStorageConfiguration();
        $storageConfiguration->setTableName('migration_versions');
        $storageConfiguration->setVersionColumnLength(191);
        $storageConfiguration->setVersionColumnName('version');
        $storageConfiguration->setExecutedAtColumnName('executed_at');
        $storageConfiguration->setExecutionTimeColumnName('execution_time');
        $configuration->setMetadataStorageConfiguration($storageConfiguration);

        // Create DependencyFactory
        $dependencyFactory = DependencyFactory::fromConnection(
            new ExistingConfiguration($configuration),
            new ExistingConnection($connection)
        );

        // Create and run the migrate command
        $migrateCommand = new MigrateCommand($dependencyFactory);
        return $migrateCommand->run($customInput, $output);
    }
}
