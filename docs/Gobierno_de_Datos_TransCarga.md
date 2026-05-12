# Gobierno de Datos — TransCarga S.A.S.

## Primer Borrador | Segunda Entrega

**Universidad Pontificia Bolivariana — Data Office Strategy, 2026**

---

## 1. Introducción

Este documento define el marco de gobierno de datos para TransCarga S.A.S. Establece los roles, responsabilidades, políticas, estándares de calidad, catálogo de datos, reglas de seguridad y trazabilidad necesarios para que los datos sean un activo estratégico confiable.

Hoy TransCarga no tiene ninguna gestión formal de datos: la información está dispersa en Excel, WhatsApp y sistemas desconectados. No hay estándares de calidad, no hay responsables definidos, y las decisiones se toman por intuición. Este documento cambia eso.

---

## 2. Objetivos del Gobierno de Datos

| Objetivo | Descripción | KPI |
|----------|-------------|-----|
| Calidad | Datos precisos, completos, consistentes y oportunos | >95% registros sin errores |
| Disponibilidad | Acceso a datos cuando se necesiten, por personas autorizadas | Uptime pipelines >99% |
| Seguridad | Proteger datos de accesos no autorizados o pérdida | 0 incidentes de filtración |
| Trazabilidad | Rastrear origen, transformaciones y destino de cada dato | 100% datasets con linaje documentado |
| Estandarización | Formatos y convenciones comunes | 100% campos con definición en catálogo |
| Cumplimiento | Cumplir Ley 1581 de 2012 (Protección de Datos Personales) | 100% datos personales con consentimiento |

---

## 3. Roles y Responsabilidades

### 3.1 Estructura de Gobierno

```
CEO / Sponsor Ejecutivo
    │   Aprueba políticas, asigna presupuesto
    │
Data Owner (Gerente por área)
    │   Responsable del dominio de datos, aprueba accesos
    │
Data Steward (Analista por squad)
    │   Cuida la calidad diaria, valida, corrige, documenta
    │
Data Engineer (Equipo técnico)
    │   Construye y mantiene pipelines ETL, infraestructura
    │
Data Consumer (Usuarios finales)
        Accede a dashboards y reportes para decisiones
```

### 3.2 Matriz RACI

| Actividad | CEO | Data Owner | Data Steward | Data Engineer | Data Consumer |
|-----------|-----|------------|--------------|---------------|---------------|
| Definir políticas de datos | A | R | C | C | I |
| Aprobar accesos a datos | I | A/R | C | I | I |
| Validar calidad de datos | I | A | R | C | I |
| Construir pipelines ETL | I | I | C | R | I |
| Mantener catálogo de datos | I | A | R | C | I |
| Monitorear cumplimiento legal | A | R | C | I | I |
| Consumir dashboards/reportes | I | I | I | I | R |
| Resolver incidentes de datos | I | A | R | R | I |

**R** = Responsable | **A** = Aprueba | **C** = Consultado | **I** = Informado

### 3.3 Asignación en TransCarga

| Rol | Persona / Área | Responsabilidad |
|-----|----------------|-----------------|
| Sponsor Ejecutivo | CEO | Aprueba políticas, presupuesto |
| Data Owner — Operaciones | Líder Squad Entregas | Datos de rutas, entregas, conductores, vehículos |
| Data Owner — Comercial | Líder Squad Crecimiento | Datos de clientes, pedidos, facturación |
| Data Owner — Plataforma | Líder Squad Plataforma | Datos técnicos (logs, APIs, rendimiento) |
| Data Steward — Operaciones | Analista operativo | Valida GPS, tiempos, entregas |
| Data Steward — Comercial | Analista comercial | Valida clientes, pedidos, NPS |
| Data Engineer | Equipo técnico (2-3 personas) | Pipelines ETL, Data Lake, monitoreo |
| Data Consumer | Gerentes, operadores, conductores | Dashboards y reportes |

---

## 4. Catálogo de Datos

### 4.1 Dominio: Clientes

