# TransCarga S.A.S. — Transformación Digital

> Estrategia corporativa y prototipo de optimización de rutas para una empresa logística mediana en Colombia.

**Universidad Pontificia Bolivariana** — Data Office Strategy, 2026

---

## Descripción del Proyecto

TransCarga S.A.S. es una empresa logística mediana simulada (250 empleados, COP $18.000M/año) con sede en Medellín que enfrenta una crisis de pérdida de clientes por falta de capacidades digitales. Este repositorio contiene:

1. **Estrategia corporativa** de transformación digital (análisis, frameworks, roadmap)
2. **Prototipo funcional** de optimización de rutas con datos reales colombianos
3. **Pipeline ETL** para ingesta, limpieza y procesamiento de datos
4. **Documentación técnica** del stack tecnológico y justificación de herramientas

---

## Arquitectura

### Producción (Target)

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Clientes   │    │  Conductores │    │  E-commerce  │
│  Portal Web  │    │   App Móvil  │    │     APIs     │
│   (React)    │    │(React Native)│    │              │
└──────┬───────┘    └──────┬───────┘    └──────┬───────┘
       │                   │                   │
       └───────────────────┼───────────────────┘
                           │
                    ┌──────▼───────┐
                    │   FastAPI    │
                    │   Backend    │
                    └──────┬───────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
       ┌──────▼──────┐ ┌──▼───┐ ┌─────▼──────┐
       │  Data Lake  │ │  n8n │ │ PostgreSQL │
       │  (S3/Azure) │ │      │ │ + PostGIS  │
       └──────┬──────┘ └──────┘ └────────────┘
              │
       ┌──────▼──────┐
       │ Databricks  │
       │ (Spark/SQL) │
       └──────┬──────┘
              │
       ┌──────▼──────┐
       │  Dashboards │
       │  Power BI   │
       └─────────────┘
```

### Prototipo (MVP — lo que estamos construyendo ahora)

```
┌─────────────────────────────────────────────────┐
│              Jupyter Notebooks                   │
│  01_extraccion → 02_transformacion → 03_carga   │
└──────────────────────┬──────────────────────────┘
                       │
          ┌────────────┼────────────┐
          │            │            │
   ┌──────▼──────┐ ┌──▼──────┐ ┌──▼──────────┐
   │ PostgreSQL  │ │  Redis  │ │  CSV/Parquet │
   │ + PostGIS   │ │  Cache  │ │  (processed) │
   └─────────────┘ └─────────┘ └──────────────┘
          │
   ┌──────▼──────┐
   │  OR-Tools   │
   │  (Python)   │
   │  Rutas VRP  │
   └─────────────┘
