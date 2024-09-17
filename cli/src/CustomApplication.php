<?php

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos;

use Symfony\Component\Console\Application;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Translation\Translator;
use Symfony\Component\Translation\Loader\YamlFileLoader;
use Symfony\Component\Console\Command\ListCommand;

class CustomApplication extends Application
{
    /** @var array<Command> */
    private array $defaultCommands;

    public function __construct(
        private Translator $translator,
        private string $name = 'UNKNOWN',
        private string $version = 'UNKNOWN'
    ) {
        parent::__construct($name, $version);

        $this->defaultCommands = parent::getDefaultCommands();

        $this->translate();

        $this->setDefaultCommand('lista');
    }

    public function getDefaultCommands(): array
    {
        return $this->defaultCommands;
    }

    private function substituirComando(Command $commandRemover, Command $adicionar): void
    {
        $this->defaultCommands = array_filter(
            $this->defaultCommands,
            fn(Command $command) => $command->getName() !== $commandRemover->getName()
        );

        $this->add($adicionar);
    }

    private function translate()
    {
        $nomeTraduzido = $this->translator->trans('Symfony\Component\Console\Command\ListCommand.name');
        $descricaoTraduzida = $this->translator->trans('Symfony\Component\Console\Command\ListCommand.description');
        $textoDeAjudaTraduzido = $this->translator->trans('Symfony\Component\Console\Command\ListCommand.help');

        $listCommandTraduzido = new ListCommand();

        $listCommandTraduzido
            ->setName($nomeTraduzido)
            ->setDescription($descricaoTraduzida)
            ->setHelp($textoDeAjudaTraduzido)
        ;

        $this->substituirComando(new ListCommand(), $listCommandTraduzido);
    }
}