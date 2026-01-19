import google.generativeai as genai
import v51_config
import os

# Configuración del Cerebro
genai.configure(api_key=v51_config.API_KEY)
model = genai.GenerativeModel(v51_config.MODEL_NAME)

def analizar_discurso(texto_transcrito):
    prompt = f"""
    Eres el Analista de Inteligencia de Vía 51. Tu misión es procesar este texto bajo los 
    11 componentes del Plan de Acción (Ayllu Morado).
    
    TEXTO A PROCESAR: {texto_transcrito}
    
    ESTRUCTURA DE SALIDA:
    1. RESUMEN EJECUTIVO (Máximo 3 líneas)
    2. RIESGOS POLÍTICOS (Alertas para el portal)
    3. PROPUESTAS DE BIENESTAR (Para el mapa interactivo)
    4. SENTIMIENTO (Positivo/Neutral/Negativo)
    """
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    print("🧠 Cerebro V51 Activo. Listo para procesar transcripciones.")