```

> **¿Por qué dos arquitecturas?** La arquitectura de producción (Data Lake + Databricks) está documentada y justificada en `docs/stack_tecnologico.docx`. El prototipo (PostgreSQL + Jupyter) valida el enfoque antes de invertir en infraestructura cloud. Esto es una práctica estándar: prototipar → validar → escalar.

---

## Estructura del Repositorio

```
transcarga-digital/
│
├── docs/                                  # Documentación del proyecto
│   ├── stack_tecnologico.docx             # Justificación de herramientas
│   ├── contexto_y_fuentes.md              # Datos de mercado y fuentes
│   ├── optimizacion_rutas.md              # Spec de optimización de rutas
│   ├── etl_specifications.md              # Spec del pipeline ETL
│   └── presentacion_estrategia.pptx       # Deck de estrategia corporativa
│
├── datos/                                 # Datos del proyecto
│   ├── raw/                               # Datos sin procesar
│   │   ├── clientes_raw.csv
│   │   ├── divipola_raw.csv
│   │   ├── trafico_raw.csv
│   │   ├── peajes_raw.csv
│   │   └── combustible_raw.csv
│   ├── processed/                         # Datos limpios
│   │   ├── clientes_limpios.csv
│   │   ├── trafico_limpio.csv
│   │   ├── peajes_limpios.csv
│   │   └── combustible_limpio.csv
│   └── external/                          # Datos externos (no versionados)
│       └── .gitkeep
│
├── notebooks/                             # Jupyter notebooks
│   ├── 01_extraccion.ipynb                # Extracción de datos
│   ├── 02_transformacion.ipynb            # Limpieza y transformación
│   └── 03_carga.ipynb                     # Carga a BD + cache
│
├── src/                                   # Código fuente
│   ├── limpieza.py                        # Scripts de limpieza de datos
│   ├── optimizacion.py                    # Algoritmo VRP con OR-Tools
│   ├── visualizacion.py                   # Mapas y gráficos (Folium)
│   └── api.py                             # API REST (FastAPI) — futuro
│
├── logs/                                  # Logs de ejecución
│   └── .gitkeep
│
├── tests/                                 # Tests
│   ├── test_limpieza.py
│   └── test_optimizacion.py
│
├── requirements.txt                       # Dependencias Python
├── .gitignore                             # Archivos excluidos
└── README.md                              # Este archivo
```

---

## Stack Tecnológico

| Capa | Herramienta | Justificación |
|------|-------------|---------------|
| Lenguaje | **Python** | Unifica backend + datos + IA en un solo lenguaje. Ecosistema enorme para ciencia de datos. |
| Backend API | **FastAPI** | Ligero, rápido, documentación Swagger automática. Mismo lenguaje que el stack de datos. |
| Data Lake (prod) | **AWS S3 / Azure ADLS** | Escalable, barato (~$50-100 USD/mes), acepta cualquier formato. |
| Procesamiento (prod) | **Databricks** | SQL + Python + ML en un solo lugar sin necesidad de DevOps. |
| BD (prototipo) | **PostgreSQL + PostGIS** | Datos geoespaciales nativos. Ideal para prototipo de rutas. |
| Cache | **Redis** | Acceso rápido a matrices de distancia/tiempo precalculadas. |
| Optimización | **Google OR-Tools** | Open source, escalable, bien documentado para VRP. |
| Geo/Mapas | **OSMnx + Folium** | Red vial real de Colombia + visualización interactiva. |
| Automatización | **n8n** | Open source, self-hosted, sin límite de ejecuciones, low-code. |
| Versionamiento | **GitHub** | Estándar de la industria. Integración nativa con Databricks. |
| Prototipado | **Google Colab** | Gratis, sin configuración, ideal para exploración rápida de datos. |
| Portal web (prod) | **React** | Ecosistema más grande, más desarrolladores disponibles. |
| App conductor (prod) | **React Native** | Mismo conocimiento que React, genera iOS + Android desde un código. |
| BI / Dashboards (prod) | **Databricks SQL + Power BI** | Integrado con el Data Lake. |

> Documento completo de justificación (por qué cada herramienta y no otras): `docs/stack_tecnologico.docx`

---

## Fuentes de Datos Reales

| Dataset | Fuente | Formato | Uso |
|---------|--------|---------|-----|
| Red vial Colombia | [OpenStreetMap / Geofabrik](https://download.geofabrik.de/south-america/colombia.html) | OSM/PBF | Grafo de rutas con distancias y tiempos |
| División política | [DIVIPOLA / IGAC](https://www.datos.gov.co/Mapas-Nacionales/DIVIPOLA-2024/gd9h-jp7n) | CSV | Geocodificación de direcciones |
| Tráfico Medellín | [Datos Abiertos Medellín](https://datosabiertos.medellin.gov.co/) | CSV/JSON | Ajuste de tiempos por congestión |
| Clima | [IDEAM](http://dhime.ideam.gov.co/web/) | CSV | Factor de impacto clima en rutas |
| Peajes | [INVIAS / Datos.gov.co](https://www.datos.gov.co/Transporte/Peales-Colombia/8d9c-7m7k) | CSV | Costos adicionales por ruta |
| Combustible | [MinMinas / Datos.gov.co](https://www.datos.gov.co/Minas-y-Energ-a/Precios-de-Combustibles/en5n-7zt5) | CSV | Costo de combustible por departamento |
| Mercado logístico | [Mordor Intelligence](https://www.mordorintelligence.com/industry-reports/colombia-freight-logistics-market-study) | Reporte | Contexto de mercado (USD $23.5B, 6.18% CAGR) |

---

## Cómo Ejecutar

### Requisitos previos

- Python 3.10+
- PostgreSQL 14+ con extensión PostGIS
- Redis (opcional, para cache)
- Git

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/[usuario]/transcarga-digital.git
cd transcarga-digital

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate   # Windows

# Instalar dependencias
pip install -r requirements.txt
```

