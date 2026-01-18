import os
import json
from datetime import datetime

PATH_ENTRADA = "C:/V51_PRODUCCION/02_ENTRADA/"
PATH_COMPONENTE = "C:/V51_PRODUCCION/COMPONENTES/"

def auditar_sistema():
    reporte = {
        "fecha_auditoria": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "archivos_V51_detectados": [f for f in os.listdir(PATH_ENTRADA) if f.startswith("V51_")],
        "motor_html_presente": os.path.exists("C:/V51_PRODUCCION/v51_html.py"),
        "index_creado": os.path.exists("C:/V51_PRODUCCION/index.html")
    }
    
    print("\n--- 🏛️ AUDITORÍA DE EJECUCIÓN VÍA 51 ---")
    print(f"Última comprobación: {reporte['fecha_auditoria']}")
    print(f"Regiones en Sistema: {len(reporte['archivos_V51_detectados'])}")
    for reg in reporte['archivos_V51_detectados']:
        print(f"  [OK] {reg}")
    
    if not reporte['index_creado']:
        print("  [!] ADVERTENCIA: El portal index.html aún no se ha generado.")
    
    with open(os.path.join(PATH_COMPONENTE, "v51_status.json"), "w") as f:
        json.dump(reporte, f, indent=4)

if __name__ == "__main__":
    auditar_sistema()
