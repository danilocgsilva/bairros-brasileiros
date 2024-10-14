<?php

declare(strict_types=1);

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20241014085107 extends AbstractMigration
{
    public function getDescription(): string
    {
        return 'Histórico de busca.';
    }

    public function up(Schema $schema): void
    {
        $this->addSql('CREATE TABLE historico_buscas (
            `id` INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
            `data` DATETIME NOT NULL,
            `sucessos` INT NOT NULL,
            `falhas` INT NOT NULL,
            `receita_id` INT UNISGNED NOT NULL
        )');
        $this->addSql("ALTER TABLE historico_buscas ADD CONSTRAINT historico_buscas_receitas FOREIGN KEY (receita_id) REFERENCES `receitas` (`id`);");
    }

    public function down(Schema $schema): void
    {
        $this->addSql('ALTER TABLE historico_buscas DROP FOREIGN KEY historico_buscas_receitas;');
        $this->addSql('DROP TABLE historico_buscas;');
    }
}
