from v51_auth import get_drive
AREAS = ["POLITICO-SOCIAL", "COMERCIAL", "INDUSTRIAL", "SERVICIOS", "TECNO-CIENCIA", "ORGANIZACIONES", "PERSONAS"]
def construir():
    drive = get_drive()
    res = drive.files().list(q="name='VIA51_OPERACIONES'", fields="files(id)").execute()
    root_id = res['files'][0]['id']
    for a in AREAS:
        n = f"04_REPORTES_{a}"
        c = drive.files().list(q=f"name='{n}'").execute()
        if not c.get('files'):
            drive.files().create(body={'name':n,'parents':[root_id],'mimeType':'application/vnd.google-apps.folder'}).execute()
    print("✅ Carpetas de Sectores verificadas.")
if __name__ == '__main__': construir()
