"""
Test de Modelo de Optimizacion VRP
"""
import os
import pandas as pd
import numpy as np
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Cargar datos
BASE_DIR = r'C:\Users\danie\OneDrive\Documentos\TransCarga_ETL'
OUTPUT_DIR = os.path.join(BASE_DIR, 'datos', 'output')

clientes = pd.read_csv(os.path.join(OUTPUT_DIR, 'optimizacion_clientes.csv'))
vehiculos = pd.read_csv(os.path.join(OUTPUT_DIR, 'optimizacion_vehiculos.csv'))
bodegas = pd.read_csv(os.path.join(OUTPUT_DIR, 'optimizacion_bodegas.csv'))
matriz_distancias = pd.read_csv(os.path.join(OUTPUT_DIR, 'optimizacion_matriz_distancias.csv'), index_col=0)

print(f"Clientes: {len(clientes)}")
print(f"Vehiculos: {len(vehiculos)}")
print(f"Bodegas: {len(bodegas)}")
print(f"Matriz: {matriz_distancias.shape}")

# Seleccionar clientes (max 10 para prueba)
# Filtrar clientes con demanda pequena
clientes_small = clientes[clientes['capacidad_kg'] <= 500].head(10)
n_clientes = len(clientes_small)
clientes_sample = clientes_small.copy()

# Crear locations
locations = []

# Bodega
bodega = bodegas.iloc[0]
locations.append({
    'id': bodega['id_bodega'],
    'lat': bodega['latitud'],
    'lon': bodega['longitud'],
    'demanda': 0
})

# Clientes
for idx, row in clientes_sample.iterrows():
    locations.append({
        'id': row['id_cliente'],
        'lat': row['latitud'],
        'lon': row['longitud'],
        'demanda': row['capacidad_kg']
    })

print(f"\nLocations: {len(locations)}")

# Calcular matriz de distancias
from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    R = 6371
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

n = len(locations)
distance_matrix = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(0)
        else:
            d = haversine(locations[i]['lat'], locations[i]['lon'],
                         locations[j]['lat'], locations[j]['lon'])
            row.append(int(d * 1000))  # metros
    distance_matrix.append(row)

print(f"Matriz de distancias: {n}x{n}")

# Demands y vehicle capacities
demands = [loc['demanda'] for loc in locations]
print(f"Demanda total: {sum(demands)} kg")

n_vehiculos = 5
# Seleccionar vehiculos con mayor capacidad
vehiculos_sorted = vehiculos.sort_values('capacidad_kg', ascending=False)
vehicle_capacities = [int(vehiculos_sorted.iloc[i]['capacidad_kg']) for i in range(n_vehiculos)]
print(f"Capacidad total: {sum(vehicle_capacities)} kg")
print(f"Capacidades: {vehicle_capacities}")

# Crear modelo
manager = pywrapcp.RoutingIndexManager(n, n_vehiculos, 0)
routing = pywrapcp.RoutingModel(manager)

# Distance callback
def distance_callback(from_index, to_index):
    from_node = manager.IndexToNode(from_index)
    to_node = manager.IndexToNode(to_index)
    return distance_matrix[from_node][to_node]

transit_callback_index = routing.RegisterTransitCallback(distance_callback)
routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

# Capacity constraint
def demand_callback(from_index):
    from_node = manager.IndexToNode(from_index)
    return demands[from_node]

demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
routing.AddDimensionWithVehicleCapacity(
    demand_callback_index,
    0,
    vehicle_capacities,
    True,
    'Capacity'
)

# Search parameters
search_parameters = pywrapcp.DefaultRoutingSearchParameters()
search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
search_parameters.local_search_metaheuristic = routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
search_parameters.time_limit.seconds = 30

print("\nResolviendo...")
solution = routing.SolveWithParameters(search_parameters)

if solution:
    print("\n[OK] Solucion encontrada!")
    
    total_distance = 0
    for vehicle_id in range(n_vehiculos):
        index = routing.Start(vehicle_id)
        route = []
        route_distance = 0
        
        print(f"\n--- Vehiculo {vehicle_id + 1} ---")
        
        while not routing.IsEnd(index):
            node = manager.IndexToNode(index)
            route.append(node)
            print(f"  {node}: {locations[node]['id']} ({locations[node]['demanda']} kg)")
            
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        
        node = manager.IndexToNode(index)
        route.append(node)
        print(f"  {node}: DEPOT (fin)")
        
        total_distance += route_distance
        print(f"  Distancia: {route_distance/1000:.1f} km")
        print(f"  Paradas: {len(route) - 2}")
    
    print(f"\nDistancia total: {total_distance/1000:.1f} km")
else:
    print("\n[ERROR] No se encontro solucion")
    print("Posibles causas:")
    print("  - Capacidad insuficiente")
    print("  - Restricciones muy estrictas")
    print("  - Time limit demasiado corto")
