# Gobierno de Datos - TransCarga S.A.S.

## Data Governance Framework

---

## 1. Introducción y Contexto

### 1.1 Propósito
Este documento establece el marco de gobierno de datos para TransCarga S.A.S., definiendo los roles, políticas, estándares y procesos necesarios para garantizar que los datos sean un activo estratégico confiable, seguro y accesible para la toma de decisiones empresariales.

### 1.2 Alcance
El marco de gobierno de datos aplica a todos los conjuntos de datos utilizados en las operaciones de TransCarga S.A.S., incluyendo:
- Datos de clientes y deliveries
- Datos de vehículos y flota
- Datos geográficos y de rutas
- Datos financieros y operacionales
- Datos de proveedores externos (datos.gov.co)

### 1.3 Objetivos del Gobierno de Datos
1. **Calidad**: Garantizar precisión, completitud y consistencia de los datos
2. **Seguridad**: Proteger la confidencialidad e integridad de los datos
3. **Accesibilidad**: Facilitar el acceso oquesto a datos confiables
4. **Trazabilidad**: Documentar el origen y transformaciones de los datos
5. **Cumplimiento**: Asegurar adherencia a regulaciones colombianas (Ley 1581 de 2012)

---

## 2. Organización y Roles

### 2.1 Estructura de Gobierno de Datos

```
                    ┌─────────────────────┐
                    │ Comité de Datos     │
                    │ (Data Governance    │
                    │  Council)           │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
┌───────▼───────┐      ┌───────▼───────┐      ┌───────▼───────┐
│ Data Owner    │      │ Data Steward  │      │ Data Custodian│
│ (Propietario) │      │ (Administrador│      │ (Custodio)    │
└───────────────┘      └───────────────┘      └───────────────┘
        │                      │                      │
        │                      │                      │
┌───────▼───────┐      ┌───────▼───────┐      ┌───────▼───────┐
│ Gerentes de   │      │ Analistas de  │      │ Equipo TI     │
│ Área          │      │ Datos         │      │               │
└───────────────┘      └───────────────┘      └───────────────┘
```

### 2.2 Definición de Roles

#### 2.2.1 Comité de Datos (Data Governance Council)

| Aspecto | Descripción |
|---------|-------------|
| **Responsable** | Gerencia General + Gerentes de Área |
| **Frecuencia de reunión** | Mensual |
| **Autoridad** | Toma de decisiones estratégicas sobre datos |
| **Responsabilidades** | - Definir políticas de gobierno de datos<br>- Aprobar estándares y normativas<br>- Resolver conflictos de datos<br>- Priorizar iniciativas de datos<br>- Asignar recursos |

**Miembros del Comité:**
- Gerente General (Presidente)
- Gerente de Operaciones
- Gerente Comercial
- Gerente Financiero
- Director de Tecnología
- Data Steward Principal

---

#### 2.2.2 Data Owner (Propietario de Datos)

| Aspecto | Descripción |
|---------|-------------|
| **Definición** | Responsable del negocio por un dominio de datos específico |
| **Autoridad** | Toma decisiones sobre el uso y acceso a sus datos |
| **Accountability** | Responde ante el Comité de Datos |

**Data Owners por Dominio:**

| Dominio | Data Owner | Área |
|---------|------------|------|
| Clientes y Deliveries | Gerente Comercial | Comercial |
| Vehículos y Flota | Gerente de Operaciones | Operaciones |
| Rutas y Geolocalización | Coordinador de Logística | Logística |
| Finanzas y Costos | Gerente Financiero | Finanzas |
| Recursos Humanos | Gerente de Talento | RRHH |

**Responsabilidades del Data Owner:**
1. Definir requisitos de calidad para su dominio
2. Autorizar acceso a datos sensibles
3. Validar definiciones de negocio
4. Aprobar cambios en la estructura de datos
5. Gestionar issues de calidad de datos

---

#### 2.2.3 Data Steward (Administrador de Datos)

| Aspecto | Descripción |
|---------|-------------|
| **Definición** | Responsable operativo de la calidad y metadata |
| **Reporta a** | Data Owner del dominio |
| **Tipo** | Rol dedicado (no compartido) |

**Data Stewards Asignados:**

| Dominio | Data Steward | Dedicación |
|---------|--------------|------------|
| Operaciones | Analista de Datos Senior | 50% |
| Comercial | Analista de Business Intel. | 40% |
| Logística | Coordinador de Rutas | 30% |

**Responsabilidades del Data Steward:**
1. Monitorear calidad de datos con dashboards
2. Documentar definiciones y metadata
3. Ejecutar validaciones y limpieza de datos
4. Gestionar catálogo de activos de datos
5. Reportar métricas de calidad al Comité
6. Capacitar usuarios en uso de datos
7. Identificar y documentar issues de calidad
8. Coordinar con Data Custodians

---

#### 2.2.4 Data Custodian (Custodio de Datos)

| Aspecto | Descripción |
|---------|-------------|
| **Definición** | Responsable técnico del almacenamiento y seguridad |
| **Reporta a** | Director de Tecnología |
| **Equipo** | Área de TI |

