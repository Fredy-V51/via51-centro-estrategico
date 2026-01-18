from v51_auth import get_drive
def crear_carpetas_campana():
    drive = get_drive()
    res = drive.files().list(q="name='VIA51_OPERACIONES'", fields="files(id)").execute()
    root_id = res['files'][0]['id']
    carpetas = ["04_REPORTES_MI_PARTIDO", "04_REPORTES_COMPETENCIA_ELECTORAL"]
    for c in carpetas:
        check = drive.files().list(q=f"name='{c}'").execute()
        if not check.get('files'):
            drive.files().create(body={'name':c,'parents':[root_id],'mimeType':'application/vnd.google-apps.folder'}).execute()
    print("✅ Carpetas electorales listas.")
if __name__ == '__main__': crear_carpetas_campana()
