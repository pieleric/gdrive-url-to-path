#!/usr/bin/python3

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


import sys
import os

# To get an API OAuth credential see https://developers.google.com/drive/api/quickstart/python
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]
CRED_FILE = "/home/piel/google-credential.json"
TOKEN_FILE = "/home/piel/google-token.json"

def get_drive_service():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(TOKEN_FILE):
        creds = Credentials.from_authorized_user_file(TOKEN_FILE, SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CRED_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(TOKEN_FILE, "w") as token:
            token.write(creds.to_json())

    return build('drive', 'v3', credentials=creds)

def get_drive_name(service, drive_id):
    drive = service.drives().get(driveId=drive_id).execute()
    return drive["name"]

def get_full_path(service, file_id):
    try:
        #print(f"Searching for {file_id}")
        file = service.files().get(fileId=file_id, fields='name, parents, driveId', supportsAllDrives=True).execute()
        if 'parents' in file:
            parent_id = file['parents'][0]  # Assumes the file has exactly one parent
            parent_path = get_full_path(service, parent_id)
            return parent_path + '/' + file['name']
        else:
            if "driveId" in file:  # Special way to show the name of the shared drive
                return get_drive_name(service, file["driveId"])
            else:
                return file['name']

    except HttpError as error:
        print(f'An error occurred: {error}')
        return None

def get_path_from_url(service, url):
    file_id = url.split('/d/')[1].split('/view')[0] # TODO: remove /edit? too
    return get_full_path(service, file_id)

service = get_drive_service()
url = sys.argv[1]
print(get_path_from_url(service, url))