**Responsabilidades del Data Custodian:**
1. Administrar infraestructura de datos
2. Implementar controles de seguridad
3. Gestionar backups y recuperación
4. Mantener ambientes de datos (prod, dev, test)
5. Implementar controles de acceso técnico
6. Monitorear performance de bases de datos
7. Ejecutar archivado y purga de datos

---

#### 2.2.5 Data User (Usuario de Datos)

| Aspecto | Descripción |
|---------|-------------|
| **Definición** | Persona que consume datos para su trabajo |
| **Obligaciones** | Usar datos según políticas definidas |

**Tipos de Usuarios:**

| Tipo | Perfil | Acceso |
|------|--------|--------|
| Ejecutivo | Gerentes, Directivos | Dashboards, Reportes agregados |
| Analista | Analistas, Planificadores | Datos detallados, herramientas analíticas |
| Operativo | Conductores, Despachadores | Datos operacionales en tiempo real |
| Externo | Clientes, Proveedores | Portal de clientes, APIs limitadas |

---

## 3. Políticas de Calidad de Datos

### 3.1 Dimensiones de Calidad

| Dimensión | Definición | Métrica | Objetivo |
|-----------|------------|---------|----------|
| **Precisión** | Los datos representan la realidad | % de registros validados vs muestra | ≥ 98% |
| **Completitud** | Todos los datos requeridos están presentes | % de campos obligatorios con valor | ≥ 95% |
| **Consistencia** | Datos coherentes entre sistemas | % de registros sin conflictos | ≥ 99% |
| **Oportunidad** | Datos disponibles cuando se necesitan | Latencia máxima de actualización | < 24 horas |
| **Unicidad** | Sin duplicados | % de registros únicos | 100% |
| **Validez** | Datos conforme a reglas de negocio | % de registros que pasan validaciones | ≥ 97% |

### 3.2 Reglas de Calidad por Dominio

#### 3.2.1 Dominio: Clientes y Deliveries

| Campo | Regla de Calidad | Criticidad |
|-------|------------------|------------|
| ID Cliente | Único, no nulo, formato CL-XXXX | Crítica |
| Nombre | No nulo, longitud 3-100 caracteres | Alta |
| Dirección | No nula, geocodificable | Crítica |
| Teléfono | Formato válido colombiano (10 dígitos) | Alta |
| Email | Formato email válido (si existe) | Media |
| Coordenadas | Latitud: -4.2 a 12.5, Longitud: -79 a -66 | Crítica |
| Demanda | Valor numérico > 0, ≤ capacidad máxima | Crítica |

#### 3.2.2 Dominio: Vehículos y Flota

| Campo | Regla de Calidad | Criticidad |
|-------|------------------|------------|
| Placa | Única, formato ABC-123 | Crítica |
| Capacidad | Valor numérico > 0 | Crítica |
| Tipo | Valor de lista: CAMIONETA, CAMION, MOTO | Alta |
| Estado | Valor de lista: DISPONIBLE, EN_RUTA, MANTENIMIENTO | Crítica |
| Ubicación | Coordenadas válidas en Colombia | Alta |

#### 3.2.3 Dominio: Rutas y Geolocalización

| Campo | Regla de Calidad | Criticidad |
|-------|------------------|------------|
| Origen | Coordenadas válidas o ID de bodega | Crítica |
| Destino | Coordenadas válidas o ID de cliente | Crítica |
| Distancia | Valor numérico ≥ 0 (km) | Crítica |
| Tiempo | Valor numérico ≥ 0 (minutos) | Alta |

### 3.3 Proceso de Gestión de Calidad

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Monitoreo  │───▶│  Detección  │───▶│   Análisis  │───▶│ Corrección  │
│  Continuo   │    │ de Issues   │    │   de Causa  │    │   y Acción  │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
       │                  │                  │                  │
       │                  │                  │                  │
       ▼                  ▼                  ▼                  ▼
   Dashboards          Tickets            Root Cause         Validación
   Calidad             Issue Tracker      Analysis           Final