### Ejecutar el pipeline ETL

```bash
# 1. Extracción de datos (~30-45 min)
jupyter notebook notebooks/01_extraccion.ipynb

# 2. Transformación y limpieza (~20-30 min)
jupyter notebook notebooks/02_transformacion.ipynb

# 3. Carga a PostgreSQL + Redis (~10-15 min)
jupyter notebook notebooks/03_carga.ipynb
```

### Ejecutar optimización de rutas

```bash
jupyter notebook notebooks/03_optimizacion.ipynb
```

---

## Métricas Objetivo

| Métrica | Actual | Objetivo | Mejora |
|---------|--------|----------|--------|
| Tiempo promedio por ruta | 6.5 horas | 5.2 horas | -20% |
| Distancia promedio por ruta | 120 km | 96 km | -20% |
| Entregas por día por vehículo | 18 | 24 | +33% |
| Costo por entrega | COP $8,500 | COP $7,480 | -12% |
| Consumo combustible/ruta | 15 galones | 12 galones | -20% |
| Deserción de clientes | 18% anual | <8% anual | -56% |
| Pedidos digitalizados | 0% | 80% | +80pp |

---

## Equipo

| Integrante | Rol | Responsabilidad |
|------------|-----|-----------------|
| Juanes | Líder del proyecto | Estrategia, stack tecnológico, repo, automatización (n8n), README |
| Daniel | Desarrollo técnico | ETL pipeline, optimización de rutas, código Python, specs técnicos |
| Santiago | Datos e investigación | Dataset de fuentes reales, investigación de mercado, documentación |

---

## Roadmap del Proyecto

```
Semana 1 (Entrega 1):  Estrategia corporativa + presentación BPMN
Semana 2 (Entrega 2):  Stack definido + prototipo ETL + repo público
Semana 3 (Final):      Modelo VRP funcionando + dashboards + presentación final
```

---

## Documentos de Soporte

| Documento | Descripción | Ubicación |
|-----------|-------------|-----------|
| Stack Tecnológico | Justificación de cada herramienta vs alternativas | `docs/stack_tecnologico.docx` |
| Contexto y Fuentes | Datos de mercado reales + perfil empresa simulada | `docs/contexto_y_fuentes.md` |
| Optimización de Rutas | Spec técnico del modelo VRP | `docs/optimizacion_rutas.md` |
| ETL Specifications | Pipeline de datos detallado | `docs/etl_specifications.md` |
| Presentación Estrategia | Deck de 10 slides con análisis Porter/Ansoff/BSC | `docs/presentacion_estrategia.pptx` |
| Matriz de Decisión | Excel con justificación de puntajes | `docs/matriz_decision.xlsx` |
| Guion de Exposición | Script para presentación oral | `docs/guion_exposicion.docx` |

---

## Licencia

Proyecto académico — Universidad Pontificia Bolivariana, 2026.

---

*TransCarga S.A.S. es una empresa simulada creada para este taller evaluativo. Todos los datos de mercado y fuentes son reales.*
