<?php

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos\Comandos;

use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use GuzzleHttp\Client;
use Danilocgsilva\BairrosBrasileirosLinhaDeComandos\Traits\Perguntar;

#[AsCommand(
    name: 'receitas:rodar',
    description: 'Buscar os dados a partir de uma receita específica já salva.',
)]
class RodarReceita extends Command
{
    use Perguntar;

    private $input;

    private $output;

    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $this->input = $input;
        $this->output = $output;

        $idReceita = $this->perguntar('Qual o id da receita a ser rodado?');

        $guzzleClient = new Client();
        $resposta = $guzzleClient->post(
            "http://bairros_brasileiros_python:5000/receita/rodar",
            [
                'json' => [
                    'receita_id' => $idReceita
                ]
            ]            
        );

        $output->writeln($resposta->getBody()->getContents());
        return Command::SUCCESS;
    }
}