```

### 3.4 Métricas y Reportes de Calidad

**Frecuencia de medición:** Semanal
**Responsable:** Data Steward
**Audience:** Comité de Datos, Data Owners

**Dashboard de Calidad incluye:**
1. Score de calidad por dominio (0-100)
2. Tendencia de calidad (últimos 30 días)
3. Issues abiertos por criticidad
4. Tiempo promedio de resolución
5. Top 10 campos con más errores

---

## 4. Catálogo de Activos de Datos

### 4.1 Estructura del Catálogo

Cada activo de datos está documentado con:

| Atributo | Descripción |
|----------|-------------|
| ID Activo | Identificador único |
| Nombre | Nombre descriptivo |
| Descripción | Propósito y uso del activo |
| Data Owner | Responsable del negocio |
| Data Steward | Responsable operativo |
| Formato | CSV, JSON, Parquet, SQL |
| Ubicación | Ruta física o conexión |
| Frecuencia de actualización | Tiempo entre actualizaciones |
| Retención | Tiempo de conservación |
| Clasificación | Confidencial, Interno, Público |
| Linaje | Origen y transformaciones |

### 4.2 Catálogo de Activos

#### ACTIVO-001: Clientes Crudos

| Atributo | Valor |
|----------|-------|
| **ID** | ACTIVO-001 |
| **Nombre** | clientes_raw |
| **Descripción** | Datos de clientes extraídos de datos.gov.co DIVIPOLA con demanda simulada |
| **Data Owner** | Gerente Comercial |
| **Data Steward** | Analista de BI |
| **Formato** | CSV |
| **Ubicación** | `/datos/raw/clientes_raw.csv` |
| **Frecuencia** | Diaria |
| **Retención** | 2 años |
| **Clasificación** | Interno |
| **Linaje** | datos.gov.co API → Extracción → CSV |
| **Registros** | 200 |
| **Campos** | id, nombre, municipio, latitud, longitud, demanda, horario |

---

#### ACTIVO-002: Clientes Limpios

| Atributo | Valor |
|----------|-------|
| **ID** | ACTIVO-002 |
| **Nombre** | clientes_clean |
| **Descripción** | Datos de clientes validados y normalizados para optimización |
| **Data Owner** | Gerente Comercial |
| **Data Steward** | Analista de Datos |
| **Formato** | CSV |
| **Ubicación** | `/datos/processed/clientes_clean.csv` |
| **Frecuencia** | Diaria |
| **Retención** | 2 años |
| **Clasificación** | Interno |
| **Linaje** | clientes_raw → Validación → Normalización → CSV |
| **Registros** | 200 |
| **Campos** | id_cliente, nombre, municipio, latitud, longitud, demanda_kg, hora_inicio_min, hora_fin_min |

---

#### ACTIVO-003: Vehículos Crudos

| Atributo | Valor |
|----------|-------|
| **ID** | ACTIVO-003 |
| **Nombre** | vehiculos_raw |
| **Descripción** | Datos de vehículos de la flota de TransCarga |
| **Data Owner** | Gerente de Operaciones |
| **Data Steward** | Analista de Datos |
| **Formato** | CSV |
| **Ubicación** | `/datos/raw/vehiculos_raw.csv` |
| **Frecuencia** | Semanal |
| **Retención** | 5 años (vida útil del vehículo + 2 años) |
| **Clasificación** | Confidencial |
| **Linaje** | Sistema interno → Export → CSV |
| **Registros** | 85 |
| **Campos** | id_vehiculo, placa, tipo, capacidad_kg, estado, ubicacion |

---

#### ACTIVO-004: DIVIPOLA Geolocalizado

| Atributo | Valor |
|----------|-------|
| **ID** | ACTIVO-004 |
| **Nombre** | divipola_raw |
| **Descripción** | Datos geográficos de municipios colombianos (DIVIPOLA) |
| **Data Owner** | Director de Tecnología |
| **Data Steward** | Analista de Datos |
| **Formato** | CSV |
| **Ubicación** | `/datos/raw/divipola_raw.csv` |
| **Frecuencia** | Mensual (verificación de cambios) |
| **Retención** | Indefinida (datos de referencia) |
| **Clasificación** | Público |
| **Linaje** | datos.gov.co API → Extracción → CSV |
| **Registros** | 1,121 |
| **Fuente** | https://www.datos.gov.co/resource/vafm-j2df.json |

---

#### ACTIVO-005: Precios Combustible

| Atributo | Valor |
|----------|-------|
| **ID** | ACTIVO-005 |
| **Nombre** | combustible_raw |
| **Descripción** | Precios de combustible por municipio |
| **Data Owner** | Gerente Financiero |
| **Data Steward** | Analista de Datos |
| **Formato** | CSV |
| **Ubicación** | `/datos/raw/combustible_raw.csv` |
| **Frecuencia** | Semanal |
| **Retención** | 3 años |
| **Clasificación** | Público |
| **Linaje** | datos.gov.co API → Extracción → CSV |
| **Fuente** | https://www.datos.gov.co/resource/x6id-4v3g.json |

---

#### ACTIVO-006: Matriz de Distancias

| Atributo | Valor |
|----------|-------|
| **ID** | ACTIVO-006 |
| **Nombre** | matriz_distancias |
| **Descripción** | Matriz de distancias Haversine entre todos los puntos (bodegas + clientes) |
| **Data Owner** | Coordinador de Logística |
| **Data Steward** | Analista de Datos |
| **Formato** | CSV |
| **Ubicación** | `/datos/processed/matriz_distancias.csv` |
| **Frecuencia** | Diaria |
| **Retención** | 6 meses |
| **Clasificación** | Interno |
| **Linaje** | DIVIPOLA + Clientes → Cálculo Haversine → Matriz |
| **Dimensiones** | 52 x 52 (nodos) |
| **Unidad** | Kilómetros |

---

#### ACTIVO-007: Rutas Optimizadas

| Atributo | Valor |
|----------|-------|
| **ID** | ACTIVO-007 |
| **Nombre** | rutas_optimizadas |
| **Descripción** | Resultado del modelo de optimización VRP con asignación de clientes a vehículos |
| **Data Owner** | Coordinador de Logística |
| **Data Steward** | Analista de Datos |
| **Formato** | CSV |
| **Ubicación** | `/datos/results/rutas_optimizadas.csv` |
| **Frecuencia** | Diaria (por cada ejecución del modelo) |
| **Retención** | 1 año |
| **Clasificación** | Confidencial |
| **Linaje** | Clientes + Vehículos + Matrices → OR-Tools CVRP → CSV |
| **Campos** | vehiculo_id, parada_num, cliente_id, tipo, carga_kg, distancia_km, tiempo_min |

---

#### ACTIVO-008: Métricas de Optimización

| Atributo | Valor |
|----------|-------|
| **ID** | ACTIVO-008 |
| **Nombre** | metricas_optimizacion |
| **Descripción** | Métricas agregadas de la optimización de rutas |
| **Data Owner** | Coordinador de Logística |
| **Data Steward** | Analista de Datos |
| **Formato** | JSON |
| **Ubicación** | `/datos/results/metricas_optimizacion.json` |
| **Frecuencia** | Diaria |
| **Retención** | 2 años |
| **Clasificación** | Interno |
| **Campos** | distancia_total_km, clientes_atendidos, vehiculos_utilizados, costo_total_cop |

---

### 4.3 Diccionario de Datos

#### Tabla: clientes_clean

| Campo | Tipo | Nullable | Default | Descripción | Ejemplo |
|-------|------|----------|---------|-------------|---------|
| id_cliente | VARCHAR(10) | NO | - | Identificador único del cliente | CL-0001 |
| nombre | VARCHAR(100) | NO | - | Nombre o razón social | Cliente ABC Ltda |
| municipio | VARCHAR(50) | NO | - | Nombre del municipio DIVIPOLA | MEDELLÍN |
| latitud | DECIMAL(9,6) | NO | - | Coordenada latitud WGS84 | 6.251840 |
| longitud | DECIMAL(9,6) | NO | - | Coordenada longitud WGS84 | -75.563591 |
| demanda_kg | INTEGER | NO | - | Demanda en kilogramos | 500 |
| hora_inicio_min | INTEGER | NO | 480 | Hora inicio ventana (minutos desde 00:00) | 480 (08:00) |
| hora_fin_min | INTEGER | NO | 1020 | Hora fin ventana (minutos desde 00:00) | 1020 (17:00) |

#### Tabla: vehiculos_clean

| Campo | Tipo | Nullable | Default | Descripción | Ejemplo |
|-------|------|----------|---------|-------------|---------|
| id_vehiculo | VARCHAR(10) | NO | - | Identificador único | VH-001 |
| placa | VARCHAR(7) | NO | - | Placa vehicular colombiana | ABC-123 |
| tipo | VARCHAR(20) | NO | - | Tipo de vehículo | CAMIONETA |
| capacidad_kg | INTEGER | NO | - | Capacidad máxima de carga | 2000 |
| estado | VARCHAR(20) | NO | DISPONIBLE | Estado operativo | DISPONIBLE |
| costo_km_cop | DECIMAL(10,2) | NO | - | Costo operativo por km | 850.00 |

---

## 5. Estándares y Normativas

### 5.1 Estándares de Nomenclatura

#### 5.1.1 Nombres de Archivos

| Regla | Formato | Ejemplo |
|-------|---------|---------|
| Archivos crudos | `{entidad}_raw.csv` | clientes_raw.csv |
| Archivos limpios | `{entidad}_clean.csv` | clientes_clean.csv |
| Archivos de salida | `{entidad}_output.csv` | rutas_output.csv |
| Archivos de resultado | `{entidad}.csv` | rutas_optimizadas.csv |
| Matrices | `matriz_{tipo}.csv` | matriz_distancias.csv |
| Configuraciones | `config_{modelo}.json` | config_modelo.json |

#### 5.1.2 Nombres de Campos

| Regla | Ejemplo Correcto | Ejemplo Incorrecto |
|-------|------------------|-------------------|
| Usar snake_case | id_cliente | idCliente |
| Incluir unidad si aplica | demanda_kg, tiempo_min | demanda, tiempo |
| No usar abreviaturas oscuras | coordenada_latitud | coord_lat |
| IDs con prefijo semántico | id_cliente, id_vehiculo | id, codigo |

#### 5.1.3 Códigos y Identificadores

| Entidad | Formato | Ejemplo |
|---------|---------|---------|
| Cliente | CL-XXXX | CL-0001, CL-0200 |
| Vehículo | VH-XXX | VH-001, VH-085 |
| Bodega | BD-XX | BD-01 (Medellín), BD-02 (Cali) |
| Ruta | RT-YYYYMMDD-VXX | RT-20260511-V01 |

### 5.2 Estándares de Formato

#### 5.2.1 Fechas y Tiempos

| Tipo | Formato | Ejemplo |
|------|---------|---------|
| Fecha | ISO 8601: YYYY-MM-DD | 2026-05-11 |
| Hora | 24 horas: HH:MM:SS | 14:30:00 |
| Fecha-Hora | ISO 8601: YYYY-MM-DDTHH:MM:SS | 2026-05-11T14:30:00 |
| Ventana de tiempo | Minutos desde 00:00 | 480 (08:00), 1020 (17:00) |

#### 5.2.2 Coordenadas Geográficas

| Tipo | Formato | Precisión |
|------|---------|-----------|
| Sistema de referencia | WGS84 (EPSG:4326) | - |
| Latitud | Decimal, 6 decimales | 6.251840 |
| Longitud | Decimal, 6 decimales | -75.563591 |
| Rango válido Colombia | Lat: -4.2 a 12.5, Lon: -79 a -66 | - |

#### 5.2.3 Valores Monetarios

| Tipo | Formato | Ejemplo |
|------|---------|---------|
| Moneda | COP (Peso Colombiano) | - |
| Formato | Decimal, 2 decimales | 1234567.89 |
| Sin separador de miles en dato | 1234567.89 | NO: 1,234,567.89 |

### 5.3 Estándares de Codificación

#### 5.3.1 Python

| Aspecto | Estándar |
|---------|----------|
| Estilo | PEP 8 |
| Imports | Orden: stdlib, third-party, local |
| Docstrings | Google style |
| Tipado | Type hints obligatorios |
| Encoding | UTF-8 |

**Ejemplo de función documentada:**
```python
def calcular_distancia_haversine(
    lat1: float, 
    lon1: float, 
    lat2: float, 
    lon2: float
) -> float:
    """
    Calcula la distancia Haversine entre dos puntos geográficos.
    
    Args:
        lat1: Latitud del punto origen en grados decimales.
        lon1: Longitud del punto origen en grados decimales.
        lat2: Latitud del punto destino en grados decimales.
        lon2: Longitud del punto destino en grados decimales.
    
    Returns:
        Distancia en kilómetros entre los dos puntos.
    
    Raises:
        ValueError: Si las coordenadas están fuera del rango válido.
    """
    # Implementación...
