<?php

declare(strict_types=1);

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20241006202116 extends AbstractMigration
{
    public function getDescription(): string
    {
        return 'Cria uma tabela no banco de dados.';
    }

    public function up(Schema $schema): void
    {
        $this->addSql('CREATE TABLE locais (
            `id` INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
            `local` VARCHAR(255),
            `parentalidade` INT UNSIGNED,
            `tipo_localidade` INT UNSIGNED
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;');
        $this->addSql('ALTER TABLE locais ADD CONSTRAINT `parentalidade_id_constraint` FOREIGN KEY (`parentalidade`) REFERENCES locais (`id`);');
        $this->addSql('CREATE TABLE tipos_locais (
            `id` INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
            `tipo` VARCHAR(32)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;');
        $this->addSql('ALTER TABLE `locais` ADD CONSTRAINT `tipos_locais_tipo_localidade_constraint` FOREIGN KEY (`tipo_localidade`) REFERENCES `tipos_locais` (`id`);');
    }

    public function down(Schema $schema): void
    {
        $this->addSql('ALTER TABLE locais DROP FOREIGN KEY tipos_locais_tipo_localidade_constraint;');
        $this->addSql('DROP TABLE tipos_locais');
        $this->addSql('ALTER TABLE locais DROP FOREIGN KEY parentalidade_id_constraint;');
        $this->addSql('DROP TABLE locais;');
    }
}
