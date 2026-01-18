@echo off
title MOTOR V?A 51 - INTELIGENCIA ELECTORAL
cd /d C:\V51_PRODUCCION
echo [1/4] Clasificando documentos...
python v51_clasificador.py
echo [2/4] Verificando infraestructura y alertas...
python v51_alertas.py
echo [3/4] Procesando nuevos medios (si existen)...
:: Aqu? se llamar?a al transcriptor de ser necesario
echo [4/4] Actualizando Portal Patria Grande...
python ensamblar_v51.py
echo.
echo === VIGILANCIA V51 ACTIVA ===
pause