```

---

## 6. Seguridad y Privacidad

### 6.1 Clasificación de Datos

| Nivel | Definición | Ejemplos | Controles |
|-------|------------|----------|-----------|
| **Público** | Sin restricción, disponible externamente | DIVIPOLA, precios combustible | Ninguno |
| **Interno** | Solo para uso interno, no sensible | Rutas optimizadas, métricas | Autenticación básica |
| **Confidencial** | Información sensible del negocio | Datos de clientes, flota | Autenticación + Autorización |
| **Restringido** | Altamente sensible, pocos autorizados | Datos financieros detallados | Cifrado + Auditoría |

### 6.2 Matriz de Acceso

| Rol | Público | Interno | Confidencial | Restringido |
|-----|---------|---------|--------------|-------------|
| Ejecutivo | Leer | Leer | Leer | Leer |
| Data Owner | Leer | Leer/Escribir | Leer/Escribir | Leer |
| Data Steward | Leer | Leer/Escribir | Leer/Escribir | - |
| Analista | Leer | Leer | Leer | - |
| Operativo | Leer | Leer (limitado) | - | - |
| Externo | Leer | - | - | - |

### 6.3 Controles de Seguridad

#### 6.3.1 Control de Acceso

| Control | Descripción | Implementación |
|---------|-------------|----------------|
| Autenticación | Verificar identidad del usuario | Usuario/contraseña, MFA para roles críticos |
| Autorización | Verificar permisos del usuario | RBAC (Role-Based Access Control) |
| Auditoría | Registrar accesos y cambios | Logs con timestamp, usuario, acción |

#### 6.3.2 Protección de Datos

| Control | Descripción |
|---------|-------------|
| Cifrado en tránsito | HTTPS/TLS para todas las conexiones |
| Cifrado en reposo | Cifrado de archivos sensibles |
| Backup | Copias diarias, retención 30 días |
| Sanitización | Eliminación segura de datos al archivar |

### 6.4 Privacidad de Datos Personales

#### 6.4.1 Cumplimiento Legal

**Ley 1581 de 2012 (Habeas Data)**
- Principio de finalidad: Datos solo para propósito específico
- Principio de veracidad: Datos exactos y actualizados
- Principio de seguridad: Protección contra acceso no autorizado
- Derecho de acceso: Titulares pueden conocer sus datos
- Derecho de rectificación: Titulares pueden corregir datos

#### 6.4.2 Datos Personales Identificados

| Dato | Tipo | Tratamiento |
|------|------|-------------|
| Nombre cliente | Personal | Uso operativo, acceso restringido |
| Teléfono cliente | Personal | Uso operativo, no compartir externamente |
| Dirección cliente | Personal | Uso operativo, geocodificación |
| Ubicación vehículo | Personal | Solo durante operación, historial 30 días |

#### 6.4.3 Medidas de Privacidad

1. **Minimización**: Solo recolectar datos necesarios
2. **Anonimización**: Para análisis agregados, usar IDs anónimos
3. **Pseudonimización**: Para desarrollo/testing, reemplazar datos reales
4. **Retención limitada**: Eliminar datos después del período de retención

---

## 7. Trazabilidad y Linaje de Datos

### 7.1 Concepto de Linaje

El linaje de datos documenta el ciclo de vida completo de los datos:
- **Origen**: De dónde provienen los datos
- **Transformaciones**: Qué procesos se aplican
- **Destino**: Dónde terminan los datos
- **Responsables**: Quién controla cada etapa

### 7.2 Diagrama de Linaje - Pipeline ETL

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           FUENTES EXTERNAS                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐   │
│  │  datos.gov.co│  │ datos.gov.co │  │ datos.gov.co │  │   Sistema    │   │
│  │   DIVIPOLA   │  │  Combustible │  │   Parque     │  │   Interno    │   │
│  │  vafm-j2df   │  │   x6id-4v3g  │  │  Automotor   │  │              │   │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘   │
│         │                 │                 │                 │           │
└─────────┼─────────────────┼─────────────────┼─────────────────┼───────────┘
          │                 │                 │                 │
          ▼                 ▼                 ▼                 ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CAPA DE EXTRACCIÓN (01)                             │
│  Notebook: 01_extraccion.ipynb                                              │
│  Responsable: Data Steward                                                  │
│  Frecuencia: Diaria                                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────────┐                                                       │
│  │ API Requests     │ → requests.get(url, params={'$limit': 5000})         │
│  └────────┬─────────┘                                                       │
│           │                                                                 │
│           ▼                                                                 │
│  ┌──────────────────┐                                                       │
│  │ Validación HTTP  │ → status_code == 200                                  │
│  └────────┬─────────┘                                                       │
│           │                                                                 │
│           ▼                                                                 │
│  ┌──────────────────┐                                                       │
│  │ Guardar CSV      │ → datos/raw/{entidad}_raw.csv                        │
│  └────────┬─────────┘                                                       │
│                                                                             │
└─────────┼───────────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      CAPA DE DATOS CRUDOS (/datos/raw/)                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  divipola_raw.csv     │ 1,121 registros │ Coordenadas municipios           │
│  combustible_raw.csv  │ 5,000+ registros│ Precios por municipio            │
│  vehiculos_raw.csv    │ 85 registros    │ Flota TransCarga                 │
│  clientes_raw.csv     │ 200 registros   │ Clientes simulados               │
└─────────────────────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      CAPA DE TRANSFORMACIÓN (02)                            │
│  Notebook: 02_transformacion.ipynb                                          │
│  Responsable: Data Steward                                                  │
│  Frecuencia: Diaria                                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Transformaciones:                                                          │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ 1. DIVIPOLA: Filtrar Antioquia/Valle, validar coordenadas          │    │
│  │ 2. Combustible: Convertir precio a numérico, filtrar departamentos │    │
│  │ 3. Clientes: Validar coords, convertir horarios a minutos          │    │
│  │ 4. Vehículos: Calcular eficiencia, validar estados                 │    │
│  │ 5. Matrices: Calcular distancias Haversine, estimar tiempos        │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────┼───────────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CAPA DE DATOS LIMPIOS (/datos/processed/)                │
├─────────────────────────────────────────────────────────────────────────────┤
│  divipola_clean.csv       │ 240 registros  │ Solo Antioquia/Valle         │
│  combustible_clean.csv    │ 500 registros  │ Precios validados            │
│  clientes_clean.csv       │ 200 registros  │ Clientes normalizados        │
│  vehiculos_clean.csv      │ 64 registros   │ Vehículos disponibles        │
│  matriz_distancias.csv    │ 52x52          │ Distancias Haversine         │
│  matriz_tiempos.csv       │ 52x52          │ Tiempos estimados            │
└─────────────────────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                          CAPA DE CARGA (03)                                 │
│  Notebook: 03_carga.ipynb                                                   │
│  Responsable: Data Steward                                                  │
│  Frecuencia: Diaria                                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Genera archivos de entrada para el modelo de optimización:                 │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ optimizacion_clientes.csv    → 200 clientes con demanda           │    │
│  │ optimizacion_vehiculos.csv   → 64 vehículos con capacidad         │    │
│  │ optimizacion_bodegas.csv     → 2 bodegas (Medellín, Cali)         │    │
│  │ config_modelo.json           → Parámetros CVRP                    │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────┼───────────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                      CAPA DE DATOS SALIDA (/datos/output/)                  │
├─────────────────────────────────────────────────────────────────────────────┤
│  optimizacion_clientes.csv      │ 200 registros │ Input modelo             │
│  optimizacion_vehiculos.csv     │ 64 registros  │ Input modelo             │
│  optimizacion_matriz_dist.csv   │ 52x52         │ Input modelo             │
│  config_modelo.json             │ 1 archivo     │ Parámetros               │
└─────────────────────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                       CAPA DE OPTIMIZACIÓN (04)                             │
│  Notebook: 04_optimizacion.ipynb                                            │
│  Responsable: Analista de Datos                                             │
│  Frecuencia: Diaria (o por demanda)                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Modelo: CVRP con Google OR-Tools                                           │
│  ┌────────────────────────────────────────────────────────────────────┐    │
│  │ - RoutingIndexManager: Gestión de índices                          │    │
│  │ - RoutingModel: Modelo de enrutamiento                             │    │
│  │ - DistanceCallback: Función de distancia                           │    │
│  │ - AddDimensionWithVehicleCapacity: Restricción capacidad           │    │
│  │ - GUIDED_LOCAL_SEARCH: Metaheurística de búsqueda                  │    │
│  └────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────┼───────────────────────────────────────────────────────────────────┘
          │
          ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CAPA DE RESULTADOS (/datos/results/)                     │
├─────────────────────────────────────────────────────────────────────────────┤
│  rutas_optimizadas.csv       │ Detalle de paradas por vehículo             │
│  rutas_optimizadas.png       │ Visualización de rutas                      │
│  metricas_optimizacion.json  │ Métricas de la solución                     │
│  reporte_vehiculos.csv       │ Resumen por vehículo                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 7.3 Metadata de Linaje

| Activo | Origen | Transformación | Destino | Responsable |
|--------|--------|----------------|---------|-------------|
| clientes_clean | clientes_raw + DIVIPOLA | Validación, geocoding | optimizacion_clientes | Data Steward |
| matriz_distancias | clientes_clean | Haversine calculation | optimizacion_matriz | Data Steward |
| rutas_optimizadas | optimizacion_* | CVRP optimization | Despacho operativo | Analista |

---

## 8. Gestión del Ciclo de Vida

### 8.1 Retención de Datos

| Tipo de Dato | Período de Retención | Justificación | Destino Final |
|--------------|---------------------|---------------|---------------|
| Datos crudos | 30 días | Auditoría inicial | Eliminación |
| Datos procesados | 6 meses | Reprocesamiento | Archivo comprimido |
| Resultados optimización | 1 año | Análisis histórico | Archivo |
| Logs de auditoría | 2 años | Cumplimiento legal | Archivo seguro |
| DIVIPOLA (referencia) | Indefinida | Datos de referencia | - |

### 8.2 Archivado y Eliminación

#### Proceso de Archivado:
1. Data Owner aprueba archivado
2. Data Custodian comprime datos
3. Mover a `/datos/archive/YYYY-MM/`
4. Registrar en catálogo como "Archivado"
5. Actualizar metadata

#### Proceso de Eliminación:
1. Verificar que retención expiró
2. Data Owner autoriza eliminación
3. Data Custodian ejecuta eliminación segura
4. Registrar en log de auditoría
5. Actualizar catálogo como "Eliminado"

---

## 9. Métricas y KPIs

### 9.1 KPIs de Gobierno de Datos

| KPI | Fórmula | Objetivo | Frecuencia |
|-----|---------|----------|------------|
| Score de Calidad | (Issues resueltos / Total issues) × 100 | ≥ 95% | Semanal |
| Tiempo de Resolución | Promedio días Issue → Cierre | ≤ 5 días | Mensual |
| Completitud de Metadata | (Activos con metadata completa / Total activos) × 100 | 100% | Mensual |
| Cumplimiento de Estándares | (Campos conforme estándar / Total campos) × 100 | ≥ 98% | Mensual |
| Incidentes de Seguridad | Conteo de incidentes | 0 | Mensual |
| Tiempo de Acceso | Promedio tiempo respuesta query | < 5 seg | Diario |

### 9.2 Dashboard de Gobierno

**Contenido:**
1. Score de calidad por dominio (gauge chart)
2. Tendencia de calidad últimos 30 días (line chart)
3. Issues por criticidad (pie chart)
4. Top 5 activos con más problemas (bar chart)
5. Cumplimiento de retención (table)
6. Accesos no autorizados (counter)

---

## 10. Procesos y Procedimientos

### 10.1 Proceso de Solicitud de Acceso a Datos

```
┌─────────────┐
│ Usuario     │
│ solicita    │
│ acceso      │
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│ Data Steward        │
│ revisa solicitud    │
│ (1 día hábil)       │
└──────┬──────────────┘
       │
       ├─── Rechazada ──→ Notificar usuario ──→ FIN
       │
       ▼
