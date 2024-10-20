<?php

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos\Comandos;

use Danilocgsilva\BairrosBrasileirosLinhaDeComandos\Traits\Perguntar;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;
use Symfony\Component\Console\Attribute\AsCommand;
use GuzzleHttp\Client;
use Symfony\Component\Console\Input\InputArgument;

#[AsCommand(
    name: 'receita:adicionar',
    description: 'Adiciona uma receita para a busca de dados.',
)]
class AdicionarReceita extends Command
{
    use Perguntar;

    private $input;

    private $output;

    protected function configure(): void
    {
        $this->addOption('nome_receita', 'r', InputArgument::OPTIONAL, 'O nome da receita');
    }

    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $this->input = $input;
        $this->output = $output;

        $nomeReceita = $this->buscarOpcao('nome_receita', 'Qual o nome da receita a ser adicionada?');
        $seletotTabela = $this->perguntar('Qual o seletor html da tabela?');
        $seletorColuna = $this->perguntar('Qual o seletor html da coluna?');
        $endereco = $this->perguntar('Qual o endereço para a busca da informação?');
        $tipoLocalidade = $this->perguntar('Qual o tipo de localidade?');
        $nomeLocalidadePai = $this->perguntar('Qual o nome da localidade pai (se houver)?');

        $guzzleClient = new Client();

        $resposta = $guzzleClient->post(
            "http://bairros_brasileiros_python:5000/receita/adicionar",
            [
                'json' => [
                    'nome' => $nomeReceita,
                    'seletor_tabela' => $seletotTabela,
                    'seletor_coluna' => $seletorColuna,
                    'endereco' => $endereco,
                    'tipo_localidade' => $tipoLocalidade,
                    'nome_localidade_pai' => $nomeLocalidadePai
                ]
            ]            
        );

        $output->writeln($resposta->getBody()->getContents());
        return Command::SUCCESS;
    }

    private function buscarOpcao(string $nomeOpcao, string $pergunta): string
    {
        $opcao = $this->input->getOption($nomeOpcao);
        if ($opcao !== null) {
            return $opcao;
        }
        return $this->perguntar($pergunta);
    }
}
