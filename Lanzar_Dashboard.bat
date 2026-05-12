@echo off
title Lanzador de Dashboard TransCarga S.A.S.
echo =======================================================
echo    BIENVENIDO AL DASHBOARD DE TRANSCARGA S.A.S.
echo =======================================================
echo.
echo [1/3] Verificando dependencias...
pip install -r requirements.txt --quiet
echo [OK] Dependencias listas.
echo.
echo [2/3] Iniciando servidor de Streamlit...
echo.
echo -------------------------------------------------------
echo El dashboard se abrira automaticamente en tu navegador.
echo No cierres esta ventana mientras uses la aplicacion.
echo -------------------------------------------------------
echo.
streamlit run dashboard.py
pause