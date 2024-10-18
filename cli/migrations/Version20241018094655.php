<?php

declare(strict_types=1);

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

final class Version20241018094655 extends AbstractMigration
{
    public function getDescription(): string
    {
        return 'Quando houver erro das capturas e houver mensagem, fazer o registro.';
    }

    public function up(Schema $schema): void
    {
        $this->addSql(
            "CREATE TABLE mensagens_erros_capturas (
                `id` INT UNSIGNED NOT NULL PRIMARY KEY AUTO_INCREMENT,
                `mensagem` VARCHAR(255),
                `historico_capturas_id` INT UNSIGNED NOT NULL
            );"
        );
        $this->addSql("ALTER TABLE mensagens_erros_capturas ADD CONSTRAINT mensagens_erros_capturas_historico_capturas FOREIGN KEY (historico_capturas_id) REFERENCES historico_capturas (id);");
    }

    public function down(Schema $schema): void
    {
        $this->addSql("ALTER TABLE mensagens_erros_capturas DROP FOREIGN KEY mensagens_erros_capturas_historico_capturas;");
        $this->addSql("DROP TABLE mensagens_erros_capturas;");
    }
}
