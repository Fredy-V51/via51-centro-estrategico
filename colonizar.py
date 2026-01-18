import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import pickle

# Alcances: Acceso total a Drive y Documentos
SCOPES = ['https://www.googleapis.com/auth/drive', 'https://www.googleapis.com/auth/documents']

def colonizar_via51():
    creds = None
    # El archivo token.pickle almacena los tokens de acceso del usuario
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
            
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    drive_service = build('drive', 'v3', credentials=creds)
    docs_service = build('docs', 'v1', credentials=creds)

    # 1. Crear Carpeta Raíz
    folder_metadata = {'name': 'VIA51_OPERACIONES', 'mimeType': 'application/vnd.google-apps.folder'}
    root_folder = drive_service.files().create(body=folder_metadata, fields='id').execute()
    root_id = root_folder.get('id')
    print(f"✅ Carpeta Raíz Creada: {root_id}")

    # 2. Crear Subcarpetas
    subcarpetas = [
        "01_DOCUMENTACION", "02_ENTRADA", "03_MOTOR_IA", "04_REPORTES", "05_CONFIG"
    ]
    for sub in subcarpetas:
        sub_metadata = {
            'name': sub,
            'parents': [root_id],
            'mimeType': 'application/vnd.google-apps.folder'
        }
        drive_service.files().create(body=sub_metadata).execute()
    
    # 3. Crear Documento Maestro (WIKI)
    doc_metadata = {
        'title': 'VÍA 51: MAPA MAESTRO',
        'parents': [root_id]
    }
    doc_file = drive_service.files().create(body={'name': 'VÍA 51: MAPA MAESTRO', 'parents': [root_id], 'mimeType': 'application/vnd.google-apps.document'}).execute()
    doc_id = doc_file.get('id')
    
    print(f"🚀 Infraestructura lista. Documento Maestro ID: {doc_id}")
    print("Navega a Google Drive para ver tu nuevo ecosistema.")

if __name__ == '__main__':
    colonizar_via51()