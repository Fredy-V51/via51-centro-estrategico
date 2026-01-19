import os

html_path = "C:/V51_PRODUCCION/index.html"
nuevo_analisis = """
<div class="card my-4 border-primary">
    <div class="card-header bg-primary text-white">
        <h5 class="mb-0">🏛️ Alerta de Inteligencia: Realidad Política y Minera</h5>
    </div>
    <div class="card-body">
        <p class="card-text"><strong>Resumen Ejecutivo:</strong> Crisis de institucionalidad y debilitamiento de organismos reguladores. El Caso Conga demuestra la inviabilidad de proyectos sin licencia social.</p>
        
        <h6>Componentes Afectados:</h6>
        <ul>
            <li><strong>Componente 02 (Infraestructura):</strong> Conflictos en cabeceras de cuenca afectan la viabilidad del recurso hídrico.</li>
            <li><strong>Componente 05 (Minero/Industrial):</strong> Necesidad de corregir Estudios de Impacto Ambiental para obtener legitimidad social.</li>
            <li><strong>Componente 07 (Tecnociencia):</strong> Propuesta de uso de <strong>Big Data</strong> para fiscalizar proveedores del Estado y detectar cartas fianza falsas.</li>
        </ul>
        
        <div class="alert alert-warning">
            <strong>Alerta de Monitor:</strong> Se requiere vigilancia ciudadana digital para exponer redes de impunidad institucional.
        </div>
    </div>
    <div class="card-footer text-muted">
        Análisis generado vía V51-ANALYSIS - Paso de Vencedores
    </div>
</div>
"""

try:
    if os.path.exists(html_path):
        with open(html_path, "r", encoding="utf-8") as f:
            contenido = f.read()
        
        # Insertar el análisis antes del cierre de la sección principal o del body
        if "" in contenido:
            nuevo_contenido = contenido.replace("", nuevo_analisis + "\n")
        else:
            nuevo_contenido = contenido.replace("</body>", nuevo_analisis + "\n</body>")
            
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(nuevo_contenido)
        print("✅ Portal actualizado con éxito en index.html")
    else:
        print("⚠️ No se encontró index.html. Creando estructura base...")
        # (Aquí se podría crear un index.html base si no existe)
except Exception as e:
    print(f"❌ Error al actualizar el portal: {e}")
