import os

def crear_cronica_amena(texto_analisis):
    # Estructura de "Crónica Fidedigna"
    cronica = f"""
    <div class="card my-4 shadow-sm border-0">
        <div class="card-body bg-light">
            <h3 class="text-primary"><i class="fas fa-newspaper"></i> Crónica V51: El Pulso de la Realidad</h3>
            <hr>
            
            <div class="row">
                <div class="col-md-4 border-end">
                    <h5 class="text-secondary">🧐 ¿De qué se trata?</h5>
                    <p>Una radiografía cruda sobre la minería y la institucionalidad en el Perú, centrada en por qué los proyectos se detienen cuando se ignora el factor humano y ambiental.</p>
                </div>
                <div class="col-md-4 border-end">
                    <h5 class="text-secondary">👥 ¿Quiénes intervienen?</h5>
                    <ul>
                        <li><strong>Las Comunidades:</strong> Guardianes del agua en las cabeceras de cuenca.</li>
                        <li><strong>El Estado:</strong> Organismos como OEFA e Ingemmet, hoy debilitados.</li>
                        <li><strong>La Red de Impunidad:</strong> Actores que operan en la sombra de las licitaciones.</li>
                    </ul>
                </div>
                <div class="col-md-4">
                    <h5 class="text-secondary">💡 La Solución V51</h5>
                    <p>No es falta de dinero, es falta de <strong>liderazgo digital</strong>. El Big Data y la vigilancia ciudadana son las herramientas para recuperar el control.</p>
                </div>
            </div>
            
            <div class="alert alert-info mt-3">
                <strong>Nota del Analista:</strong> Esta lectura ha sido procesada para ser fiel a los hechos, eliminando el ruido político y enfocándose en las soluciones técnicas del Ayllu Morado.
            </div>
        </div>
    </div>
    """
    return cronica

# Ruta del portal
html_path = "C:/V51_PRODUCCION/index.html"

if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        contenido = f.read()
    
    # Generar la crónica
    nueva_seccion = crear_cronica_amena("")
    
    # Insertar al principio del contenido para que sea lo primero que se lea
    if "<body>" in contenido:
        # Usamos una inserción limpia justo después de la apertura del body o del contenedor principal
        contenido_actualizado = contenido.replace("<body>", "<body>\n" + nueva_seccion)
        
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(contenido_actualizado)
        print("✅ Servicio 'V51-CRONISTA' implementado. Lectura amena añadida.")
else:
    print("❌ No se encontró el index.html para editar.")
