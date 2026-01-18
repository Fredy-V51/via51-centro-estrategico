import os
import whisper
import subprocess

def procesar_video_electoral(url, nivel, region):
    print(f"📥 Descargando audio de: {url}...")
    # Descargar solo audio para ahorrar banda y tiempo
    cmd = f'yt-dlp -x --audio-format mp3 -o "temp_audio.%(ext)s" {url}'
    subprocess.run(cmd, shell=True)

    print("🧠 Transcribiendo localmente (Whisper)...")
    model = whisper.load_model("base") # El modelo 'base' es rápido y gratuito
    result = model.transcribe("temp_audio.mp3")
    texto = result["text"]

    # Guardar en la carpeta correspondiente según el nivel de Fredy
    folder = f"C:/V51_PRODUCCION/COMPONENTES/REPORTES_MEDIOS.txt"
    with open(folder, "a", encoding="utf-8") as f:
        f.write(f"\n--- REPORTE DE MEDIOS ({nivel} - {region}) ---\n")
        f.write(f"URL: {url}\n")
        f.write(f"TRANSCRIPCIÓN: {texto}\n")
        f.write("-" * 30 + "\n")
    
    os.remove("temp_audio.mp3")
    print("✅ Transcripción completada y guardada en componentes.")

if __name__ == '__main__':
    # Probando con tu link de YouTube Shorts
    procesar_video_electoral("https://www.youtube.com/shorts/6xfIovfa0AM", "DIPUTADOS", "LIMA")
