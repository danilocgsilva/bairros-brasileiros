<?php

declare(strict_types=1);

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

final class Version20241008115114 extends AbstractMigration
{
    public function getDescription(): string
    {
        return 'Adicionando os estados brasileiros.';
    }

    public function up(Schema $schema): void
    {
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('São Paulo', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Paraná', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Rio Grande do Sul', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Santa Catarina', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Minas Gerais', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Mato Grosso', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Acre', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Alagoas', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Amapá', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Amazonas', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Bahia', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Ceará', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Mato Grosso do Sul', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Espírito Santo', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Goiás', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Maranhão', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Pará', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Paraíba', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Pernambuco',3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Piauí',3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Rio de Janeiro',3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Rio Grande do Norte', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Rondônia', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Roraima', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Sergipe', 3);");
        $this->addSql("INSERT INTO locais (local, tipo_localidade) VALUES ('Tocantins', 3);");
    }

    public function down(Schema $schema): void
    {
        $this->addSql("DELETE FROM locais WHERE tipo_localidade = 3;");
    }
}
