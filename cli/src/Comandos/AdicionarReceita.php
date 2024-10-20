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
        $this->addOption('seletor_tabela', 't', InputArgument::OPTIONAL, 'O seletor da tabela');
        $this->addOption('seletor_coluna', 'c', InputArgument::OPTIONAL, 'O seletor da coluna');
        $this->addOption('endereco', 'e', InputArgument::OPTIONAL, 'O endereço para a busca da informação');
        $this->addOption('tipo_localidade', 'tl', InputArgument::OPTIONAL, 'O tipo de localidade a ser inserido');
        $this->addOption('id_localidade_pai', 'p', InputArgument::OPTIONAL, 'O id da localidade pai, se houver.');
    }

    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $this->input = $input;
        $this->output = $output;

        $nomeReceita = $this->buscarOpcao('nome_receita', 'Qual o nome da receita a ser adicionada?');
        $seletotTabela = $this->buscarOpcao('seletor_tabela', 'Qual o seletor html da tabela?');
        $seletorColuna = $this->buscarOpcao('seletor_coluna', 'Qual o seletor html da coluna?');
        $endereco = $this->buscarOpcao('endereco', 'Qual o endereço para a busca da informação?');
        $tipoLocalidade = $this->buscarOpcao('tipo_localidade', 'Qual o tipo de localidade a ser inserido (cidade ou bairro)?');
        $nomeLocalidadePai = $this->buscarOpcao('id_localidade_pai', 'Qual o id da localidade pai (se houver)?');

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
                    'id_localidade_pai' => $nomeLocalidadePai
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
