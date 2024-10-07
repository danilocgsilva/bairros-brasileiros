<?php

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos;

use Symfony\Component\Console\Input\ArgvInput;
use Symfony\Component\Console\Input\Input;
use Symfony\Component\Console\Input\InputDefinition;
use Symfony\Component\Console\Input\InputArgument;

class MigrationInput extends ArgvInput
{
    public function __construct()
    {
        // $customArgv = array_merge([""], $argv);
        // parent::__construct($argv, new InputDefinition($definitionArray));
        parent::__construct(
            ['zero' => null, 'version' => 'latest'],
            new InputDefinition([new InputArgument('version')])
        );
    }
}
