<?php

declare(strict_types=1);

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

final class Version20241012150945 extends AbstractMigration
{
    public function getDescription(): string
    {
        return 'Cria a estrutura para registrar receitas para a captura de dados.';
    }

    public function up(Schema $schema): void
    {
        $this->addSql('CREATE TABLE receitas (
            `id` INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
            `nome` VARCHAR(255),
            `seletor_tabela` CHAR(192),
            `parseador` CHAR(192),
            `processador` CHAR(192),
            `endereco` VARCHAR(255),
            `tipo_localidade` CHAR(32)
        );');
    }

    public function down(Schema $schema): void
    {
        $this->addSql('DROP TABLE receitas;');
    }
}
