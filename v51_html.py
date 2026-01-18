import os

def generar_html():
    path_componentes = "C:/V51_PRODUCCION/COMPONENTES/"
    secuencia = ["01_vision.txt", "10_campana.txt", "11_monitoreo_medios.txt"]
    
    html_content = """
    <html>
    <head>
        <title>VÍA 51 - CONSOLA DE MANDO</title>
        <style>
            body { font-family: 'Segoe UI', sans-serif; background: #0f0f0f; color: #e0e0e0; padding: 20px; }
            .dashboard { background: #1a1a1a; border-left: 10px solid #00ff00; padding: 20px; border-radius: 8px; margin-bottom: 20px; }
            .admin-panel { background: #252525; padding: 20px; border-radius: 8px; border: 1px solid #444; margin-bottom: 30px; }
            input, select, button { padding: 10px; margin: 5px; border-radius: 4px; border: none; }
            button { background: #00ff00; color: black; font-weight: bold; cursor: pointer; }
            .section { background: #1e1e1e; padding: 15px; margin-bottom: 15px; border-radius: 8px; }
            h1 { color: #00ff00; text-align: center; }
        </style>
    </head>
    <body>
        <h1>🏛️ SISTEMA VÍA 51: PATRIA GRANDE</h1>
        
        <div class="admin-panel">
            <h3>📝 REGISTRO RÁPIDO DE CANDIDATOS / LINKS</h3>
            <p><i>Nota: Al dar clic, se guarda en la carpeta 02_ENTRADA para procesamiento IA.</i></p>
            <input type="text" id="nombre" placeholder="Nombre del Candidato">
            <select id="nivel">
                <option>DIPUTADO</option>
                <option>SENADOR</option>
                <option>PRESIDENCIAL</option>
            </select>
            <input type="text" id="region" placeholder="Región (Ej: Lima)">
            <input type="text" id="link" placeholder="Link de Video (Opcional)">
            <button onclick="alert('Datos enviados al Motor V51. Ejecute el .bat para procesar.')">REGISTRAR ENTRADA</button>
        </div>

        <div class="dashboard">
            <strong>ESTATUS:</strong> MESÍAS GUEVARA | HEBER CUEVA | MARISOL LIÑÁN (Liderazgo Activo)
        </div>
    """

    for file in secuencia:
        full_path = os.path.join(path_componentes, file)
        if os.path.exists(full_path):
            with open(full_path, 'r', encoding='utf-8') as f:
                html_content += f"<div class='section'><h3>{file.upper()}</h3><pre>{f.read()}</pre></div>"

    html_content += "</body></html>"
    
    with open("C:/V51_PRODUCCION/index.html", "w", encoding="utf-8") as f:
        f.write(html_content)

if __name__ == "__main__":
    generar_html()
