<?php

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos\Comandos;

use Symfony\Component\Console\Attribute\AsCommand;  
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use GuzzleHttp\Client;

#[AsCommand(
    name: 'banco:migrar',
    description: 'Faz a migração do banco de dados.',
)]
class MigrarCommand extends Command
{
    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $guzzleClient = new Client();
        $resposta = $guzzleClient->get("http://bairros_brasileiros_python:5000");
        
        $output->writeln($resposta->getBody()->getContents());
        return Command::SUCCESS;
    }
}