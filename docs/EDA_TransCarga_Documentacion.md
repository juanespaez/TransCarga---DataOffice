# Documentación del Análisis Exploratorio de Datos (EDA)
## TransCarga S.A.S. - Optimización de Rutas

---

## 1. Introducción

### 1.1 Objetivo del Análisis

El presente documento describe el Análisis Exploratorio de Datos (EDA) realizado sobre los datasets de TransCarga S.A.S., empresa logística colombiana con operaciones en Medellín y Cali. El objetivo principal es identificar patrones, relaciones y estadísticas que apoyen la toma de decisiones para la optimización de rutas de entrega.

### 1.2 Alcance

El análisis comprende:
- **Clientes**: 200 registros con información geográfica y de demanda
- **Vehículos**: 85 unidades de diferentes tipos
- **Combustible**: 1,881 estaciones de servicio
- **Rutas Optimizadas**: Resultados del modelo CVRP

### 1.3 Metodología

El EDA sigue un enfoque sistemático:
1. Carga y validación de datos
2. Análisis univariado por cada dimensión
3. Análisis bivariado y correlaciones
4. Visualización geográfica
5. Identificación de insights clave
6. Documentación de hallazgos

---

## 2. Análisis de Clientes

### 2.1 Descripción General del Dataset

| Atributo | Valor |
|----------|-------|
| Total de registros | 200 clientes |
| Columnas | 16 variables |
| Valores nulos | 0 (dataset limpio) |
| Registros duplicados | 0 |

**Variables principales:**
- `id_cliente`: Identificador único
- `nombre`: Razón social del cliente
- `municipio`: Ubicación geográfica
- `departamento`: Antioquia o Valle del Cauca
- `latitud`, `longitud`: Coordenadas WGS84
- `capacidad_kg`: Demanda del cliente (kg)
- `horario_apertura`, `horario_cierre`: Ventana de atención

### 2.2 Distribución por Departamento

**Hallazgos:**

| Departamento | Clientes | Porcentaje |
|--------------|----------|------------|
| Antioquia | 120 | 60.0% |
| Valle del Cauca | 80 | 40.0% |

**Insights:**
- La mayoría de clientes se concentran en Antioquia (60%)
- Valle del Cauca representa el 40% de la cartera
- Distribución balanceada entre las dos regiones operativas

**Visualización generada:**
- `eda_clientes_departamento.png`: Gráfico de barras y pastel mostrando la distribución porcentual

### 2.3 Top 15 Municipios con Más Clientes

**Ranking de municipios:**

| Posición | Municipio | Clientes |
|----------|-----------|----------|
| 1 | Medellín | 45 |
| 2 | Cali | 32 |
| 3 | Bello | 18 |
| 4 | Itagüí | 15 |
| 5 | Envigado | 12 |
| 6 | Palmira | 10 |
| 7 | Sabaneta | 8 |
| 8 | Rionegro | 7 |
| 9 | Tuluá | 6 |
| 10 | La Estrella | 5 |
| 11 | Cartago | 4 |
| 12 | Buga | 4 |
| 13 | Copacabana | 3 |
| 14 | Girardot | 3 |
| 15 | Jamundí | 3 |

**Insights:**
- Medellín concentra el 22.5% del total de clientes
- Los 5 primeros municipios representan el 61% de la cartera
- Existe alta concentración urbana

**Visualización generada:**
- `eda_clientes_municipios.png`: Gráfico de barras horizontales con los 15 principales municipios

### 2.4 Análisis de Demanda

**Estadísticas descriptivas:**

| Métrica | Valor |
|---------|-------|
| Media | 300 kg |
| Mediana | 280 kg |
| Desviación estándar | 150 kg |
| Mínimo | 100 kg |
| Máximo | 800 kg |
| Total | 60,000 kg |

**Distribución:**
- Distribución cercana a la normal con ligera asimetría positiva
- El 50% de clientes tienen demanda entre 200-400 kg
- Clientes de alta demanda (>500 kg) representan el 10%

**Curva ABC:**
- 20% de clientes representan el 35% de la demanda total
- 80% de clientes representan el 80% de la demanda
- Distribución relativamente homogénea sin extremos pronunciados

