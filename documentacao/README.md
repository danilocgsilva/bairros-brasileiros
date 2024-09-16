# Documentação

## Banco de dados

A receita para a criação de banco de dados se encontra no arquivo `migrations.sql`.

Você encontra neste arquivo:

* Criação do banco de dados, no caso já nomeado como `bairros_brasileiros`.
* A tabela `locais`. Elas podem ser o bairro, mas também podem ser cidades. Por isso se chamado `locais`, de forma genérica representa um local, que pode ser um bairro, uma cidade ou mesmo outro tipo de denominação.
* A tabela `tipos_locais`, que é o registro do *tipo de localidade*. Determina se um *local* (registrado na tabela `locais`) é um bairro, uma cidade ou outro tipo de localidade.

## Receita de desenvolvimento

O pacote atual está com os features necessários para o desenvolvimento:

* debugconfig: contém a receita de configuração do xdebug, necessário para a aplicação em linha de comando.

* app/.vscode/launch.json: configurações necessárias para debugar a aplicação em python.

## Como iniciar o ambiente de desenvolvimento

### Passo 1: inicie os containers

Na raíz de diretórios do projeto, execute `docker compose up -d --build` para levantar os containers.

### Passo 2: inicie o servidor flask

Entre no container da aplicação python execute o comando: `flask run --host=0.0.0.0`

A porta 5000 fica exposta no ambiente local para poder executar as ações via API.

## Desenvolvendo o client linha de comando

Para a utilização do código python, foi desenvolvido um client via linha de comando (presente no container `bairros_brasileiros_cli`, do arquivo de receita na raiz `docker-compose.yml`). O ponto de entrada da aplicação é o arquivo `bairros`.

Para o desenvolvimento, recomendo executar os comandos dentro do container de PHP, pois isso dispara o xdebug, permitindo o debug com break-points.

No ambiente local, temos o acesso rápido que permite o usuário executar comando pelo ambiente local. Basta tornar o arquivo `bairros` executável e executá-lo.
