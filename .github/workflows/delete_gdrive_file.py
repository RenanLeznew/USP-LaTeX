import os
import base64
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
test_var = """ewogICJ0eXBlIjogInNlcnZpY2VfYWNjb3VudCIsCiAgInByb2plY3RfaWQiOiAiY2xhc3Nlc3Bk
ZnMiLAogICJwcml2YXRlX2tleV9pZCI6ICJhODlkZWUzZjQ2ZWNhYzJhMjMwY2NiZWFlNDMyZWE1
MWZhMzVjMDAzIiwKICAicHJpdmF0ZV9rZXkiOiAiLS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0t
XG5NSUlFdlFJQkFEQU5CZ2txaGtpRzl3MEJBUUVGQUFTQ0JLY3dnZ1NqQWdFQUFvSUJBUURrQ2Z1
TVFBLzlNb1h4XG5vOURWWlQ4RkQyMU95SXNsVG0rZFI0dHI2Q1ROSWdPU1VieFhYcVJaL3M4NHpv
NFRXMHNCa1hQdTNTWnJCTGNTXG4xWVRmRkx4MTZYeXdvWWZBNGFlOTJ2cm9UWjRtRWkrNlJSbkdF
S0poRFpua3FIN2xyeFFvUWVUbU5Dc21BcXQzXG5JRlJYL3ZycXArUEhadDBZdkp3Zk1kakNvTnpE
R255dkZIQnNZNi9qVmh5a3NYK1ZLTCt3YTd6aGtsWnFjRXpNXG5UMWVpL1JVeVBzQ2F5S3dMa3Rx
N3ZNaER0eklTeG5GWDZockQ5TUJTbWtFTm1TWDNKQ0VPY0FCdCt0RllUSG8wXG5KaUtrZ2ZYd0FT
d1ZvL2FsZnQ3bFVJMm50NFdPS1ExdDBNVjBKS0xaSWdwTHY3UUZGY2FkZG5CQm5NdUZVV0dHXG5J
czhCWHZlZkFnTUJBQUVDZ2dFQWF3dDBsWVdNKytJM2xoSzcrVEFwd1FwWTJWNnlVclRiR0ExNW1S
SEVGTGNlXG56aFNvUUtzZ28wNUZuL2oySUlmK1VhSWh0Y01DUWNKWTNmSjFDUE1HOUtMQjhYZ2g3
Wnovek5ONmJJbmk3eVFpXG5XMklNa3psRHdDTk9WbFB5SFlkdUF1Zkx0M1JOdk80TDUwTzUxQVRS
YkUyYlV3TXFUbTViS3htUEV1M0lNNXpjXG5aWHY3Q1V4NFJzcS9tcVMxankxclM3d29Bd0ZsL2I5
WnNQR0ZYaFh2TkJGQmh4RitDMWdFa3dmbkdHdHN5bEdRXG52cHRWMGtweDloYkc3bmxvS2NIVk5T
OVRQU0dlWXVQa2x3YXozckQ2UlQyN2w0L0xET0tteFEvaXdGcEFaeDRWXG5seEM1UHVvOWlEbzk2
U054c2NvUkMwQVFuYVdFQ09JcWZIVEM4S3dSWVFLQmdRRDZrSTZMU1cwMXZMRE5iSkF0XG5ZSnda
SSs2a2s0T20vdkFLVnc4QzNlYmJ6OEZ4bDFmLzdhS25WcWtmdDhpSmtLamR5YlYxMWdDNkNvNTNJ
V0NnXG4zdkVWZmllY1d4QUpnZzQvVWNKeWEzZTFxTEVURXJBZFloTklsWUNjK3AzekVvVHp0clZw
a3JhcU0vNURZZmRVXG5rTGhuQkVkUzlteERLL0Q0RVlXWFhyQndKUUtCZ1FEby9GWGtqMkRZVW4y
MmZqb21pUkg0NjlMR09yMXRPTXU1XG5EV2dXbUhUZ3VuV3NSdk9iM2RpaW5ER2hqYzcrVm1SUTh3
OStjQkNNV2dPZ0VuOFl5anBQWCtvT1N2OE9PMWlRXG5ORmcyeVA1VHFtZDlsd3VvMDd1VFVZVmh2
dDIzNG5rVzZPSUoxWjRRdVMzNldEOGN6bkFPYjk0SUhCc2RycEhRXG5KenN5TXE4TGN3S0JnSE5o
eS9KQ0hzTkhIOWVJN1orbnhGb2pYTXAyajRLQUZVTjlzWkR0WkZqR2c5cnVDWHoyXG5EaGVtNVh5
UW9nMFBDMlFPZGJ4TWpzc2MvMXZHaC91c2pqSUtoTzBRVmdNNjI1cTI2S2JON0RNLytrTEJNVTVt
XG5rbUN6VDZWNkZ2QVBFQ0EyZTdXZzlQTE52SUdGQkdMeHZhamFwSW1FcG5nTUxRdmU3YmkxeHVQ
dEFvR0JBTHQwXG4yNzhNUllXSHliSWRtYmdMclRRMHVkL1l2elN6NytZeWpUOHc1MGt4ZlNCaDdm
dkk0VmJraVdKTThQRGVuZFFyXG4zSm1FblN2ditON0FReGExRDNseDJLWXJYVkFjRzhQYStlY0tq
T2JRUW5oZ0lYZHk5SWN4bmpucEVnZXo1bTJ5XG5icnd1N2dEU25kWEJUdlprZXZDQ3ZZaVU1SlJi
TXVMaHpkVXp4bmRWQW9HQVZSQnNickF5Vk4yN3NEYzZpTTVqXG5mUEtOVHNTOWFoR0ZHbCtoYm1Z
RE9pVWVBeERsN25NWGZXMENmRTZEYW9YL1JWaXUxcXNka1hlaHN0RGtoWXgyXG5lQzdLeUxveEho
SSthckxDd0JwNFJDcHdzS2lOTzdXWithTWlINE85YlZucER1NjdvZHJSaHVaMGJta2lrTEdGXG5E
OU5BZUNoUHE5N2NPb2pjTnhWTDd1ST1cbi0tLS0tRU5EIFBSSVZBVEUgS0VZLS0tLS1cbiIsCiAg
ImNsaWVudF9lbWFpbCI6ICJkcml2ZXJwZGZzQGNsYXNzZXNwZGZzLmlhbS5nc2VydmljZWFjY291
bnQuY29tIiwKICAiY2xpZW50X2lkIjogIjEwNjE1ODc0MzU3NzQ3NzYzMzUxMyIsCiAgImF1dGhf
dXJpIjogImh0dHBzOi8vYWNjb3VudHMuZ29vZ2xlLmNvbS9vL29hdXRoMi9hdXRoIiwKICAidG9r
ZW5fdXJpIjogImh0dHBzOi8vb2F1dGgyLmdvb2dsZWFwaXMuY29tL3Rva2VuIiwKICAiYXV0aF9w
cm92aWRlcl94NTA5X2NlcnRfdXJsIjogImh0dHBzOi8vd3d3Lmdvb2dsZWFwaXMuY29tL29hdXRo
Mi92MS9jZXJ0cyIsCiAgImNsaWVudF94NTA5X2NlcnRfdXJsIjogImh0dHBzOi8vd3d3Lmdvb2ds
ZWFwaXMuY29tL3JvYm90L3YxL21ldGFkYXRhL3g1MDkvZHJpdmVycGRmcyU0MGNsYXNzZXNwZGZz
LmlhbS5nc2VydmljZWFjY291bnQuY29tIiwKICAidW5pdmVyc2VfZG9tYWluIjogImdvb2dsZWFw
aXMuY29tIgp9Cg=="""

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
