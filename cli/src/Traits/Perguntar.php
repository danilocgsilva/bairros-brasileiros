<?php

namespace Danilocgsilva\BairrosBrasileirosLinhaDeComandos\Traits;

use Symfony\Component\Console\Question\Question;

trait Perguntar
{
    private function perguntar(string $tituloPergunta): string
    {
        $helper = $this->getHelper('question');
        $pergunta = new Question($tituloPergunta . ': ');

        return $helper->ask($this->input, $this->output, $pergunta);
    }
}
