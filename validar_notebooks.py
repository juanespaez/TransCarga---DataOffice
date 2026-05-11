"""
Script de Validacion de Notebooks ETL
Ejecuta los 3 notebooks y verifica que funcionen correctamente
"""

import subprocess
import os
import sys
import json
from datetime import datetime

# Directorio de notebooks
NOTEBOOKS_DIR = r'C:\Users\danie\OneDrive\Documentos\TransCarga_ETL\notebooks'
BASE_DIR = r'C:\Users\danie\OneDrive\Documentos\TransCarga_ETL'

def ejecutar_notebook(notebook_path):
    """
    Ejecuta un notebook y retorna el resultado
    """
    print(f"\n{'='*60}")
    print(f"Ejecutando: {os.path.basename(notebook_path)}")
    print('='*60)
    
    # Comando para ejecutar el notebook
    cmd = [
        sys.executable, '-m', 'jupyter', 'nbconvert', 
        '--to', 'notebook',
        '--execute',
        '--inplace',
        notebook_path
    ]
    
    try:
        result = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True, 
            timeout=300  # 5 minutos maximo
        )
        
        if result.returncode == 0:
            print(f"[OK] Notebook ejecutado exitosamente")
            return True, "Exitoso"
        else:
            print(f"[ERROR] Error en la ejecucion")
            if result.stdout:
                print(f"STDOUT: {result.stdout[:500]}")
            if result.stderr:
                print(f"STDERR: {result.stderr[:500]}")
            return False, result.stderr
            
    except subprocess.TimeoutExpired:
        print(f"[ERROR] Timeout - el notebook tardo mas de 5 minutos")
        return False, "Timeout"
    except Exception as e:
        print(f"[ERROR] Error: {str(e)}")
        return False, str(e)

def verificar_outputs():
    """
    Verifica que los archivos de output se hayan creado
    """
    print(f"\n{'='*60}")
    print("VERIFICANDO ARCHIVOS GENERADOS")
    print('='*60)
    
    output_dir = os.path.join(BASE_DIR, 'datos', 'output')
    raw_dir = os.path.join(BASE_DIR, 'datos', 'raw')
    processed_dir = os.path.join(BASE_DIR, 'datos', 'processed')
    
    archivos_esperados = {
        'raw': [
            'clientes_raw.csv',
            'vehiculos_raw.csv',
            'trafico_raw.csv',
            'peajes_raw.csv',
            'combustible_raw.csv',
            'divipola_raw.csv'
        ],
        'processed': [
            'clientes_clean.csv',
            'vehiculos_clean.csv',
            'trafico_clean.csv',
            'peajes_clean.csv',
            'combustible_clean.csv',
            'matriz_distancias.csv',
            'matriz_tiempos.csv'
        ],
        'output': [
            'optimizacion_clientes.csv',
            'optimizacion_vehiculos.csv',
            'optimizacion_bodegas.csv',
            'optimizacion_matriz_distancias.csv',
            'optimizacion_matriz_tiempos.csv',
            'config_modelo.json',
            'estadisticas_dataset.json',
            'reporte_validacion.csv'
        ]
    }
    
    resultados = {}
    
    for categoria, archivos in archivos_esperados.items():
        if categoria == 'raw':
            dir_path = raw_dir
        elif categoria == 'processed':
            dir_path = processed_dir
        else:
            dir_path = output_dir
        
        print(f"\n{categoria.upper()}:")
        for archivo in archivos:
            path = os.path.join(dir_path, archivo)
            if os.path.exists(path):
                size = os.path.getsize(path)
                print(f"  [OK] {archivo} ({size} bytes)")
                resultados[archivo] = True
            else:
                print(f"  [MISSING] {archivo} - NO ENCONTRADO")
                resultados[archivo] = False
    
    return resultados

def main():
    """
    Funcion principal de validacion
    """
    print("="*80)
    print("VALIDACION DE NOTEBOOKS ETL - TransCarga S.A.S.")
    print(f"Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)
    
    notebooks = [
        '01_extraccion.ipynb',
        '02_transformacion.ipynb',
        '03_carga.ipynb'
    ]
    
    resultados_ejecucion = {}
    
    # Ejecutar cada notebook
    for nb in notebooks:
        path = os.path.join(NOTEBOOKS_DIR, nb)
        if os.path.exists(path):
            success, msg = ejecutar_notebook(path)
            resultados_ejecucion[nb] = {'success': success, 'message': msg}
        else:
            print(f"[ERROR] Notebook no encontrado: {nb}")
            resultados_ejecucion[nb] = {'success': False, 'message': 'No encontrado'}
    
    # Verificar archivos generados
    archivos_result = verificar_outputs()
    
    # Resumen final
    print(f"\n{'='*80}")
    print("RESUMEN DE VALIDACION")
    print("="*80)
    
    print("\nEJECUCION DE NOTEBOOKS:")
    for nb, result in resultados_ejecucion.items():
        estado = "[OK]" if result['success'] else "[ERROR]"
        print(f"  {estado} {nb}")
    
    print("\nARCHIVOS GENERADOS:")
    total_ok = sum(1 for v in archivos_result.values() if v)
    total = len(archivos_result)
    print(f"  {total_ok}/{total} archivos creados correctamente")
    
    # Verificar si todo esta OK
    all_notebooks_ok = all(r['success'] for r in resultados_ejecucion.values())
    all_files_ok = all(archivos_result.values())
    
    if all_notebooks_ok and all_files_ok:
        print("\n[SUCCESS] VALIDACION EXITOSA - Los notebooks funcionan correctamente")
        return 0
    else:
        print("\n[WARNING] VALIDACION CON PROBLEMAS - Revisar los errores arriba")
        return 1

if __name__ == '__main__':
    sys.exit(main())
