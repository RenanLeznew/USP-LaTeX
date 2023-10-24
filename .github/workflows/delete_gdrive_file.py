import os
import base64
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build

def get_file_id(service, file_name):
    query = f"name='{file_name}'"
    results = service.files().list(q=query).execute()
    files = results.get('files', [])
    
    if files:
        file = files[0]  # Assumes the file name is unique within your Drive
        file_id = file.get('id')
        return file_id
    else:
        print(f'No file found with name: {file_name}')
        return None

    query = f"name='{file_name}'"
    
def delete_file(service, file_id):
    service.files().delete(fileId=file_id).execute()
    print(f'Deleted file with ID: {file_id}')

def list_files():
#   with open('/home/rnzl/Downloads/classespdfs-a89dee3f46ec.json', 'r') as file:
#       creds_json = json.load(file)
#       creds = service_account.Credentials.from_service_account_info(creds_json)
    # Get the base64-encoded credentials string from the environment variable
    creds_base64_str = os.environ['GDRIVE_SERVICE_ACCOUNT_CREDS']
    # Decode the base64-encoded string
    creds_json_str = base64.b64decode(creds_base64_str).decode('utf-8')
    # Parse the JSON string to a dictionary
    creds_json = json.loads(creds_json_str)
    # Create a Credentials object from the dictionary
    creds = service_account.Credentials.from_service_account_info(creds_json)
    # Build and return the Google Drive API service client
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
    

def main(file_name):
#   with open('/home/rnzl/Downloads/classespdfs-a89dee3f46ec.json', 'r') as file:
#       creds_json = json.load(file)
#       creds = service_account.Credentials.from_service_account_info(creds_json)
    # Get the base64-encoded credentials string from the environment variable
    creds_base64_str = os.environ['GDRIVE_SERVICE_ACCOUNT_CREDS']
    # Decode the base64-encoded string
    creds_json_str = base64.b64decode(creds_base64_str).decode('utf-8')
    # Parse the JSON string to a dictionary
    creds_json = json.loads(creds_json_str)
    # Create a Credentials object from the dictionary
    creds = service_account.Credentials.from_service_account_info(creds_json)
    # Build and return the Google Drive API service client
    service = build('drive', 'v3', credentials=creds)
    
    file_id = get_file_id(service, file_name)
    if file_id:
        delete_file(service, file_id)

if __name__ == '__main__':
    FILES = list_files()
#    FILES = [
#              'algebra_notes.pdf', 
#              'analysis_notes.pdf',
#              'metric_notes.pdf',
#              'physics_notes.pdf',
#              'physicsII_notes.pdf',
#              'linear_algebra_notes.pdf',
#              'complex.pdf',
#              'probability_notes.pdf'
#               ]  # Replace with your file's name
    for file in FILES:
        if file["id"]!='1aS3fF7XhO1DM_PM8ZS4mqTBwxi8FWGoc':
            main(file)
        else:
            continue
