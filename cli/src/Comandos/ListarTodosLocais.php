<?php

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos\Comandos;

use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use GuzzleHttp\Client;

#[AsCommand(
    name: 'receitas:listar',
    description: 'Listar todas as receitas',
)]
class ListarTodosLocais extends Command
{
    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $guzzleClient = new Client();
        $resposta = $guzzleClient->get("http://bairros_brasileiros_python:5000/receitas");
        $todasReceitas = json_decode($resposta->getBody()->getContents());
        foreach ($todasReceitas as $receita) {
            $output->writeln('id: ' . $receita->id . ', nome: ' . $receita->nome);
        }

        return Command::SUCCESS;
    }
}