┌─────────────────────┐
│ Data Owner          │
│ aprueba/rechaza     │
│ (2 días hábiles)    │
└──────┬──────────────┘
       │
       ├─── Rechazada ──→ Notificar usuario ──→ FIN
       │
       ▼
┌─────────────────────┐
│ Data Custodian      │
│ configura permisos  │
│ (1 día hábil)       │
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│ Usuario notificado  │
│ con credenciales    │
└─────────────────────┘
```

### 10.2 Proceso de Reporte de Issue de Calidad

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│ Usuario     │────▶│ Data        │────▶│ Clasificar  │
│ reporta     │     │ Steward     │     │ criticidad  │
│ issue       │     │ registra    │     │             │
└─────────────┘     └─────────────┘     └──────┬──────┘
                                               │
                    ┌──────────────────────────┼──────────────────────┐
                    │                          │                      │
                    ▼                          ▼                      ▼
            ┌─────────────┐            ┌─────────────┐        ┌─────────────┐
            │ Crítica     │            │ Alta        │        │ Media/Baja  │
            │ < 4 horas   │            │ < 24 horas  │        │ < 5 días    │
            └──────┬──────┘            └──────┬──────┘        └──────┬──────┘
                   │                          │                      │
                   └──────────────────────────┴──────────────────────┘
                                              │
                                              ▼
                                     ┌─────────────────┐
                                     │ Analizar causa  │
                                     │ raíz            │
                                     └────────┬────────┘
                                              │
                                              ▼
                                     ┌─────────────────┐
                                     │ Implementar     │
                                     │ corrección      │
                                     └────────┬────────┘
                                              │
                                              ▼
                                     ┌─────────────────┐
                                     │ Validar         │
                                     │ solución        │
                                     └────────┬────────┘
                                              │
                                              ▼
                                     ┌─────────────────┐
                                     │ Cerrar issue    │
                                     │ y documentar    │
                                     └─────────────────┘
```

