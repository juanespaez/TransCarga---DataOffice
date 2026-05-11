# Dashboard TransCarga - Instrucciones de Uso

## Ejecución del Dashboard

### Opción 1: Desde terminal
```bash
cd C:\Users\danie\OneDrive\Documentos\TransCarga_ETL
streamlit run dashboard.py
```

### Opción 2: Desde Python
```python
import os
os.chdir(r'C:\Users\danie\OneDrive\Documentos\TransCarga_ETL')
os.system('streamlit run dashboard.py')
```

---

## Funcionalidades del Dashboard

### 1. Métricas Principales
- Vehículos activos
- Clientes atendidos
- Distancia total
- Carga entregada
- Costo total

### 2. Mapa Interactivo
- Visualización geográfica de rutas
- Marcadores por parada
- Líneas de ruta por vehículo
- Tooltips con información detallada

### 3. Análisis de Distribución
- Top 10 municipios con más clientes
- Histograma de demanda
- Scatter plot geográfico

### 4. Análisis por Vehículo
- Paradas por vehículo
- Carga entregada
- Tabla resumen
- Gráfico radar comparativo

### 5. Análisis de Costos
- Distribución combustible vs conductores
- Métricas de eficiencia
- Comparación antes/después

---

## Filtros Disponibles

- **Filtro de vehículos:** Seleccionar qué vehículos mostrar
- **Mostrar datos raw:** Ver datos originales en el sidebar

---

## Dependencias Requeridas

```
streamlit>=1.28.0
plotly>=5.18.0
folium>=0.15.0
streamlit-folium>=0.20.0
pandas>=2.0.0
numpy>=1.24.0
```

Instalar todas:
```bash
pip install -r requirements.txt
```

---

## Notas

- El dashboard se abre automáticamente en el navegador
- URL por defecto: http://localhost:8501
- Para detener: Ctrl+C en la terminal
- Los datos se cargan desde `/datos/results/` y `/datos/processed/`