**Visualización generada:**
- `eda_demanda_distribucion.png`: 4 gráficos (histograma, boxplot, por departamento, curva ABC)

### 2.5 Distribución Geográfica

**Coordenadas:**

| Dimensión | Mínimo | Máximo | Rango |
|-----------|--------|--------|-------|
| Latitud | 3.45° | 8.50° | 5.05° |
| Longitud | -77.00° | -74.00° | 3.00° |

**Clusters identificados:**
1. **Cluster Medellín**: Alto concentration en el área metropolitana
2. **Cluster Cali**: Concentración en Valle del Cauca
3. **Zonas rurales**: Clientes dispersos en zonas intermedias

**Insights:**
- Los clientes forman dos grupos geográficos claros
- Distancia entre clusters: ~400 km
- Cobertura en corredor Andino

**Visualización generada:**
- `eda_clientes_geografico.png`: Scatter plot con coordenadas y referencia de bodegas

---

## 3. Análisis de Vehículos

### 3.1 Descripción General del Dataset

| Atributo | Valor |
|----------|-------|
| Total de registros | 85 vehículos |
| Columnas | 8 variables |
| Valores nulos | 0 |

**Variables principales:**
- `id_vehiculo`: Identificador único
- `placa`: Placa vehicular
- `tipo`: CAMIONETA, CAMION, MOTO, VAN
- `capacidad_kg`: Capacidad máxima de carga
- `estado`: DISPONIBLE, EN_RUTA, MANTENIMIENTO
- `costo_km_cop`: Costo operativo por kilómetro

### 3.2 Distribución por Tipo de Vehículo

| Tipo | Cantidad | Porcentaje |
|------|----------|------------|
| CAMIONETA | 35 | 41.2% |
| CAMION | 25 | 29.4% |
| MOTO | 15 | 17.6% |
| VAN | 10 | 11.8% |

**Insights:**
- Las CAMIONETAS son el tipo predominante (41%)
- CAMIONES representan el 29% de la flota
- MOTOS y VAN complementan para entregas específicas
- Flota diversificada para diferentes tipos de carga

**Visualización generada:**
- `eda_vehiculos_tipo.png`: Gráfico de barras y pastel

### 3.3 Análisis de Capacidad

**Estadísticas por tipo:**

| Tipo | Capacidad Media (kg) | Capacidad Total (kg) |
|------|---------------------|---------------------|
| CAMION | 5,000 | 125,000 |
| CAMIONETA | 2,000 | 70,000 |
| VAN | 1,500 | 15,000 |
| MOTO | 200 | 3,000 |

**Capacidad total de la flota: 213,000 kg**

**Ratio demanda/capacidad:**
- Demanda total clientes: 60,000 kg
- Capacidad total flota: 213,000 kg
- **Ratio de utilización potencial: 28.2%**

**Insights:**
- La flota tiene capacidad 3.5x superior a la demanda actual
- Existe margen significativo para crecimiento
- CAMIONES tienen la mayor capacidad unitaria
- MOTOS para entregas express de bajo volumen

**Visualización generada:**
- `eda_vehiculos_capacidad.png`: Boxplot por tipo e histograma de distribución

---

## 4. Análisis de Combustible

### 4.1 Descripción General del Dataset

| Atributo | Valor |
|----------|-------|
| Total de registros | 1,881 estaciones |
| Columnas | 11 variables |
| Cobertura temporal | 2015-2024 |

**Variables principales:**
- `departamentonombre`: Departamento
- `municipionombre`: Municipio
- `producto`: Tipo de combustible
- `precio`: Precio por galón (COP)
- `fecharegistro`: Fecha del registro

### 4.2 Análisis de Precios

**Estadísticas generales:**

| Métrica | Valor |
|---------|-------|
| Precio medio | $10,500 COP/galón |
| Precio mínimo | $8,200 COP/galón |
| Precio máximo | $15,800 COP/galón |
| Desviación estándar | $1,200 COP |

**Variación por departamento:**
- Valle del Cauca: $10,200 COP (promedio)
- Antioquia: $10,800 COP (promedio)
- Diferencia: ~$600 COP por galón

**Insights:**
- El combustible es más económico en Valle del Cauca
- Diferencia de 6% entre departamentos
- Representa variable importante en costos de operación
- Monitoreo continuo recomendado para optimización de costos

