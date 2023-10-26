import os
import base64
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
test_var = os.environ["DRIVESHHHH"]
def get_file_id(file_name):
    query = f"name='{file_name}'"
    creds = service_account.Credentials.from_service_account_info(json.loads(base64.b64decode(test_var).decode('utf-8')))
    service = build('drive', 'v3', credentials=creds)

    results = service.files().list(q=query).execute()
    files = results.get('files', [])
    
    if files:
        file = files[0]  # Assumes the file name is unique within your Drive
        file_id = file.get('id')
        return file_id
    else:
        print(f'No file found with name: {file_name}')
        return None
    
def delete_file(file_id):
    creds = service_account.Credentials.from_service_account_info(json.loads(base64.b64decode(test_var).decode('utf-8')))
    service = build('drive', 'v3', credentials=creds)

    service.files().delete(fileId=file_id).execute()

def list_files():
    creds = service_account.Credentials.from_service_account_info(json.loads(base64.b64decode(test_var).decode('utf-8')))
    service = build('drive', 'v3', credentials=creds)

    results = []
    page_token = None
    while True:
        response = service.files().list(
            q="trashed=false",  # This query parameter will ensure to list files that are not in the trash
            fields="nextPageToken, files(id, name)",
            pageToken=page_token
        ).execute()
        results.extend(response.get('files', []))
        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break
    response.clear()
    return results
    
print("oi")

def main(file_name):
    file_id = get_file_id(file_name)
    if file_id:
        delete_file(file_id)

if __name__ == '__main__':
    FILES = list_files()
    for file in FILES:
        if file["id"]!='1aS3fF7XhO1DM_PM8ZS4mqTBwxi8FWGoc':
            main(file["name"])
        else:
            continue
