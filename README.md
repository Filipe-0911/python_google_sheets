[Início rápido do Python no Google Sheets](https://developers.google.com/sheets/api/quickstart/python?hl=pt-br)

# Guia de início rápido do Python
## Os guias de início rápido explicam como configurar e executar um app que chama uma API Google Workspace.
## Os guias de início rápido do Google Workspace usam as bibliotecas de cliente da API para processar alguns detalhes do fluxo de autenticação e autorização. Recomendamos que você use bibliotecas de cliente para seus próprios aplicativos. Neste guia de início rápido, usamos uma abordagem de autenticação simplificada, apropriada para um ambiente de teste. Para um ambiente de produção, recomendamos aprender sobre autenticação e autorização antes de escolher as credenciais de acesso adequadas para seu aplicativo.
### Crie um aplicativo de linha de comando em Python que faça solicitações à API Google Sheets.

Objetivos:
<ul>
  <li>Configurar o ambiente.</li>  
  <li>Instale a biblioteca de cliente.</li>  
  <li>Configure a amostra.</li>  
  <li>Execute a amostra.</li>  
  <li>Pré-requisitos</li>  
</ul>


> Para executar este guia de início rápido, você precisa dos seguintes pré-requisitos:

1. Python 3.10.7 ou superior
2. A ferramenta de gerenciamento de pacotes pip
3. Um projeto do Google Cloud.
4. Uma Conta do Google
5. configure seu ambiente
6. Para concluir este guia de início rápido, configure seu ambiente.

Ativar a API
Antes de usar as APIs do Google, elas precisam ser ativadas em um projeto do Google Cloud. É possível ativar uma ou mais APIs em um único projeto do Google Cloud.
> No console do Google Cloud, ative a API Google Sheets.

[Ativar a API](https://console.cloud.google.com/flows/enableapi?apiid=sheets.googleapis.com&hl=pt-br)

Configurar a tela de permissão OAuth
Se você estiver usando um novo projeto do Google Cloud para concluir este guia de início rápido, configure a tela de permissão OAuth e adicione-se como um usuário de teste. Se você já concluiu essa etapa no projeto do Cloud, pule para a próxima seção.

No console do Google Cloud, acesse Menu menu > APIs e serviços > Tela de permissão OAuth.
[Acessar a tela de permissão OAuth](https://console.cloud.google.com/apis/credentials/consent?hl=pt-br)

Selecione o tipo de usuário do app e clique em Criar.
Preencha o formulário de registro do app e clique em Salvar e continuar.
Por enquanto, é possível pular a adição de escopos e clicar em Salvar e continuar. No futuro, ao criar um app para uso fora da organização do Google Workspace, será necessário adicionar e verificar os escopos de autorização exigidos pelo app.

Se você selecionou Externo como tipo de usuário, adicione usuários de teste:
Em Usuários de teste, clique em Adicionar usuários.
Insira seu endereço de e-mail e outros usuários de teste autorizados, depois clique em Salvar e continuar.
Analise o resumo de registro do seu app. Para fazer mudanças, clique em Editar. Se o registro do app parecer OK, clique em Voltar ao painel.
Autorizar credenciais de um aplicativo para computador
Para fazer a autenticação como usuário final e acessar os dados do usuário no app, crie um ou mais IDs do cliente OAuth 2.0. Um ID do cliente é usado para identificar um único app nos servidores OAuth do Google. Se o app for executado em várias plataformas, você precisará criar um ID do cliente separado para cada uma delas.
No console do Google Cloud, acesse Menu menu > APIs e serviços > Credenciais.
[Ir para Credenciais](https://console.cloud.google.com/apis/credentials/consent?hl=pt-br)

* Clique em Criar credenciais > ID do cliente OAuth.
* Clique em Tipo de aplicativo > App para computador.
* No campo Nome, digite um nome para a credencial. Esse nome só aparece no console do Google Cloud.
* Clique em Criar. A tela do cliente OAuth criado é exibida, mostrando seu novo ID e chave secreta do cliente.
* Clique em OK. A credencial recém-criada aparece em IDs do cliente OAuth 2.0.
* Salve o arquivo JSON salvo como credentials.json e mova o arquivo para o diretório de trabalho.
* Instalar a biblioteca de cliente do Google
* Instale a biblioteca de cliente do Google para Python:

`pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`
Configurar o exemplo

1. No diretório de trabalho, crie um arquivo chamado quickstart.py.
2. Inclua o seguinte código em quickstart.py:

```
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms"
SAMPLE_RANGE_NAME = "Class Data!A2:E"


def main():
  """Shows basic usage of the Sheets API.
  Prints values from a sample spreadsheet.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = (
        sheet.values()
        .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
        .execute()
    )
    values = result.get("values", [])

    if not values:
      print("No data found.")
      return

    print("Name, Major:")
    for row in values:
      # Print columns A and E, which correspond to indices 0 and 4.
      print(f"{row[0]}, {row[4]}")
  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()
```

No diretório de trabalho, crie e execute o exemplo:

`python3 quickstart.p`

Ao executar o exemplo pela primeira vez, você precisa autorizar o acesso:
Se você ainda não tiver feito login na sua Conta do Google, faça login quando solicitado. Se você tiver feito login em várias contas, selecione uma para usar para autorização.
Clique em Aceitar.
Seu aplicativo em Python é executado e chama a API Google Sheets.

As informações de autorização são armazenadas no sistema de arquivos. Portanto, na próxima vez que você executar o exemplo de código, a autorização não será solicitada.

Próximas etapas
Resolver problemas de autenticação e autorização
Documentação de referência da API Sheets
Documentação do cliente de APIs do Google para Python
Documentação do PyDoc da API Google Sheets