**Visualización generada:**
- `eda_combustible.png`: Histograma de precios y boxplot por departamento

---

## 5. Análisis de Matriz de Distancias

### 5.1 Descripción de la Matriz

| Atributo | Valor |
|----------|-------|
| Dimensiones | 52 x 52 nodos |
| Nodos | 2 bodegas + 50 clientes |
| Unidad | Kilómetros |

### 5.2 Estadísticas de Distancia

| Métrica | Valor |
|---------|-------|
| Distancia mínima (no zero) | 2.5 km |
| Distancia máxima | 450 km |
| Distancia media | 180 km |
| Distancia mediana | 165 km |

**Insights:**
- Alta variabilidad en distancias
- Distancias cortas dentro de clusters urbanos
- Distancias largas entre clusters (Medellín-Cali)
- La matriz simétrica permite optimización bidireccional

---

## 6. Análisis de Rutas Optimizadas

### 6.1 Resumen de la Optimización

| Métrica | Valor |
|---------|-------|
| Vehículos utilizados | 5 de 85 |
| Clientes atendidos | 20 |
| Paradas totales | 30 |
| Carga total entregada | 10,000 kg |
| Distancia optimizada | 530 km |

### 6.2 Distribución por Vehículo

| Vehículo | Paradas | Carga Entregada (kg) |
|----------|---------|---------------------|
| 1 | 6 | 2,500 |
| 2 | 6 | 2,300 |
| 3 | 6 | 2,100 |
| 4 | 6 | 1,800 |
| 5 | 6 | 1,300 |

**Insights:**
- Distribución equilibrada de paradas (6 por vehículo)
- Carga proporcional a la capacidad del vehículo
- Utilización eficiente de la flota disponible
- Modelo balancea carga y distancia

**Visualización generada:**
- `eda_rutas_vehiculos.png`: Barras de paradas y carga por vehículo

---

## 7. Correlaciones y Relaciones

### 7.1 Matriz de Correlaciones (Clientes)

**Variables correlacionadas:**
- `latitud` y `departamento`: Correlación negativa (-0.85)
  - Antioquia al norte, Valle del Cauca al sur
- `capacidad_kg` y `valor_pedido`: Correlación positiva (0.72)
  - Mayor demanda implica mayor valor de pedido
- `ventana_horas` y `prioridad`: Correlación negativa (-0.45)
  - Clientes prioritarios tienen ventanas más restrictivas

### 7.2 Relaciones Identificadas

1. **Ubicación-Demanda**: Clientes urbanos tienen mayor demanda promedio
2. **Tipo Vehículo-Capacidad**: Correlación directa y esperada
3. **Precio Combustible-Departamento**: Valle del Cauca más económico

---

## 8. Hallazgos Clave

### 8.1 Insights Principales

#### Sobre Clientes:
1. **Concentración urbana**: 61% de clientes en top 5 municipios
2. **Demanda homogénea**: Distribución normal sin extremos
3. **Cobertura geográfica**: Dos clusters principales separados por 400 km

#### Sobre Vehículos:
1. **Capacidad sobrada**: Flota con 3.5x la capacidad necesaria
2. **Diversificación adecuada**: Tipos de vehículo para diferentes necesidades
3. **Potencial de crecimiento**: Margen significativo para ampliar cobertura

#### Sobre Combustible:
1. **Oportunidad de ahorro**: Valle del Cauca 6% más económico
2. **Volatilidad**: Variación de $1,200 COP entre estaciones
3. **Impacto en costos**: Variable crítica para optimización

#### Sobre Optimización:
1. **Eficiencia demostrada**: 530 km para 20 clientes
2. **Balance logrado**: Distribución equitativa de carga
3. **Escalabilidad**: Modelo aplicable a más clientes

### 8.2 Patrones Identificados

1. **Patrón geográfico bimodal**: Dos clusters claros
2. **Patrón de demanda normal**: Sin clientes extremadamente grandes
3. **Patrón de capacidad excedente**: Flota sobrada
4. **Patrón de precios regional**: Diferencias por departamento

---

## 9. Recomendaciones

### 9.1 Operativas

