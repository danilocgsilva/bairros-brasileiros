<?php

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos;

use Symfony\Component\Console\Attribute\AsCommand;
use Symfony\Component\Console\Command\Command;
use Symfony\Component\Console\Input\InputInterface;
use Symfony\Component\Console\Output\OutputInterface;

#[AsCommand(name: 'banco:migrar')]
class MigrarCommand extends Command
{
    protected function execute(InputInterface $input, OutputInterface $output): int
    {
        $output->writeln("Vamos migrar!");

        return Command::SUCCESS;
    }
}