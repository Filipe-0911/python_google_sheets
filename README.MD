# Programa python que interage com google sheets

Criei este programa com o objetivo de facilitar alguns processos feitos no meu local de trabalho.

Projeto feito em python com paradigma de POO. Utilizei bibliotecas do Google Cloud para integração com API's do google e armazenar os dados em um banco de dados SQL. Utilizei a biblioteca sqlite3 do python para isso.

> Para utilizar este programa, você deve seguir os passos descritos neste [artigo do google](https://developers.google.com/sheets/api/quickstart/python?hl=pt-br).

Será necessário realizar todos os procedimentos que estão no link acima para obter o arquivo credentials.json e token.json. Salve estes arquivos em uma pasta auth na pasta raiz do projeto.

> IMPORTANTE: O arquivo token.json será gerado quando executar o arquivo interface.py e clicar em qualquer um dos botões. Quando clicar, será redirecionado para uma página do google para autorizar a execução do script.

Após isto, pegue o id da planilha e crie um arquivo .env com o seguinte contúdo:

```
SECRET_KEY = ID_DA_PLANILHA
```

Salve este arquivo na pasta Raiz do projeto.

## Modo de utilização

Execute o arquivo interface.py e clique em um dos botões. O programa criará um banco de dados dentro de uma pasta database. OBS.: Não é necessário criar esta pasta.

