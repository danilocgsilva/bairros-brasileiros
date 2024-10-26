<?php

declare(strict_types=1);

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos;

use Doctrine\DBAL\Schema\Schema;
use Doctrine\Migrations\AbstractMigration;

/**
 * Auto-generated Migration: Please modify to your needs!
 */
final class Version20241026115407 extends AbstractMigration
{
    public function getDescription(): string
    {
        return '';
    }

    public function up(Schema $schema): void
    {
        $sqlBase =
            "INSERT INTO receitas (
                nome, 
                seletor_tabela, 
                parseador, 
                processador, 
                endereco, 
                tipo_localidade
            ) VALUES (
                :nome, 
                :seletor_tabela, 
                :parseador, 
                :processador, 
                :endereco, 
                :tipo_localidade
            );";
        $nome = 'Buscar todas cidades brasileiras';
        $seletorTabela = '.mw-content-ltr.mw-parser-output li';
        $parseador = 'XNext(2, 1)';
        $processador = 'ProcessadorCapturaCidadeSigla';
        $endereco = 'https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Brasil';
        $tipoLocalidade = 'cidade';
        $this->addSql($sqlBase);
    }

    public function down(Schema $schema): void
    {
        $this->addSql('DELETE FROM receitas WHERE nome = :nome AND endereco = :endereco;');
    }
}
