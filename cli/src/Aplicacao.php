<?php

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos;

use Symfony\Component\Console\Application as SymfonyApplication;
use Symfony\Component\Console\Input\InputDefinition;
use Symfony\Component\Console\Input\InputArgument;
use Symfony\Component\Console\Input\InputOption;

class Aplicacao extends SymfonyApplication
{
    protected function getDefaultInputDefinition(): InputDefinition
    {
        return new InputDefinition([
            new InputArgument('command', InputArgument::REQUIRED, 'O comando a ser executado.'),
            new InputOption('--help', '-h', InputOption::VALUE_NONE, 'Exibe uma ajuda para um comando fornecido. Quando nenhum comando fornecido é, exibe a ajuda para o comando padrão.'),
            new InputOption('--quiet', '-q', InputOption::VALUE_NONE, 'Não escreve nenhuma mensagem no comando.'),
            new InputOption('--verbose', '-v|vv|vvv', InputOption::VALUE_NONE, 'Aumenta o detalhamento da mensagem: 1 para saída normal, 2 para maior detalhamento e 3 para debug.'),
            new InputOption('--version', '-V', InputOption::VALUE_NONE, 'Exibe a versão da aplicação.'),
            new InputOption('--ansi', '', InputOption::VALUE_NEGATABLE, 'Força (ou desativa --no-ansi) a saída ANSI.', null),
            new InputOption('--no-interaction', '-n', InputOption::VALUE_NONE, 'Não faz nenhuma pergunta durante a execução do comando.'),
        ]);
    }
}
