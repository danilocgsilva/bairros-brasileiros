# Documentação

## Banco de dados

A receita para a criação de banco de dados se encontra no arquivo `migrations.sql`.

Você encontra neste arquivo:

* Criação do banco de dados, no caso já nomeado como `bairros_brasileiros`.
* A tabela `locais`. Elas podem ser o bairro, mas também podem ser cidades. Por isso se chamado `locais`, de forma genérica representa um local, que pode ser um bairro, uma cidade ou mesmo outro tipo de denominação.
* A tabela `tipos_locais`, que é o registro do *tipo de localidade*. Determina se um *local* (registrado na tabela `locais`) é um bairro, uma cidade ou outro tipo de localidade.
