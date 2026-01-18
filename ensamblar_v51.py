import os
from v51_auth import get_docs, get_drive

def ensamblar():
    ruta_comp = "C:/V51_PRODUCCION/COMPONENTES/"
    secuencia_path = os.path.join(ruta_comp, "secuencia.txt")
    
    # Leer secuencia eliminando el BOM de Windows si existe
    with open(secuencia_path, "r", encoding="utf-8-sig") as f:
        archivos = [line.strip().strip('\ufeff') for line in f if line.strip()]
    
    cuerpo_doc = []
    indice = "🏛️ ÍNDICE DE NAVEGACIÓN\n====================\n"
    
    for nombre in archivos:
        path_archivo = os.path.join(ruta_comp, nombre)
        # Extraer nombre limpio para el título
        titulo_seccion = nombre.replace(".txt", "").split("_")[-1].upper()
        
        if os.path.exists(path_archivo):
            with open(path_archivo, "r", encoding="utf-8-sig") as f_part:
                contenido = f_part.read()
                cuerpo_doc.append(f"\n--- INICIO SECCIÓN: {titulo_seccion} ---\n")
                cuerpo_doc.append(contenido)
                cuerpo_doc.append(f"\n[VOLVER AL ÍNDICE]\n")
                indice += f"👉 SECCIÓN {titulo_seccion}\n"
        else:
            print(f"⚠️ Advertencia: No se encontró {nombre}")

    contenido_final = indice + "\n" + "".join(cuerpo_doc)
    
    # Sincronizar con la nube
    try:
        drive, docs = get_drive(), get_docs()
        res = drive.files().list(q="name='VÍA 51: MAPA MAESTRO'", fields="files(id)").execute()
        if not res['files']: 
            print("❌ No se encontró el Mapa Maestro en Drive.")
            return
        doc_id = res['files'][0]['id']
        
        # Actualización
        docs.documents().batchUpdate(documentId=doc_id, body={'requests': [
            {'insertText': {'location': {'index': 1}, 'text': contenido_final}}
        ]}).execute()
        print(f"✅ Sincronización exitosa. Portal actualizado.")
    except Exception as e:
        print(f"❌ Error en la conexión: {e}")

if __name__ == '__main__': ensamblar()
