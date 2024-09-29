<?php

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos\Comandos;

use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use Symfony\Component\Console\Attribute\AsCommand;
use GuzzleHttp\Client;

#[AsCommand(
    name: 'banco:ajuda',
    description: 'Descreve a anatomia do banco de dados.',
)]
class AjudaBanco extends Command
{
    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $guzzleClient = new Client();
        $resposta = $guzzleClient->get("http://bairros_brasileiros_python:5000/banco/ajuda");

        $output->writeln($resposta->getBody()->getContents());
        return Command::SUCCESS;
    }
}
