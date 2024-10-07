<?php

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos;

use Symfony\Component\Console\Input\ArgvInput;

class MigrationInput extends ArgvInput
{
    public function setValue($name, $value)
    {
        $this->arguments[$name] = $value;
    }
}