| Campo | Tipo | Formato | Obligatorio | Descripción | Ejemplo |
|-------|------|---------|-------------|-------------|---------|
| cliente_id | String | UUID v4 | Sí | Identificador único del cliente | "a1b2c3d4-..." |
| razon_social | String | Texto libre | Sí | Nombre legal del cliente PYME | "Distribuciones El Café S.A.S." |
| nit | String | NNN.NNN.NNN-D | Sí | Número de identificación tributaria | "900.123.456-7" |
| direccion | String | Texto libre | Sí | Dirección física del cliente | "Cra 45 #32-10, Medellín" |
| latitud | Float | Decimal 6 dígitos | Sí | Coordenada geográfica | 6.244203 |
| longitud | Float | Decimal 6 dígitos | Sí | Coordenada geográfica | -75.581211 |
| telefono | String | 10 dígitos | Sí | Teléfono de contacto | "3001234567" |
| email | String | RFC 5322 | No | Correo electrónico | "contacto@elcafe.com" |
| ciudad | String | Catálogo DIVIPOLA | Sí | Ciudad del cliente | "Medellín" |
| departamento | String | Catálogo DIVIPOLA | Sí | Departamento | "Antioquia" |
| fecha_registro | Date | YYYY-MM-DD | Sí | Fecha de alta en el sistema | "2024-03-15" |
| estado | String | Enum: activo/inactivo | Sí | Estado del cliente | "activo" |
| clasificacion | String | Enum: A/B/C | No | Clasificación por volumen | "A" |

### 4.2 Dominio: Pedidos

| Campo | Tipo | Formato | Obligatorio | Descripción | Ejemplo |
|-------|------|---------|-------------|-------------|---------|
| pedido_id | String | UUID v4 | Sí | Identificador único del pedido | "e5f6g7h8-..." |
| cliente_id | String | UUID v4 (FK) | Sí | Referencia al cliente | "a1b2c3d4-..." |
| fecha_creacion | Datetime | ISO 8601 | Sí | Fecha y hora de creación | "2026-05-10T14:30:00" |
| direccion_entrega | String | Texto libre | Sí | Dirección de destino | "Calle 10 #25-30, Envigado" |
| lat_entrega | Float | Decimal 6 dígitos | Sí | Latitud destino | 6.171389 |
| lon_entrega | Float | Decimal 6 dígitos | Sí | Longitud destino | -75.590833 |
| peso_kg | Float | Decimal 2 dígitos | Sí | Peso del paquete en kg | 12.50 |
| volumen_m3 | Float | Decimal 3 dígitos | No | Volumen en metros cúbicos | 0.045 |
| estado | String | Enum | Sí | Estado del pedido | "en_transito" |
| conductor_id | String | UUID v4 (FK) | No | Conductor asignado | "i9j0k1l2-..." |
| vehiculo_id | String | UUID v4 (FK) | No | Vehículo asignado | "m3n4o5p6-..." |
| fecha_entrega | Datetime | ISO 8601 | No | Fecha real de entrega | "2026-05-10T16:45:00" |
| firma_digital | Boolean | true/false | No | Si el cliente firmó recepción | true |

**Estados válidos del pedido:** creado → asignado → en_transito → entregado | fallido | devuelto

### 4.3 Dominio: Rutas y GPS

| Campo | Tipo | Formato | Obligatorio | Descripción | Ejemplo |
|-------|------|---------|-------------|-------------|---------|
| ruta_id | String | UUID v4 | Sí | Identificador de la ruta | "q7r8s9t0-..." |
| conductor_id | String | UUID v4 (FK) | Sí | Conductor asignado | "i9j0k1l2-..." |
| vehiculo_id | String | UUID v4 (FK) | Sí | Vehículo asignado | "m3n4o5p6-..." |
| fecha_ruta | Date | YYYY-MM-DD | Sí | Fecha de la ruta | "2026-05-10" |
| pedidos_asignados | Array[String] | Lista UUID | Sí | Pedidos en esta ruta | ["e5f6...", "u1v2..."] |
| distancia_km | Float | Decimal 1 dígito | Sí | Distancia total en km | 87.3 |
| tiempo_estimado_min | Integer | Minutos | Sí | Tiempo estimado | 210 |
| tiempo_real_min | Integer | Minutos | No | Tiempo real (post-entrega) | 245 |
| costo_combustible | Float | COP | No | Costo de combustible de la ruta | 85000.00 |

### 4.4 Dominio: Vehículos

| Campo | Tipo | Formato | Obligatorio | Descripción | Ejemplo |
|-------|------|---------|-------------|-------------|---------|
| vehiculo_id | String | UUID v4 | Sí | Identificador único | "m3n4o5p6-..." |
| placa | String | AAA-000 | Sí | Placa del vehículo | "ABC-123" |
| tipo | String | Enum | Sí | Tipo de vehículo | "furgon" |
| capacidad_kg | Float | Decimal | Sí | Capacidad máxima en kg | 3500.00 |
| capacidad_m3 | Float | Decimal | Sí | Capacidad volumétrica | 18.5 |
| año_modelo | Integer | YYYY | Sí | Año del vehículo | 2018 |
| estado | String | Enum | Sí | Estado operativo | "activo" |
| km_acumulados | Integer | Entero | Sí | Kilómetros acumulados | 185000 |
| fecha_ultimo_mantenimiento | Date | YYYY-MM-DD | Sí | Último mantenimiento | "2026-04-15" |

---

