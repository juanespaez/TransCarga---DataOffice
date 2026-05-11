# TransCarga S.A.S. - Data Office Strategy

## Optimización de Rutas de Entrega con ETL y VRP

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)]()

---

## 📋 Descripción

Este proyecto implementa una solución completa de optimización de rutas de entrega para **TransCarga S.A.S.**, una empresa logística colombiana con operaciones en Medellín y Cali. El proyecto incluye:

- **Pipeline ETL completo** para procesamiento de datos
- **Modelo de optimización CVRP** (Capacitated Vehicle Routing Problem)
- **Documentación técnica y de gobierno de datos**
- **Visualización de resultados**

### Problema Abordado

TransCarga S.A.S. enfrenta una deserción del **18% de clientes PYME** debido a:
- Falta de tracking digital
- Procesos manuales de despacho
- Competidores con mejor tecnología

### Solución Implementada

Sistema de optimización de rutas basado en datos abiertos de datos.gov.co que permite:
- Reducir costos operativos
- Mejorar tiempos de entrega
- Digitalizar la planificación logística

---

## 📊 Resultados

| Métrica | Valor |
|---------|-------|
| Clientes optimizados | 20 |
| Distancia total | 530 km |
| Vehículos utilizados | 5 |
| Carga total | 10,000 kg |
| Costo estimado | $1,239,878 COP |
| Tiempo de resolución | 60 segundos |

---

## 🗂️ Estructura del Repositorio

```
TransCarga_ETL/
├── 📁 notebooks/              # Jupyter notebooks del pipeline ETL
│   ├── 01_extraccion.ipynb    # Extracción de datos de APIs
│   ├── 02_transformacion.ipynb # Limpieza y transformación
│   ├── 03_carga.ipynb         # Generación de archivos para modelo
│   └── 04_optimizacion.ipynb  # Modelo CVRP con OR-Tools
│
├── 📁 datos/                  # Datos del proyecto
│   ├── 📁 raw/                # Datos originales (7 archivos)
│   ├── 📁 processed/          # Datos limpios y transformados
│   ├── 📁 output/             # Archivos de entrada al modelo
│   └── 📁 results/            # Resultados de optimización
│
├── 📁 documentacion/          # Documentación técnica
│   ├── gobierno_datos.md      # Marco de gobierno de datos
│   └── *.md                   # Otros documentos
│
├── 📁 logs/                   # Logs de ejecución
│
├── 📄 README.md               # Este archivo
├── 📄 requirements.txt        # Dependencias Python
├── 📄 .gitignore              # Archivos ignorados por Git
└── 📄 validar_notebooks.py    # Script de validación
```

---

## ⚙️ Instalación

### Prerrequisitos

- Python 3.10 o superior
- pip (gestor de paquetes)
- Jupyter Notebook o Jupyter Lab

### Pasos de Instalación

1. **Clonar el repositorio:**
```bash
git clone https://github.com/juanespaez/TransCarga---DataOffice.git
cd TransCarga---DataOffice
```

2. **Crear entorno virtual (recomendado):**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Instalar dependencias:**
```bash
pip install -r requirements.txt
```

---

## 🚀 Ejecución

### Ejecutar Pipeline ETL Completo

Los notebooks deben ejecutarse en orden:

```bash
jupyter notebook

# Abrir en orden:
# 1. notebooks/01_extraccion.ipynb
# 2. notebooks/02_transformacion.ipynb
# 3. notebooks/03_carga.ipynb
# 4. notebooks/04_optimizacion.ipynb
```

### Ejecutar desde Terminal

```bash
# Convertir notebooks a Python y ejecutar
jupyter nbconvert --to script notebooks/*.ipynb
python notebooks/01_extraccion.py
python notebooks/02_transformacion.py
python notebooks/03_carga.py
python notebooks/04_optimizacion.py
```

### Validar Notebooks

```bash
python validar_notebooks.py
```

---

## 📈 Pipeline ETL

### 01. Extracción

- **Fuente:** APIs de datos.gov.co
- **Datasets:**
  - DIVIPOLA (geolocalización de municipios)
  - Precios de combustible
  - Parque automotor
- **Salida:** Archivos CSV en `/datos/raw/`

### 02. Transformación

- **Procesos:**
  - Filtrado por departamentos (Antioquia, Valle del Cauca)
  - Validación de coordenadas
  - Normalización de formatos
  - Cálculo de matrices de distancia Haversine
- **Salida:** Archivos limpios en `/datos/processed/`

### 03. Carga

- **Procesos:**
  - Consolidación de datos
  - Generación de archivos de entrada al modelo
  - Configuración de parámetros CVRP
- **Salida:** Archivos optimización en `/datos/output/`

### 04. Optimización

- **Modelo:** CVRP con Google OR-Tools
- **Algoritmo:** GUIDED_LOCAL_SEARCH
- **Restricciones:**
  - Capacidad de vehículos
  - Múltiples vehículos
  - Retorno al depósito
- **Salida:** Rutas optimizadas en `/datos/results/`

---

## 📚 Fuentes de Datos

| Dataset | Fuente | URL |
|---------|--------|-----|
| DIVIPOLA Geolocalizado | datos.gov.co | https://www.datos.gov.co/resource/vafm-j2df.json |
| Precios Combustible | datos.gov.co | https://www.datos.gov.co/resource/x6id-4v3g.json |
| Parque Automotor Medellín | datos.gov.co | https://www.datos.gov.co/resource/3fqj-86mk.json |
| Terminales Transporte | datos.gov.co | https://www.datos.gov.co/resource/aesn-q83n.json |

---

## 🔧 Tecnologías

| Tecnología | Uso |
|------------|-----|
| Python 3.12 | Lenguaje principal |
| pandas | Manipulación de datos |
| numpy | Cálculos numéricos |
| requests | Peticiones HTTP |
| Google OR-Tools | Optimización VRP |
| matplotlib | Visualización |
| Jupyter | Notebooks interactivos |

---

## 📖 Documentación

### Gobierno de Datos

El documento completo de gobierno de datos se encuentra en:
`documentacion/gobierno_datos.md`

Incluye:
- Roles y responsabilidades (Data Owner, Data Steward, Data Custodian)
- Políticas de calidad de datos
- Catálogo de activos de datos
- Estándares y normativas
- Seguridad y privacidad
- Trazabilidad y linaje de datos


