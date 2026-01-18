from v51_auth import get_drive

def crear_estructura_medios():
    drive = get_drive()
    res = drive.files().list(q="name='04_REPORTES_MI_PARTIDO'", fields="files(id)").execute()
    padre_id = res['files'][0]['id']
    
    niveles = ["PRESIDENCIAL", "SENADO", "DIPUTADOS", "PARLANDINO"]
    for nivel in niveles:
        nombre = f"MEDIOS_{nivel}"
        check = drive.files().list(q=f"name='{nombre}' and '{padre_id}' in parents").execute()
        if not check.get('files'):
            drive.files().create(body={'name': nombre, 'parents': [padre_id], 'mimeType': 'application/vnd.google-apps.folder'}).execute()
    print("✅ Carpetas de seguimiento de medios creadas.")

if __name__ == '__main__': crear_estructura_medios()
