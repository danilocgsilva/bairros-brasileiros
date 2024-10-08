<?php

declare(strict_types=1);

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20241008000406 extends AbstractMigration
{
    public function getDescription(): string
    {
        return 'Criar tipos de localidades.';
    }

    public function up(Schema $schema): void
    {
        $this->addSql("INSERT INTO tipos_locais (tipo) VALUES ('bairro');");
        $this->addSql("INSERT INTO tipos_locais (tipo) VALUES ('cidade');");
        $this->addSql("INSERT INTO tipos_locais (tipo) VALUES ('estado');");
    }

    public function down(Schema $schema): void
    {
        $this->addSql('DELETE FROM tipos_locais;');
        $this->addSql('ALTER TABLE tipos_locais AUTO_INCREMENT = 1;');
    }
}
