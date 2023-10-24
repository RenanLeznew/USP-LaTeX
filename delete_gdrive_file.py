# delete_gdrive_file.py
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

def delete_file(file_id):
    creds = None
    creds = service_account.Credentials.from_service_account_info(
        os.environ['DRIVESHHHH']
    )

    service = build('drive', 'v3', credentials=creds)

    service.files().delete(fileId=file_id).execute()

if __name__ == '__main__':
    FILE_ID = 'your-file-id-here'  # Replace with your file's ID
    delete_file(FILE_ID)
