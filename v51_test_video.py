from google import genai
import v51_config
import os

def analizar_final(url):
    print(f"🚀 [PASO DE VENCEDORES] Conexión directa al motor estable...")
    
    # Forzamos la configuración para evitar el error 404
    client = genai.Client(api_key=v51_config.API_KEY)
    
    prompt = f"Analiza el contenido de este video de YouTube y resume su importancia para la infraestructura ferroviaria: {url}"
    
    try:
        # Usamos la sintaxis simplificada que NO depende de la versión beta
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=prompt
        )
        
        print("\n--- 🏛️ ANALISIS ESTRATÉGICO RECUPERADO ---")
        print(response.text)
        
        # Guardar resultado para el portal
        os.makedirs("C:/V51_PRODUCCION/02_ENTRADA", exist_ok=True)
        with open("C:/V51_PRODUCCION/02_ENTRADA/V51_ANALISIS_VIDEO.txt", "w", encoding="utf-8") as f:
            f.write(response.text)
            
    except Exception as e:
        print(f"⚠️ Nota de Ingeniería: Si persiste el 404, el modelo debe llamarse sin el prefijo 'models/'. Reintentando...")
        try:
             # Segundo intento con ruta alternativa
             response = client.models.generate_content(model="gemini-1.5-flash", contents=prompt)
             print(response.text)
        except Exception as e2:
             print(f"❌ Error crítico: {e2}")

if __name__ == "__main__":
    url_video = "https://www.youtube.com/shorts/dRPcifNUI68"
    analizar_final(url_video)
