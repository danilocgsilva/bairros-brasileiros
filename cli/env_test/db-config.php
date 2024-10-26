<?php

return [
    'dbname' => getenv('BAIRROS_BRASILEIROS_DB_NOME_TESTE'),
    'user' => getenv('BAIRROS_BRASILEIROS_DB_USUARIO'),
    'password' => getenv('BAIRROS_BRASILEIROS_DB_SENHA'),
    'host' => getenv('BAIRROS_BRASILEIROS_DB_HOST'),
    'driver' => 'pdo_mysql',
];