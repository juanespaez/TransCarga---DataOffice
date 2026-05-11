# Análisis de Brechas - TransCarga vs Rúbrica UPB

## Fecha: 2026-05-11

---

## 1. ESTRUCTURA DE CARPETAS

### Requerido por Rúbrica:
```
/proyecto/
├── /notebooks/          ← limpieza, EDA, visualización
├── /documentacion/      ← estrategia, procesos, arquitectura, gobernanza
├── README.md            ← resumen y cómo ejecutar
└── /img/ o /dashboard/  ← visualizaciones o reportes
```

### Estado Actual del Repositorio:
```
/TransCarga_ETL/
├── /notebooks/          ✅ EXISTE (4 notebooks)
├── /docs/               ⚠️ NOMBRE INCORRECTO (debe ser /documentacion/)
├── README.md            ❌ NO EXISTE
└── /img/ o /dashboard/  ❌ NO EXISTE
```

**ACCIONES REQUERIDAS:**
- [ ] Crear README.md completo
- [ ] Renombrar /docs/ a /documentacion/
- [ ] Crear carpeta /img/ o /dashboard/

---

## 2. ANÁLISIS POR CRITERIO DE RÚBRICA

### Criterio 1: Problema y Estrategia (10%)
**Estado:** ✅ CUBIERTO

**Evidencia:**
- Documentos de estrategia: `TransCarga_DataOffice_Strategy.pdf`
- Definición del problema: 18% deserción de clientes
- Análisis estratégico: Competidores (Coordinadora, Inter Rapidísimo)
- Conexión con entorno digital: Falta de tracking, procesos manuales

---

### Criterio 2: Procesos y Automatización (10%)
**Estado:** ✅ CUBIERTO

**Evidencia:**
- Diagramas BPMN AS-IS y TO-BE en `TransCarga_DataOffice_BPMN.pdf`
- Procesos modelados: Despacho, Tracking, Inventario
- Automatización propuesta: ETL Pipeline, Optimización automática de rutas

---

### Criterio 3: Arquitectura de Datos (15%)
**Estado:** ✅ CUBIERTO

**Evidencia:**
- Documentación técnica: `TransCarga_ETL_Documentacion.pdf`
- Arquitectura ETL definida: Extracción → Transformación → Carga → Optimización
- Herramientas especificadas: Python, pandas, OR-Tools, datos.gov.co APIs
- Flujo de datos documentado con diagramas

---

### Criterio 4: Limpieza y Normalización (10%)
**Estado:** ✅ CUBIERTO

**Evidencia:**
- Notebook `02_transformacion.ipynb`:
  - Limpieza de DIVIPOLA (filtrar departamentos, validar coordenadas)
  - Limpieza de combustible (convertir precios, filtrar regiones)
  - Normalización de clientes (coordenadas, horarios a minutos)
  - Cálculo de matrices de distancia/tiempo
- Código documentado y reproducible
- Datos limpios en `/datos/processed/`

---

### Criterio 5: Análisis Exploratorio EDA (10%)
**Estado:** ⚠️ PARCIALMENTE CUBIERTO

**Lo que existe:**
- Notebooks con `describe()`, `value_counts()`
- Visualización de rutas optimizadas (`rutas_optimizadas.png`)
- Métricas de optimización

**Lo que FALTA:**
- EDA dedicado con visualizaciones de:
  - Distribución de clientes por municipio
  - Histograma de demandas
  - Scatter plots de ubicaciones
  - Análisis de precios de combustible por región
  - Estadísticas del parque automotor
- Notebook específico para EDA o sección clara en notebook existente

---

### Criterio 6: Gobierno de Datos (20%) ⚠️ CRÍTICO
**Estado:** ❌ NO CUBIERTO

**Lo que EXIGE la rúbrica:**
- Definición de roles y responsables
- Políticas de datos
- Estándares de calidad
- Catálogo de datos
- Seguridad y privacidad
- Trazabilidad

**Lo que FALTA:**
- [ ] Documento de gobernanza de datos
- [ ] Definición de roles: Data Steward, Data Owner, Data Custodian
- [ ] Políticas de calidad de datos
- [ ] Catálogo de activos de datos
- [ ] Lineamientos de seguridad
- [ ] Reglas de retención y archival

**Este criterio vale 20% - ES EL MÁS IMPORTANTE**

---

### Criterio 7: Visualización Final (10%)
**Estado:** ⚠️ PARCIALMENTE CUBIERTO

**Lo que existe:**
- Visualización de rutas optimizadas (`rutas_optimizadas.png`)
- Gráficos en notebooks

**Lo que FALTA:**
- Dashboard interactivo para toma de decisiones
- La rúbrica especifica: "Dashboard atractivo y útil con conexión a los objetivos"
- Opciones recomendadas:
  - Power BI (conectado a CSV)
  - Streamlit dashboard
  - Jupyter dashboard con ipywidgets
  - Plotly Dash

---

### Criterio 8: Trabajo Colaborativo GitHub (15%)
**Estado:** ⚠️ PARCIALMENTE CUBIERTO

**Lo que existe:**
- Repositorio en GitHub
- Notebooks funcionales
- Estructura de carpetas