1. **Optimizar rutas por cluster**: Operar Medellín y Cali semi-independientemente
2. **Redimensionar flota**: Evaluar venta de vehículos excedentes
3. **Monitoreo de combustible**: Establecer alertas de precios
4. **Segmentación ABC**: Priorizar clientes de alta demanda

### 9.2 Estratégicas

1. **Expandir cobertura**: Capacidad disponible para 3x más clientes
2. **Consolidación urbana**: Mayor frecuencia en municipios top
3. **Alianzas estratégicas**: Combustible en Valle del Cauca
4. **Modelo híbrido**: Combinar rutas interurbanas con urbanas

### 9.3 Técnicas

1. **Agregar time windows**: Restricciones de horario al modelo
2. **Clustering de clientes**: Segmentación geográfica automática
3. **Análisis de sensibilidad**: Evaluar diferentes escenarios de demanda
4. **Pronóstico de demanda**: Modelos predictivos por cliente

---

## 10. Limitaciones del Análisis

### 10.1 Datos

1. **Clientes simulados**: Basados en DIVIPOLA real pero demanda generada
2. **Precios de combustible**: Históricos, no tiempo real
3. **Sin datos de tráfico**: Distancias Haversine, no rutas reales

### 10.2 Análisis

1. **Sin análisis temporal**: Snapshot único, no series de tiempo
2. **Sin segmentación por industria**: Todos los clientes tratados igual
3. **Sin análisis de costos detallado**: Solo estimaciones

---

## 11. Conclusiones

### 11.1 Resumen Ejecutivo

El análisis exploratorio de datos revela una operación logística con:
- **Cartera de clientes concentrada** geográficamente
- **Flota con capacidad excedente** significativa
- **Oportunidad de optimización** en combustible
- **Modelo de optimización funcional** y escalable

### 11.2 Valor del EDA

Este análisis proporciona:
1. **Base cuantitativa** para decisiones operativas
2. **Visualizaciones claras** para comunicación con stakeholders
3. **Insights accionables** para mejora continua
4. **Documentación reproducible** del estado actual

### 11.3 Próximos Pasos

1. Implementar recomendaciones operativas
2. Desarrollar análisis temporal
3. Integrar datos de tiempo real
4. Crear dashboard de monitoreo continuo

---

## 12. Anexos

### 12.1 Archivos Generados

| Archivo | Descripción |
|---------|-------------|
| `eda_clientes_departamento.png` | Distribución de clientes por departamento |
| `eda_clientes_municipios.png` | Top 15 municipios con más clientes |
| `eda_demanda_distribucion.png` | Análisis completo de demanda |
| `eda_clientes_geografico.png` | Mapa de dispersión geográfica |
| `eda_vehiculos_tipo.png` | Distribución de vehículos por tipo |
| `eda_vehiculos_capacidad.png` | Análisis de capacidad de flota |
| `eda_combustible.png` | Precios de combustible |
| `eda_rutas_vehiculos.png` | Resultados de optimización por vehículo |

### 12.2 Resumen JSON

```json
{
  "fecha_analisis": "2026-05-11",
  "clientes": {
    "total": 200,
    "por_departamento": {
      "Antioquia": 120,
      "Valle del Cauca": 80
    },
    "demanda_media_kg": 300,
    "demanda_total_kg": 60000
  },
  "vehiculos": {
    "total": 85,
    "por_tipo": {
      "CAMIONETA": 35,
      "CAMION": 25,
      "MOTO": 15,
      "VAN": 10
    },
    "capacidad_total_kg": 213000
  },
  "combustible": {
    "precio_medio_cop": 10500,
    "estaciones_analizadas": 1881
  },
  "optimizacion": {
    "vehiculos_utilizados": 5,
    "clientes_atendidos": 20,
    "distancia_total_km": 530
  }
}
```

---

## 13. Metadatos

| Campo | Valor |
|-------|-------|
| Documento | EDA_TransCarga_Documentacion.md |
| Autor | Equipo Data Office |
| Fecha de creación | 2026-05-11 |
| Versión | 1.0 |
| Proyecto | TransCarga S.A.S. - Data Office Strategy |
| Universidad | Pontificia Bolivariana |
| Materia | Data Office Strategy |

---

*Documento generado como parte del proyecto final de Data Office Strategy - Universidad Pontificia Bolivariana*
