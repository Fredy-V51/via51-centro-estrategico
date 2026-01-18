import os

# Diccionarios de control doctrinario
REGLAS = {
    "ESLOGAN_RIVAL": ["POTENCIA MUNDIAL"], # Bloqueo inmediato
    "CONCEPTOS_CLAVE": ["PATRIA GRANDE", "VÍA 51", "CALIDAD MUNDIAL"],
    "TEMAS_CRITICOS": ["CORRUPCIÓN", "INSEGURIDAD", "REGIONES"]
}

def analizar_alerta(texto, candidato, nivel):
    texto_up = texto.upper()
    alertas_encontradas = []
    
    # 1. Detectar infiltración del eslogan rival
    for prohibida in REGLAS["ESLOGAN_RIVAL"]:
        if prohibida in texto_up:
            alertas_encontradas.append(f"🔴 CRÍTICO: Uso de eslogan rival '{prohibida}'")

    # 2. Verificar cumplimiento de Patria Grande
    cumple_doctrina = any(clv in texto_up for clv in REGLAS["CONCEPTOS_CLAVE"])
    if not cumple_doctrina:
        alertas_encontradas.append("🟡 ADVERTENCIA: No se mencionó la Doctrina Patria Grande")

    # 3. Registrar resultados
    log_path = "C:/V51_PRODUCCION/COMPONENTES/ALERTAS_CAMPAÑA.txt"
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(f"\n[ALERTA] Candidato: {candidato} ({nivel})\n")
        if alertas_encontradas:
            for a in alertas_encontradas:
                f.write(f"- {a}\n")
        else:
            f.write("- ✅ Discurso Alineado.\n")
    
    return alertas_encontradas

if __name__ == '__main__':
    # Simulación de prueba con un texto extraído
    print("🚀 Probando Monitor de Alertas...")
    analizar_alerta("Queremos que el Perú sea una potencia mundial.", "Candidato_Prueba", "DIPUTADO")
