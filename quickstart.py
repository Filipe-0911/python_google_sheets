import os.path
import os

from dotenv import load_dotenv
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

load_dotenv()
SAMPLE_SPREADSHEET_ID = str(os.getenv('SECRET_KEY'))
SAMPLE_RANGE_NAME = str(os.getenv('LOCAL_LEITURA'))

def main():
  creds = None

  token_path = os.path.join(os.path.dirname(__file__), "auth", "token.json")
  if os.path.exists(token_path):
    creds = Credentials.from_authorized_user_file(token_path, SCOPES)

  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
           os.path.join(os.path.dirname(__file__), "auth", "credentials.json"), SCOPES
      )
      creds = flow.run_local_server(port=0)
    with open(os.path.join(os.path.dirname(__file__), "auth", "token.json"), "w") as token:
      token.write(creds.to_json())

  try:
    service = build("sheets", "v4", credentials=creds)

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

    return values
    
  except HttpError as err:
    print(err)


if __name__ == "__main__":
  main()