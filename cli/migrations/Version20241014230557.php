<?php

declare(strict_types=1);

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

final class Version20241014230557 extends AbstractMigration
{
    public function getDescription(): string
    {
        return 'Registra o histórico da captura de dados.';
    }

    public function up(Schema $schema): void
    {
        $this->addSql('CREATE TABLE historico_capturas (
            `id` INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
            `data_captura` DATETIME(3) NOT NULL,
            `sucesso` TINYINT NOT NULL,
            `historico_buscas_id` INT UNSIGNED NOT NULL
        );');
        $this->addSql('ALTER TABLE historico_capturas ADD CONSTRAINT historico_capturas_historico_busca FOREIGN KEY (historico_buscas_id) REFERENCES historico_buscas (id);');
    }

    public function down(Schema $schema): void
    {
        $this->addSql('ALTER TABLE historico_capturas DROP FOREIGN KEY historico_capturas_historico_busca;');
        $this->addSql('DROP TABLE historico_capturas;');
    }
}