## 5. Políticas de Calidad de Datos

### 5.1 Reglas de Validación

| Dimensión | Regla | Acción si falla |
|-----------|-------|-----------------|
| Completitud | Campos obligatorios siempre llenos | Rechazar registro, notificar Data Steward |
| Precisión | Coordenadas dentro de Colombia (lat 1°-13°, lon -79° a -67°) | Marcar inválido, geocodificar manualmente |
| Consistencia | Mismo cliente = mismo ID (deduplicación por NIT) | Fusionar registros, mantener el más reciente |
| Oportunidad | Datos GPS con menos de 5 min de retraso | Alertar si vehículo no reporta en 5 min |
| Validez | Formatos según catálogo (teléfono 10 dígitos, NIT válido) | Rechazar y pedir corrección |
| Unicidad | Sin registros duplicados por tabla | Deduplicar automáticamente en ETL |

### 5.2 Métricas de Calidad

| Métrica | Fórmula | Objetivo | Frecuencia |
|---------|---------|----------|------------|
| Tasa de completitud | Registros completos / Total registros × 100 | >95% | Diaria |
| Tasa de precisión | Coordenadas válidas / Total coordenadas × 100 | >98% | Diaria |
| Tasa de duplicados | Registros duplicados / Total registros × 100 | <1% | Semanal |
| Latencia de datos GPS | Promedio de retraso en segundos | <60s | Tiempo real |
| Tasa de entregas sin firma | Entregas sin firma digital / Total entregas × 100 | <5% | Diaria |

---

## 6. Políticas de Seguridad y Privacidad

### 6.1 Clasificación de Datos

| Nivel | Descripción | Ejemplos | Acceso |
|-------|-------------|----------|--------|
| Público | Datos no sensibles, pueden ser compartidos | Nombre empresa, ciudad, tipo de servicio | Todos |
| Interno | Datos operativos de uso interno | Rutas, tiempos, costos, KPIs | Empleados autorizados |
| Confidencial | Datos sensibles de negocio | Facturación, márgenes, contratos | Data Owners + CEO |
| Restringido | Datos personales protegidos por Ley 1581 | NIT, teléfono, email, dirección de persona natural | Solo con consentimiento explícito |

### 6.2 Controles de Acceso

| Rol | Público | Interno | Confidencial | Restringido |
|-----|---------|---------|--------------|-------------|
| CEO | ✅ Lectura/Escritura | ✅ Lectura/Escritura | ✅ Lectura/Escritura | ✅ Lectura |
| Data Owner | ✅ Lectura/Escritura | ✅ Lectura/Escritura | ✅ Lectura | ✅ Lectura (su dominio) |
| Data Steward | ✅ Lectura/Escritura | ✅ Lectura/Escritura | ❌ | ✅ Lectura (su dominio) |
| Data Engineer | ✅ Lectura | ✅ Lectura/Escritura | ❌ | ❌ (datos anonimizados) |
| Data Consumer | ✅ Lectura | ✅ Lectura (dashboards) | ❌ | ❌ |

### 6.3 Cumplimiento Legal — Ley 1581 de 2012

| Requisito | Implementación en TransCarga |
|-----------|------------------------------|
| Consentimiento | Todo cliente PYME firma autorización de tratamiento de datos al registrarse |
| Finalidad | Los datos se usan exclusivamente para logística y comunicación del servicio |
| Acceso y rectificación | El portal de clientes permite ver y corregir sus datos personales |
| Eliminación | Clientes inactivos por 2+ años: datos personales anonimizados automáticamente |
| Responsable del tratamiento | CEO de TransCarga (registrado ante la SIC) |
| Encargado del tratamiento | Data Engineer (maneja datos bajo instrucciones del responsable) |

---

## 7. Linaje de Datos (Data Lineage)

### 7.1 Flujo de Datos General

```
FUENTES                    INGESTA              ALMACENAMIENTO         PROCESAMIENTO          CONSUMO
─────────────────────────────────────────────────────────────────────────────────────────────────────

Portal web ──────┐
                 │
App conductor ───┤
                 ├──→ FastAPI ──→ PostgreSQL ──→ ETL (Python) ──→ Datos limpios ──→ Dashboards
E-commerce API ──┤         │       (raw)          (notebooks)       (processed)       (Power BI)
                 │         │
GPS vehículos ───┤         └──→ Data Lake ──→ Databricks ──→ Modelos ──→ Optimización
                 │              (S3/Azure)     (Spark)        (ML)        de rutas
Datos abiertos ──┘              (raw)
(DIVIPOLA, IDEAM,
 INVIAS, MinMinas)
```

### 7.2 Trazabilidad por Dataset

