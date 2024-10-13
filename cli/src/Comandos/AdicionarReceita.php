<?php

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos\Comandos;

use Danilocgsilva\BairrosBrasileirosLinhaDeComandos\Traits\Perguntar;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use Symfony\Component\Console\Attribute\AsCommand;
use GuzzleHttp\Client;

#[AsCommand(
    name: 'receita:adicionar',
    description: 'Adiciona uma receita para a busca de dados.',
)]
class AdicionarReceita extends Command
{
    use Perguntar;

    private $input;

    private $output;

    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $this->input = $input;
        $this->output = $output;

        $nomeReceita = $this->perguntar('Qual o nome da receita a ser adicionada?');
        $seletotTabela = $this->perguntar('Qual o seletor html da tabela?');
        $seletorColuna = $this->perguntar('Qual o seletor html da coluna?');
        $endereco = $this->perguntar('Qual o endereço para a busca da informação?');

        $guzzleClient = new Client();

        $resposta = $guzzleClient->post(
            "http://bairros_brasileiros_python:5000/receita/adicionar",
            [
                'json' => [
                    'nome' => $nomeReceita,
                    'seletor_tabela' => $seletotTabela,
                    'seletor_coluna' => $seletorColuna,
                    'endereco' => $endereco,
                ]
            ]            
        );

        $output->writeln($resposta->getBody()->getContents());
        return Command::SUCCESS;
    }
}