---

## 11. Herramientas

### 11.1 Stack Tecnológico de Gobierno

| Función | Herramienta | Propósito |
|---------|-------------|-----------|
| Catálogo de datos | Documentación Markdown | Inventario de activos |
| Calidad de datos | pandas, pytest | Validaciones automatizadas |
| Versionamiento | Git/GitHub | Trazabilidad de cambios |
| Monitoreo | Logs + Dashboards | Métricas de calidad |
| Backup | Git + OneDrive | Recuperación |
| Auditoría | Logs estructurados | Registro de accesos |

### 11.2 Automatización de Validaciones

**Script de validación diaria:**
```python
# validar_calidad_datos.py
def validar_clientes():
    df = pd.read_csv('datos/processed/clientes_clean.csv')
    
    # Validaciones
    assert df['id_cliente'].is_unique, "IDs duplicados"
    assert df['demanda_kg'].min() > 0, "Demandas negativas"
    assert df['latitud'].between(-4.2, 12.5).all(), "Latitudes inválidas"
    assert df['longitud'].between(-79, -66).all(), "Longitudes inválidas"
    
    return True
```

---

## 12. Capacitación y Cultura

### 12.1 Programa de Capacitación

| Audiencia | Tema | Frecuencia | Duración |
|-----------|------|------------|----------|
| Todos | Introducción a Gobierno de Datos | Onboarding | 2 horas |
| Usuarios | Uso de datos y políticas | Anual | 1 hora |
| Data Stewards | Técnicas de calidad | Semestral | 4 horas |
| Data Owners | Responsabilidades y KPIs | Semestral | 2 horas |

