<?php

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos\Comandos;

use Danilocgsilva\BairrosBrasileirosLinhaDeComandos\MigrationInput;
use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use Doctrine\DBAL\DriverManager;
use Doctrine\Migrations\DependencyFactory;
use Doctrine\Migrations\Configuration\Migration\ExistingConfiguration;
use Doctrine\Migrations\Configuration\Configuration;
use Doctrine\Migrations\Metadata\Storage\TableMetadataStorageConfiguration;
use Doctrine\Migrations\Configuration\Connection\ExistingConnection;
use Doctrine\Migrations\Tools\Console\Command\MigrateCommand;
use Doctrine\DBAL\Connection;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputOption;

#[AsCommand(
    name: 'banco:migrar',
    description: 'Faz a migração do banco de dados.',
)]
class MigrarCommand extends Command
{ 
    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $customInput = new MigrationInput();

        $dependencyFactory = DependencyFactory::fromConnection(
            new ExistingConfiguration(
                $this->buscarConfiguracoesDeConexao()
            ),
            new ExistingConnection(
                $this->buscarCredenciaisDeConexao()
            )
        );

        $migrateCommand = new MigrateCommand($dependencyFactory);
        return $migrateCommand->run($customInput, $output);
    }

    private function buscarConfiguracoesDeConexao(): Configuration
    {
        $configuration = new Configuration();
        $configuration->addMigrationsDirectory('Danilocgsilva\BairrosBrasileirosLinhaDeComandos', './migrations');
        $configuration->setAllOrNothing(true);
        $configuration->setCheckDatabasePlatform(false);
        $configuration->setMigrationOrganization('none');
        $configuration->setTransactional(true);

        $configuration->setMetadataStorageConfiguration(
            $this->buscarConfiguracoesStorage()
        );

        return $configuration;
    }

    private function buscarCredenciaisDeConexao(): Connection
    {
        $connection = DriverManager::getConnection([
            'dbname' => getenv('BAIRROS_BRASILEIROS_DB_NOME'),
            'user' => getenv('BAIRROS_BRASILEIROS_DB_USUARIO'),
            'password' => getenv('BAIRROS_BRASILEIROS_DB_SENHA'),
            'host' => getenv('BAIRROS_BRASILEIROS_DB_HOST'),
            'driver' => 'pdo_mysql'
        ]);

        return $connection;
    }

    private function buscarConfiguracoesStorage(): TableMetadataStorageConfiguration
    {
        $storageConfiguration = new TableMetadataStorageConfiguration();
        $storageConfiguration->setTableName('migration_versions');
        $storageConfiguration->setVersionColumnLength(191);
        $storageConfiguration->setVersionColumnName('version');
        $storageConfiguration->setExecutedAtColumnName('executed_at');
        $storageConfiguration->setExecutionTimeColumnName('execution_time');

        return $storageConfiguration;
    }
}