**Lo que FALTA:**
- README.md completo con:
  - Resumen del proyecto
  - Instrucciones de instalación
  - Cómo ejecutar los notebooks
  - Dependencias (requirements.txt)
  - Estructura del repositorio
  - Autores/colaboradores
- Evidencia de trabajo en equipo (commits distribuidos)
- Archivo .gitignore apropiado
- Licencia

---

## 3. RESUMEN DE FALTANTES CRÍTICOS

| Prioridad | Faltante | Criterio | Impacto |
|-----------|----------|----------|---------|
| 🔴 CRÍTICO | Gobierno de datos | 20% | Perdió 20% de nota |
| 🔴 CRÍTICO | README.md | 15% | Repositorio incompleto |
| 🟠 ALTO | Dashboard interactivo | 10% | Visualización insuficiente |
| 🟠 ALTO | Carpeta /documentacion/ | Entregable | Estructura incorrecta |
| 🟠 ALTO | Carpeta /img/ o /dashboard/ | Entregable | Estructura incorrecta |
| 🟡 MEDIO | EDA dedicado | 10% | Análisis superficial |

---

## 4. ACCIONES INMEDIATAS RECOMENDADAS

### Prioridad 1 - CRÍTICO (Antes de entrega final):

1. **Crear documento de Gobierno de Datos**
   - Archivo: `/documentacion/gobierno_datos.md`
   - Incluir: Roles, políticas, estándares, catálogo, seguridad

2. **Crear README.md**
   - Ubicación: Raíz del repositorio
   - Contenido mínimo:
     ```markdown
     # TransCarga S.A.S. - Data Office Strategy
     
     ## Descripción
     Proyecto de optimización de rutas de entrega...
     
     ## Estructura
     - /notebooks/ - Pipeline ETL
     - /documentacion/ - Documentos técnicos
     - /img/ - Visualizaciones
     
     ## Instalación
     pip install -r requirements.txt
     
     ## Ejecución
     jupyter notebook notebooks/01_extraccion.ipynb
     
     ## Autores
     - Nombre 1
     - Nombre 2
     - Nombre 3
     ```

3. **Renombrar carpeta /docs/ a /documentacion/**

4. **Crear carpeta /img/ y mover visualizaciones**

### Prioridad 2 - ALTA:

5. **Crear Dashboard o visualización interactiva**
   - Opción rápida: Streamlit app con 3-4 gráficos
   - Opción media: Jupyter notebook con ipywidgets
   - Opción completa: Plotly Dash o Power BI

6. **Agregar EDA dedicado**
   - Crear notebook `05_eda.ipynb` o
   - Ampliar notebook 02 con más visualizaciones

### Prioridad 3 - RECOMENDADO:

7. **Crear requirements.txt**
   ```
   pandas>=2.0.0
   numpy>=1.24.0
   requests>=2.31.0
   ortools>=9.8.0
   matplotlib>=3.7.0
   jupyter>=1.0.0
   ```

8. **Agregar .gitignore**
   ```
   __pycache__/
   .ipynb_checkpoints/
   *.pyc
   .env
   ```

9. **Documentar commits con mensajes descriptivos**

---

## 5. ESTIMACIÓN DE NOTA ACTUAL

| Criterio | Peso | Estado | Nota Estimada |
|----------|------|--------|---------------|
| 1. Problema y estrategia | 10% | ✅ Completo | 10/10 |
| 2. Procesos y automatización | 10% | ✅ Completo | 10/10 |
| 3. Arquitectura de datos | 15% | ✅ Completo | 15/15 |
| 4. Limpieza y normalización | 10% | ✅ Completo | 10/10 |
| 5. EDA | 10% | ⚠️ Parcial | 6/10 |
| 6. Gobierno de datos | 20% | ❌ Faltante | 0/20 |
| 7. Visualización final | 10% | ⚠️ Parcial | 5/10 |
| 8. Trabajo colaborativo | 15% | ⚠️ Parcial | 8/15 |
| **TOTAL** | **100%** | | **54/100** |

---

## 6. ESTIMACIÓN CON CORRECCIONES

Si se completan las acciones de Prioridad 1:

| Criterio | Peso | Estado | Nota Estimada |
|----------|------|--------|---------------|
| 1. Problema y estrategia | 10% | ✅ Completo | 10/10 |
| 2. Procesos y automatización | 10% | ✅ Completo | 10/10 |
| 3. Arquitectura de datos | 15% | ✅ Completo | 15/15 |
| 4. Limpieza y normalización | 10% | ✅ Completo | 10/10 |
| 5. EDA | 10% | ✅ Completo | 9/10 |
| 6. Gobierno de datos | 20% | ✅ Completo | 18/20 |
| 7. Visualización final | 10% | ✅ Completo | 9/10 |
| 8. Trabajo colaborativo | 15% | ✅ Completo | 14/15 |
| **TOTAL** | **100%** | | **85/100** |

---

## 7. CONCLUSIÓN

El proyecto tiene un **excelente trabajo técnico** en:
- Pipeline ETL funcional
- Modelo de optimización VRP
- Documentación de estrategia y procesos

Pero tiene **faltancias críticas** en:
- Gobierno de datos (20% de la nota)
- README.md (obligatorio)
- Estructura de carpetas según rúbrica

**Recomendación:** Completar los faltantes de Prioridad 1 antes de la entrega final del 20 de mayo para alcanzar una nota estimada de 85/100.