### 12.2 Comunicación

| Mecanismo | Frecuencia | Contenido |
|-----------|------------|-----------|
| Boletín de datos | Mensual | Novedades, tips, métricas |
| Comité de datos | Mensual | Decisión y seguimiento |
| Wiki interna | Continuo | Documentación actualizada |
| Slack/Teams | Diario | Consultas rápidas |

---

## 13. Cumplimiento y Auditoría

### 13.1 Auditorías

| Tipo | Frecuencia | Responsable | Alcance |
|------|------------|-------------|---------|
| Interna de calidad | Mensual | Data Steward | Validaciones |
| Interna de seguridad | Semestral | Data Custodian | Accesos, cifrado |
| Externa | Anual | Auditor externo | Cumplimiento legal |

### 13.2 Checklist de Cumplimiento

**Mensual:**
- [ ] Revisar score de calidad por dominio
- [ ] Actualizar catálogo de activos
- [ ] Revisar issues pendientes
- [ ] Verificar backups

**Semestral:**
- [ ] Revisar políticas de retención
- [ ] Auditar accesos y permisos
- [ ] Actualizar documentación
- [ ] Capacitar usuarios nuevos

**Anual:**
- [ ] Auditoría externa de cumplimiento
- [ ] Revisión de roles y responsabilidades
- [ ] Actualizar marco de gobierno