| Dataset | Fuente Original | Transformaciones | Destino Final | Responsable |
|---------|-----------------|------------------|---------------|-------------|
| Clientes | Portal web / manual | Validación NIT, geocodificación, deduplicación | PostgreSQL → Dashboard comercial | Data Steward Comercial |
| Pedidos | Portal web / API e-commerce | Validación dirección, asignación de ruta | PostgreSQL → TMS → Dashboard operativo | Data Steward Operaciones |
| GPS | Dispositivos en vehículos | Limpieza de outliers, interpolación, agregación | Data Lake → Modelo de rutas | Data Engineer |
| Tráfico | Datos Abiertos Medellín | Normalización horaria, merge con rutas | Data Lake → Modelo de rutas | Data Engineer |
| Combustible | MinMinas / Datos.gov.co | Normalización por departamento y fecha | PostgreSQL → Cálculo de costos | Data Engineer |
| Peajes | INVIAS / Datos.gov.co | Geocodificación de peajes, cálculo por ruta | PostgreSQL → Cálculo de costos | Data Engineer |
| División política | DIVIPOLA / IGAC | Estandarización de nombres de municipios | PostgreSQL → Validación de direcciones | Data Engineer |

---

## 8. Estándares y Convenciones

### 8.1 Nomenclatura

| Elemento | Convención | Ejemplo |
|----------|------------|---------|
| Tablas | snake_case, singular | `cliente`, `pedido`, `ruta` |
| Campos | snake_case | `fecha_creacion`, `peso_kg` |
| IDs | UUID v4 | `a1b2c3d4-e5f6-7890-abcd-ef1234567890` |
| Fechas | ISO 8601 | `2026-05-10T14:30:00` |
| Moneda | COP, sin decimales para valores grandes | `85000` (no `$85.000,00`) |
| Coordenadas | Decimal, 6 dígitos | `6.244203`, `-75.581211` |
| Booleanos | true/false (no 0/1, no sí/no) | `true` |
| Nulos | NULL explícito, nunca strings vacíos | `NULL` (no `""`, no `"N/A"`) |

### 8.2 Estándares de Código (Python)

| Regla | Detalle |
|-------|---------|
| Estilo | PEP 8 + Black formatter |
| Docstrings | Obligatorios en funciones públicas (Google style) |
| Type hints | Obligatorios en parámetros y retornos |
| Tests | Mínimo 1 test por función de limpieza |
| Versionamiento | Git con commits descriptivos en español |
| Branch strategy | main (producción) + develop (desarrollo) + feature/* (por tarea) |

### 8.3 Estándares de Notebooks

| Regla | Detalle |
|-------|---------|
| Estructura | Título → Objetivo → Imports → Datos → Análisis → Conclusiones |
| Markdown | Cada celda de código precedida por una celda markdown explicando qué hace |
| Outputs | Los notebooks se suben con los outputs ejecutados (no vacíos) |
| Reproducibilidad | Paths relativos, requirements.txt actualizado, semillas fijas para aleatoriedad |

---

## 9. Gestión de Incidentes de Datos

| Severidad | Descripción | Ejemplo | SLA de resolución | Escalación |
|-----------|-------------|---------|-------------------|------------|
| Crítica | Datos corruptos o perdidos que afectan operación | Pipeline ETL falla y no se procesan pedidos del día | 2 horas | Data Engineer → Data Owner → CEO |
| Alta | Datos incorrectos que afectan decisiones | Dashboard muestra KPIs erróneos | 8 horas | Data Steward → Data Owner |
| Media | Datos incompletos que no bloquean operación | 10% de pedidos sin coordenadas | 24 horas | Data Steward |
| Baja | Inconsistencias menores | Nombres de cliente con mayúsculas inconsistentes | 1 semana | Data Steward (próximo ciclo de limpieza) |

---

## 10. Plan de Implementación del Gobierno

| Fase | Actividad | Responsable | Plazo |
|------|-----------|-------------|-------|
| 1 | Aprobar este documento como marco de gobierno | CEO | Semana 1 |
| 2 | Asignar Data Owners y Data Stewards formalmente | CEO + Gerentes | Semana 2 |
| 3 | Implementar validaciones de calidad en el pipeline ETL | Data Engineer | Semanas 2-4 |
| 4 | Crear dashboard de métricas de calidad de datos | Data Engineer | Semanas 4-6 |
| 5 | Capacitar a Data Consumers en uso de dashboards | Data Stewards | Semanas 6-8 |
| 6 | Primera auditoría de calidad de datos | Data Owner + Steward | Mes 3 |
| 7 | Revisión y actualización del marco de gobierno | Todos los roles | Cada trimestre |

---

*Documento preparado como primer borrador del gobierno de datos — Universidad Pontificia Bolivariana, Data Office Strategy, 2026.*
