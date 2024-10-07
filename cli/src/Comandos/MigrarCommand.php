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

#[AsCommand(
    name: 'banco:migrar',
    description: 'Faz a migração do banco de dados.',
)]
class MigrarCommand extends Command
{
    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $customInput = new MigrationInput();
        $customInput->setInteractive(false);

        $connection = $this->buscarCredenciaisDeConexao();
        $configuration = $this->buscarConfiguracoesDeConexao();
        $storageConfiguration = $this->buscarConfiguracoesStorage();

        $configuration->setMetadataStorageConfiguration($storageConfiguration);

        $dependencyFactory = DependencyFactory::fromConnection(
            new ExistingConfiguration($configuration),
            new ExistingConnection($connection)
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

        return $configuration;
    }

    private function buscarCredenciaisDeConexao(): Connection
    {
        $connection = DriverManager::getConnection([
            'dbname' => 'bairros_brasileiros',
            'user' => 'root',
            'password' => 'bairros_brasileiros',
            'host' => 'bairros_brasileiros_banco_de_dados',
            'driver' => 'pdo_mysql', // or your preferred driver
        ]);

        return $connection;
    }

    private function buscarConfiguracoesStorage(): TableMetadataStorageConfiguration
    {
        // Set up table storage configuration
        $storageConfiguration = new TableMetadataStorageConfiguration();
        $storageConfiguration->setTableName('migration_versions');
        $storageConfiguration->setVersionColumnLength(191);
        $storageConfiguration->setVersionColumnName('version');
        $storageConfiguration->setExecutedAtColumnName('executed_at');
        $storageConfiguration->setExecutionTimeColumnName('execution_time');

        return $storageConfiguration;
    }
}