---

## 14. Anexos

### Anexo A: Plantilla de Solicitud de Acceso

```
SOLICITUD DE ACCESO A DATOS

Fecha: ___________
Solicitante: ___________
Área: ___________

Datos solicitados:
- Activo de datos: ___________
- Justificación: ___________
- Duración estimada: ___________
- Tipo de acceso: [ ] Lectura [ ] Escritura

Firma solicitante: ___________
Aprobación Data Steward: ___________
Aprobación Data Owner: ___________
```

### Anexo B: Plantilla de Reporte de Issue

```
REPORTE DE ISSUE DE CALIDAD

ID Issue: ___________
Fecha: ___________
Reportado por: ___________

Descripción:
___________

Activo afectado: ___________
Campo(s): ___________
Criticidad: [ ] Crítica [ ] Alta [ ] Media [ ] Baja

Evidencia:
___________

Causa raíz:
___________

Acción correctiva:
___________

Fecha cierre: ___________
Validado por: ___________
```

---

## 15. Aprobaciones

| Rol | Nombre | Firma | Fecha |
|-----|--------|-------|-------|
| Gerente General | | | |
| Gerente de Operaciones | | | |
| Gerente Comercial | | | |
| Director de Tecnología | | | |

---

**Documento preparado por:** Data Office TransCarga S.A.S.  
**Versión:** 1.0  
**Fecha de creación:** 2026-05-11  
**Próxima revisión:** 2026-11-11

---

*Este documento es confidencial y de uso interno de TransCarga S.A.S.*
