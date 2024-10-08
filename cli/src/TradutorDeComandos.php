<?php

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos;

use Symfony\Component\Translation\Translator;
use Symfony\Component\Translation\Formatter\MessageFormatterInterface;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Application;
use Symfony\Component\Translation\Loader\YamlFileLoader;
use Symfony\Component\Console\Command\CompleteCommand;

class TradutorDeComandos extends Translator
{
    public function __construct(
        string $locale,
        private Application $application,
        ?MessageFormatterInterface $formatter = null,
        ?string $cacheDir = null,
        bool $debug = false,
        array $cacheVary = [],
    ) {
        parent::__construct($locale, $formatter, $cacheDir, $debug, $cacheVary);

        $this->addLoader('yaml', new YamlFileLoader());
        $this->addResource('yaml', __DIR__.'/../translations/commands.pt_BR.yml', 'pt_BR');
    }

    public function traduzirComando(
        Command $comando,
        string $caminhoNamespaceNome,
        string $caminhoNamespaceDescricao,
        string $caminhoNamespaceAjuda
    ): void
    {
        $comando
            ->setName(
                $this->trans($caminhoNamespaceNome)
            )->setDescription(
                $this->trans($caminhoNamespaceDescricao)
            )->setHelp(
                $this->trans($caminhoNamespaceAjuda)
            )
        ;
        $this->application->add($comando);
    }

    public function traduzirList()
    {
        $this->traduzirComando(
            $this->application->find('list'), 
            'Symfony\Component\Console\Command\ListCommand.name',
            'Symfony\Component\Console\Command\ListCommand.description',
            'Symfony\Component\Console\Command\ListCommand.help'
        );
    }

    public function traduzirHelp(): void
    {
        $this->traduzirComando(
            $this->application->find('help'),
            'Symfony\Component\Console\Command\HelpCommand.name',
            'Symfony\Component\Console\Command\HelpCommand.description',
            'Symfony\Component\Console\Command\HelpCommand.help'
        );
    }

    public function traduzirCompletion(): void
    {
        $this->traduzirComando(
            $this->application->find('completion'),
            'Symfony\Component\Console\Command\CompleteCommand.name',
            'Symfony\Component\Console\Command\CompleteCommand.description',
            'Symfony\Component\Console\Command\CompleteCommand.help'
        );
    }
}
