<?php

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos\Comandos;

use Symfony\Component\Console\Command\Command;
use GuzzleHttp\Client;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Question\Question;

#[AsCommand(
    name: 'adicionar:cidade',
    description: 'Adiciona uma cidade.',
)]
class AdicionarCidade extends Command
{
    private $input;

    private $output;
    
    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $this->input = $input;
        $this->output = $output;
        
        $nomeCidade = $this->perguntar('Escreva o nome da cidade a ser cadastrada');
        $nomeEstado = $this->perguntar('Escreva o nome do estado da cidade');

        $guzzleClient = new Client();
        $resposta = $guzzleClient->post(
            "http://bairros_brasileiros_python:5000/adicionar/cidade",
            [
                'json' => [
                    'nome' => $nomeCidade,
                    'estado' => $nomeEstado,
                ]
            ]
        );

        $output->writeln($resposta->getBody()->getContents());
        return Command::SUCCESS;
    }

    private function perguntar(string $tituloPergunta): string
    {
        $helper = $this->getHelper('question');
        $pergunta = new Question($tituloPergunta . ': ');

        return $helper->ask($this->input, $this->output, $pergunta);
    }
}
