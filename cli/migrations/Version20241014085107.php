<?php

declare(strict_types=1);

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

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
            `receita_id` INT UNSIGNED
        );');
        $this->addSql("ALTER TABLE historico_buscas ADD CONSTRAINT historico_buscas_receitas FOREIGN KEY (receita_id) REFERENCES `receitas` (`id`);");
    }

    public function down(Schema $schema): void
    {
        $this->addSql('ALTER TABLE historico_buscas DROP FOREIGN KEY historico_buscas_receitas;');
        $this->addSql('DROP TABLE historico_buscas;');
    }
}
