<?php

declare(strict_types=1);

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

final class Version20241023082614 extends AbstractMigration
{
    public function getDescription(): string
    {
        return 'Cria a tabela para a siglas dos estados.';
    }

    public function up(Schema $schema): void
    {
        $this->addSql(
            "CREATE TABLE siglas_estados (
                `id` INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
                `sigla` CHAR(2),
                `estado_id` INT UNSIGNED NOT NULL
            );"
        );
        $this->addSql("ALTER TABLE siglas_estados ADD CONSTRAINT siglas_estados_locais_estados FOREIGN KEY (estado_id) REFERENCES locais (id);");
    }

    public function down(Schema $schema): void
    {
        $this->addSql("ALTER TABLE siglas_estados DROP FOREIGN KEY siglas_estados_locais_estados;");
        $this->addSql("DROP TABLE siglas_estados;");
    }
}
