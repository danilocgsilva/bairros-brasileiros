<?php

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos\Comandos;

use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use GuzzleHttp\Client;

#[AsCommand(
    name: 'receita:todos',
    description: 'Lista todos os locais gravados no banco de dados.',
)]
class ListarReceitas extends Command
{
    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $guzzleClient = new Client();
        $resposta = $guzzleClient->get("http://bairros_brasileiros_python:5000/ver_todas_informacoes");
        $dadosTodosLocais = json_decode($resposta->getBody()->getContents());
        foreach ($dadosTodosLocais as $local) {
            $output->writeln($local);
        }

        return Command::SUCCESS;
    }
}
