<?php

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos\Comandos;

use Symfony\Component\Console\Command\Command;
use GuzzleHttp\Client;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use Symfony\Component\Console\Attribute\AsCommand;

#[AsCommand(
    name: 'adicionar:cidade',
    description: 'Adiciona uma cidade.',
)]
class AdicionarCidade extends Command
{
    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $guzzleClient = new Client();
        $resposta = $guzzleClient->get("http://bairros_brasileiros_python:5000/adicionar/cidade");

        $output->writeln($resposta->getBody()->getContents());
        return Command::SUCCESS;
    }
}
