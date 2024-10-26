<?php

declare(strict_types=1);

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20241023083133 extends AbstractMigration
{
    public function getDescription(): string
    {
        return 'Adiciona as siglas nos estados.';
    }

    public function up(Schema $schema): void
    {
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (1, 'SP');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (2, 'PR');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (3, 'RS');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (4, 'SC');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (5, 'MG');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (6, 'MT');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (7, 'AC');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (8, 'AL');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (9, 'AP');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (10, 'AM');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (11, 'BA');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (12, 'CE');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (13, 'MS');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (14, 'ES');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (15, 'GO');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (16, 'MA');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (17, 'PA');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (18, 'PB');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (19, 'PE');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (20, 'PI');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (21, 'RJ');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (22, 'RN');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (23, 'RO');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (24, 'RR');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (25, 'SE');");
        $this->addSql("INSERT INTO siglas_estados (`estado_id`, `sigla`) VALUES (26, 'TO');");
    }

    public function down(Schema $schema): void
    {
        $this->addSql("DELETE FROM siglas_estados;");
    }
}
