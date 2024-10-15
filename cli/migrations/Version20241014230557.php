<?php

declare(strict_types=1);

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20241014230557 extends AbstractMigration
{
    public function getDescription(): string
    {
        return 'Registra o histórico da captura de dados.';
    }

    public function up(Schema $schema): void
    {
        $this->addSql('CREATE TABLE historico_captura (
            `id` INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
            `data_captura` DATETIME NOT NULL,
            `sucesso` TINYINT NOT NULL,
            `historico_buscas_id` INT UNSIGNED NOT NULL
        );');
        $this->addSql('ALTER TABLE historico_captura ADD CONSTRAINT historico_captura_historico_busca FOREIGN KEY (historico_buscas_id) REFERENCES historico_buscas (id);');
    }

    public function down(Schema $schema): void
    {
        $this->addSql('ALTER TABLE historico_captura DROP FOREIGN KEY historico_captura_historico_busca;');
        $this->addSql('DROP TABLE historico_captura;');
    }
}
