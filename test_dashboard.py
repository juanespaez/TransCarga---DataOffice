"""
Test del Dashboard - Verifica que los datos carguen correctamente
"""

import pandas as pd
import json
import os
from math import radians, sin, cos, sqrt, atan2

base_path = r'C:\Users\danie\OneDrive\Documentos\TransCarga_ETL\datos'

print("=" * 60)
print("VERIFICACION DE DATOS PARA DASHBOARD")
print("=" * 60)

# 1. Verificar rutas
print("\n[1] Cargando rutas optimizadas...")
rutas_path = os.path.join(base_path, 'results', 'rutas_optimizadas.csv')
if os.path.exists(rutas_path):
    rutas = pd.read_csv(rutas_path)
    print(f"    OK: {len(rutas)} registros encontrados")
    print(f"    OK: Columnas: {rutas.columns.tolist()}")
    
    # Normalizar
    rutas = rutas.rename(columns={'orden': 'parada_num', 'demanda': 'carga_kg'})
    rutas['tipo'] = rutas['carga_kg'].apply(lambda x: 'bodega' if x == 0 else 'cliente')
    
    # Calcular distancias
    def haversine(lat1, lon1, lat2, lon2):
        R = 6371
        lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        return R * 2 * atan2(sqrt(a), sqrt(1-a))
    
    distancias = []
    for vehiculo in rutas['vehiculo_id'].unique():
        vehiculo_data = rutas[rutas['vehiculo_id'] == vehiculo].sort_values('parada_num')
        dist_acum = 0
        prev_lat, prev_lon = None, None
        for idx, row in vehiculo_data.iterrows():
            if prev_lat is not None:
                dist = haversine(prev_lat, prev_lon, row['latitud'], row['longitud'])
                dist_acum += dist
            distancias.append(dist_acum)
            prev_lat, prev_lon = row['latitud'], row['longitud']
    
    rutas['distancia_km'] = distancias
    rutas['tiempo_min'] = rutas['distancia_km'] * 1.5
    
    print(f"    OK: Distancia total: {rutas['distancia_km'].max():.1f} km")
    print(f"    OK: Vehiculos unicos: {rutas['vehiculo_id'].nunique()}")
    print(f"    OK: Carga total: {rutas['carga_kg'].sum():,.0f} kg")
    
else:
    print("    ERROR: Archivo no encontrado")

# 2. Verificar métricas
print("\n[2] Cargando metricas...")
metricas_path = os.path.join(base_path, 'results', 'metricas_optimizacion.json')
if os.path.exists(metricas_path):
    with open(metricas_path, 'r', encoding='utf-8') as f:
        metricas = json.load(f)
    print(f"    OK: Metricas cargadas: {list(metricas.keys())}")
    for key, value in metricas.items():
        print(f"      - {key}: {value}")
else:
    print("    ERROR: Archivo no encontrado")

# 3. Verificar clientes
print("\n[3] Cargando clientes...")
clientes_path = os.path.join(base_path, 'processed', 'clientes_clean.csv')
if os.path.exists(clientes_path):
    clientes = pd.read_csv(clientes_path)
    print(f"    OK: {len(clientes)} clientes encontrados")
    print(f"    OK: Columnas: {clientes.columns.tolist()[:5]}...")
else:
    print("    ERROR: Archivo no encontrado")

# 4. Verificar vehículos
print("\n[4] Cargando vehiculos...")
vehiculos_path = os.path.join(base_path, 'processed', 'vehiculos_clean.csv')
if os.path.exists(vehiculos_path):
    vehiculos = pd.read_csv(vehiculos_path)
    print(f"    OK: {len(vehiculos)} vehiculos encontrados")
else:
    print("    ERROR: Archivo no encontrado")

print("\n" + "=" * 60)
print("VERIFICACION COMPLETADA - Dashboard listo para ejecutar")
print("=" * 60)
print("\nPara ejecutar el dashboard:")
print("  cd C:\\Users\\danie\\OneDrive\\Documentos\\TransCarga_ETL")
print("  streamlit run dashboard.py")
