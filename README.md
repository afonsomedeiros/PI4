# PI4

## Lista de rotas.

- [ x ] /previsao - [GET]
- [ x ] /dados - [GET, POST]
- [ x ] /enviar - [POST]

## Sobre as rotas.

### /previsao.

Rota que faz a previsao com base na planilha em excel disponibilizada pelo silvio.

### /dados

Rota que exibe informações disponíveis na planilha excel.

### /enviar

Rota que recebe um json de entrada com os dados semelhantes aos dados da planilha, e gera uma predição em cima destes dados usando o modelo treinado pelo silvio.

modelo de arquivo:
```json
{
    "data": [
        {
            "PM25": 44.0,
            "O3": 30.0,
            "Dias": 44999
        },
        ...
        {
            "PM25": float,
            "O3": float,
            "Dias": inteiro
        }
    ]
}
```

## Como executar:

Requerimentos:
python 3.10 ou superior.

instalar virtualenv:

ubuntu.

```sh
$ sudo python3 -m pip install virtualenv
```

windows.

```pws
> python -m pip install virtualenv
```

Criando ambiente virtual:

ubuntu e windows.

```sh
$ virtualenv .venv
```

Acessando ambiente virtual:

ubuntu
```sh
$ source .venv/bin/activate
```

windows. `Precisa habilitar a execução de scripts pelo powershell (ou usar o prompt de comandos.)`
```pws
> .venv/Scripts/activate
```

Após criação e ativação do ambiente virtual ele deverá ser exibido no prompt da seguinte forma:

```
(.venv) user@host:path$ # ubuntu
(.venv) path> # windows
```

## Instalando as depêndencias.

Para instação da depêndencias basta executar o comando.

```
python -m pip install -r requirements.txt
```

Lembre-se de estar com o diretório aberto no terminal para localizar corretamente o arquivo requirements.txt.

## Executando o projeto:

```
python main.py

Bottle v0.13.2 server starting up (using WSGIRefServer())...
Listening on http://127.0.0.1:8080/
Hit Ctrl-C to quit.
```

Desta forma poderá acessar o host apresentado no prompt.