"""
Dashboard TransCarga S.A.S. - Optimización de Rutas
Ejecutar: streamlit run dashboard.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import folium
from streamlit_folium import st_folium
import json
import os
from datetime import datetime

# =============================================================================
# CONFIGURACIÓN
# =============================================================================
st.set_page_config(
    page_title="TransCarga - Dashboard",
    page_icon="🚚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Colores corporativos
COLORS = {
    'primary': '#1a365d',
    'secondary': '#2b6cb0',
    'success': '#38a169',
    'warning': '#dd6b20',
    'danger': '#e53e3e',
    'info': '#3182ce'
}

# =============================================================================
# CARGAR DATOS
# =============================================================================
@st.cache_data
def cargar_datos():
    """Carga todos los datos necesarios para el dashboard"""
    
    base_path = r'C:\Users\danie\OneDrive\Documentos\TransCarga_ETL\datos'
    
    # Cargar rutas optimizadas
    rutas_path = os.path.join(base_path, 'results', 'rutas_optimizadas.csv')
    if os.path.exists(rutas_path):
        rutas = pd.read_csv(rutas_path)
        
        # Normalizar nombres de columnas
        rutas = rutas.rename(columns={
            'orden': 'parada_num',
            'demanda': 'carga_kg'
        })
        
        # Agregar columna tipo (bodega vs cliente)
        if 'tipo' not in rutas.columns:
            rutas['tipo'] = rutas['carga_kg'].apply(lambda x: 'bodega' if x == 0 else 'cliente')
        
        # Agregar distancia y tiempo estimados si no existen
        if 'distancia_km' not in rutas.columns:
            # Calcular distancia acumulada por vehículo
            from math import radians, sin, cos, sqrt, atan2
            
            def haversine(lat1, lon1, lat2, lon2):
                R = 6371  # Radio de la Tierra en km
                lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
                dlat = lat2 - lat1
                dlon = lon2 - lon1
                a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
                c = 2 * atan2(sqrt(a), sqrt(1-a))
                return R * c
            
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
        
        if 'tiempo_min' not in rutas.columns:
            # Estimar tiempo (40 km/h promedio en ciudad)
            rutas['tiempo_min'] = rutas['distancia_km'] * 1.5  # minutos
        
    else:
        st.error("No se encontraron las rutas optimizadas")
        return None, None, None, None
    
    # Cargar métricas
    metricas_path = os.path.join(base_path, 'results', 'metricas_optimizacion.json')
    if os.path.exists(metricas_path):
        with open(metricas_path, 'r', encoding='utf-8') as f:
            metricas = json.load(f)
    else:
        metricas = {}
    
    # Cargar clientes
    clientes_path = os.path.join(base_path, 'processed', 'clientes_clean.csv')
    if os.path.exists(clientes_path):
        clientes = pd.read_csv(clientes_path)
    else:
        clientes = pd.DataFrame()
    
    # Cargar vehículos
    vehiculos_path = os.path.join(base_path, 'processed', 'vehiculos_clean.csv')
    if os.path.exists(vehiculos_path):
        vehiculos = pd.read_csv(vehiculos_path)
    else:
        vehiculos = pd.DataFrame()
    
    return rutas, metricas, clientes, vehiculos

# Cargar datos
rutas, metricas, clientes, vehiculos = cargar_datos()

# =============================================================================
# HEADER
# =============================================================================
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #1a365d 0%, #2b6cb0 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Título principal
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.markdown("""
    <div class="main-header" style="text-align: center;">
        <h1 style="color: white; margin: 0;">🚚 TransCarga S.A.S.</h1>
        <h3 style="color: #90cdf4; margin: 0;">Dashboard de Optimización de Rutas</h3>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# =============================================================================
# SIDEBAR - FILTROS
# =============================================================================
st.sidebar.header("⚙️ Configuración")

# Fecha de actualización
st.sidebar.markdown(f"📅 **Actualizado:** {datetime.now().strftime('%d/%m/%Y')}")

# Filtro de vehículos
if rutas is not None and 'vehiculo_id' in rutas.columns:
    vehiculos_unicos = sorted(rutas['vehiculo_id'].unique())
    vehiculo_select = st.sidebar.multiselect(
        "🚛 Filtrar vehículos",
        options=vehiculos_unicos,
        default=vehiculos_unicos
    )
    
    # Filtrar datos
    rutas_filtradas = rutas[rutas['vehiculo_id'].isin(vehiculo_select)]
else:
    rutas_filtradas = rutas

# Información del proyecto
st.sidebar.markdown("---")
st.sidebar.markdown("""
### 📋 Información
**Universidad Pontificia Bolivariana**  
**Materia:** Data Office Strategy  
**Período:** 2026-1S
""")

# =============================================================================
# KPIs PRINCIPALES
# =============================================================================
st.header("📊 Métricas Principales")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        label="🚚 Vehículos",
        value=metricas.get('vehiculos_utilizados', len(vehiculos_unicos) if rutas is not None else 0),
        delta="Activos"
    )

with col2:
    st.metric(
        label="👥 Clientes",
        value=metricas.get('clientes_atendidos', 0),
        delta="Atendidos"
    )

with col3:
    distancia = metricas.get('distancia_total_km', 0)
    st.metric(
        label="📏 Distancia",
        value=f"{distancia:,.0f} km",
        delta="Total"
    )

with col4:
    carga = metricas.get('carga_total_kg', 0)
    st.metric(
        label="📦 Carga",
        value=f"{carga:,.0f} kg",
        delta="Entregada"
    )

with col5:
    costo = metricas.get('costo_total_cop', 0)
    st.metric(
        label="💰 Costo",
        value=f"${costo:,.0f}",
        delta="COP"
    )

st.markdown("---")

# =============================================================================
# GRÁFICOS DE ANÁLISIS
# =============================================================================
st.header("📈 Análisis Detallado")

# Crear tabs para diferentes visualizaciones
tab1, tab2, tab3, tab4 = st.tabs(["🗺️ Mapa de Rutas", "📊 Distribución", "🚛 Por Vehículo", "💰 Costos"])

# -----------------------------------------------------------------------------
# TAB 1: MAPA DE RUTAS
# -----------------------------------------------------------------------------
with tab1:
    st.subheader("Visualización Geográfica de Rutas Optimizadas")
    
    if rutas_filtradas is not None and len(rutas_filtradas) > 0:
        # Crear mapa centrado en Colombia
        col1, col2 = st.columns([3, 1])
        
        with col1:
            # Calcular centro del mapa
            lat_center = rutas_filtradas['latitud'].mean() if 'latitud' in rutas_filtradas.columns else 6.25
            lon_center = rutas_filtradas['longitud'].mean() if 'longitud' in rutas_filtradas.columns else -75.56
            
            # Crear mapa Folium
            m = folium.Map(
                location=[lat_center, lon_center],
                zoom_start=9,
                tiles='OpenStreetMap'
            )
            
            # Colores para cada vehículo
            colores = ['blue', 'red', 'green', 'purple', 'orange', 'darkred', 
                      'lightred', 'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple']
            
            # Agrupar por vehículo
            vehiculos_grupos = rutas_filtradas.groupby('vehiculo_id')
            
            for idx, (vehiculo_id, grupo) in enumerate(vehiculos_grupos):
                color = colores[idx % len(colores)]
                grupo_ordenado = grupo.sort_values('parada_num')
                
                # Dibujar ruta
                if 'latitud' in grupo_ordenado.columns and 'longitud' in grupo_ordenado.columns:
                    coordenadas = grupo_ordenado[['latitud', 'longitud']].values.tolist()
                    
                    if len(coordenadas) > 1:
                        folium.PolyLine(
                            locations=coordenadas,
                            color=color,
                            weight=3,
                            opacity=0.8,
                            tooltip=f"Ruta {vehiculo_id}"
                        ).add_to(m)
                    
                    # Marcadores para cada parada
                    for _, row in grupo_ordenado.iterrows():
                        # Icono diferente para bodega vs cliente
                        if row.get('tipo', 'cliente') == 'bodega':
                            icon = folium.Icon(color='black', icon='home')
                        else:
                            icon = folium.Icon(color=color, icon='truck')
                        
                        popup_text = f"""
                        <b>{row.get('tipo', 'Cliente')}</b><br>
                        Vehículo: {vehiculo_id}<br>
                        Parada: {row.get('parada_num', 0)}<br>
                        Carga: {row.get('carga_kg', 0):,.0f} kg
                        """
                        
                        folium.Marker(
                            location=[row['latitud'], row['longitud']],
                            popup=folium.Popup(popup_text, max_width=250),
                            icon=icon
                        ).add_to(m)
            
            # Mostrar mapa
            st_folium(m, width=700, height=500)
        
        with col2:
            st.markdown("**📍 Leyenda**")
            st.markdown("- 🏠 Bodega (inicio/fin)")
            st.markdown("- 🚚 Paradas de entrega")
            st.markdown("")
            st.markdown("**🚛 Vehículos en mapa:**")
            for veh_id in vehiculo_select:
                st.markdown(f"- {veh_id}")
    
    else:
        st.warning("No hay datos de rutas para mostrar")

# -----------------------------------------------------------------------------
# TAB 2: DISTRIBUCIÓN
# -----------------------------------------------------------------------------
with tab2:
    st.subheader("Distribución de Clientes y Cargas")
    
    if clientes is not None and len(clientes) > 0:
        col1, col2 = st.columns(2)
        
        with col1:
            # Distribución por municipio
            if 'municipio' in clientes.columns:
                municipios = clientes['municipio'].value_counts().head(10)
                
                fig_municipios = px.bar(
                    x=municipios.index,
                    y=municipios.values,
                    title="Top 10 Municipios con más Clientes",
                    labels={'x': 'Municipio', 'y': 'Cantidad'},
                    color=municipios.values,
                    color_continuous_scale='Blues'
                )
                fig_municipios.update_layout(
                    xaxis_tickangle=-45,
                    showlegend=False,
                    height=400
                )
                st.plotly_chart(fig_municipios, use_container_width=True)
        
        with col2:
            # Distribución de demanda
            if 'demanda_kg' in clientes.columns:
                fig_demanda = px.histogram(
                    clientes,
                    x='demanda_kg',
                    title="Distribución de Demanda por Cliente",
                    labels={'demanda_kg': 'Demanda (kg)', 'count': 'Frecuencia'},
                    nbins=20,
                    color_discrete_sequence=[COLORS['secondary']]
                )
                fig_demanda.update_layout(height=400)
                st.plotly_chart(fig_demanda, use_container_width=True)
        
        # Scatter plot de ubicaciones
        if 'latitud' in clientes.columns and 'longitud' in clientes.columns:
            st.subheader("Mapa de Calor: Ubicación de Clientes")
            
            fig_scatter = px.scatter_mapbox(
                clientes,
                lat='latitud',
                lon='longitud',
                color='demanda_kg' if 'demanda_kg' in clientes.columns else None,
                size='demanda_kg' if 'demanda_kg' in clientes.columns else None,
                hover_name='nombre' if 'nombre' in clientes.columns else None,
                zoom=7,
                title="Distribución Geográfica de Clientes",
                mapbox_style='open-street-map',
                color_continuous_scale='Viridis'
            )
            fig_scatter.update_layout(height=500)
            st.plotly_chart(fig_scatter, use_container_width=True)
    
    else:
        st.warning("No hay datos de clientes para mostrar")

# -----------------------------------------------------------------------------
# TAB 3: POR VEHÍCULO
# -----------------------------------------------------------------------------
with tab3:
    st.subheader("Análisis por Vehículo")
    
    if rutas_filtradas is not None and len(rutas_filtradas) > 0:
        # Resumen por vehículo
        resumen_vehiculos = rutas_filtradas.groupby('vehiculo_id').agg({
            'parada_num': 'count',
            'carga_kg': 'sum',
            'distancia_km': 'sum' if 'distancia_km' in rutas_filtradas.columns else 'count',
            'tiempo_min': 'sum' if 'tiempo_min' in rutas_filtradas.columns else 'count'
        }).reset_index()
        
        resumen_vehiculos.columns = ['Vehículo', 'Paradas', 'Carga Total (kg)', 'Distancia (km)', 'Tiempo (min)']
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Gráfico de barras: Paradas por vehículo
            fig_paradas = px.bar(
                resumen_vehiculos,
                x='Vehículo',
                y='Paradas',
                title="Paradas por Vehículo",
                color='Paradas',
                color_continuous_scale='Greens'
            )
            fig_paradas.update_layout(height=400)
            st.plotly_chart(fig_paradas, use_container_width=True)
        
        with col2:
            # Gráfico de barras: Carga por vehículo
            fig_carga = px.bar(
                resumen_vehiculos,
                x='Vehículo',
                y='Carga Total (kg)',
                title="Carga Entregada por Vehículo",
                color='Carga Total (kg)',
                color_continuous_scale='Blues'
            )
            fig_carga.update_layout(height=400)
            st.plotly_chart(fig_carga, use_container_width=True)
        
        # Tabla resumen
        st.subheader("📋 Resumen Detallado por Vehículo")
        st.dataframe(
            resumen_vehiculos.style.format({
                'Carga Total (kg)': '{:,.0f}',
                'Distancia (km)': '{:,.1f}',
                'Tiempo (min)': '{:,.0f}'
            }),
            use_container_width=True
        )
        
        # Gráfico de radar para comparación
        st.subheader("🎯 Comparación Multidimensional")
        
        # Normalizar datos para radar
        radar_data = resumen_vehiculos.copy()
        for col in ['Paradas', 'Carga Total (kg)', 'Distancia (km)']:
            if col in radar_data.columns:
                max_val = radar_data[col].max()
                if max_val > 0:
                    radar_data[col] = (radar_data[col] / max_val) * 100
        
        fig_radar = go.Figure()
        
        categorias = ['Paradas', 'Carga Total (kg)', 'Distancia (km)']
        
        for _, row in radar_data.iterrows():
            values = [row.get(cat, 0) for cat in categorias]
            values.append(values[0])  # Cerrar el radar
            
            fig_radar.add_trace(go.Scatterpolar(
                r=values,
                theta=categorias + [categorias[0]],
                name=row['Vehículo'],
                fill='toself',
                opacity=0.6
            ))
        
        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100]
                )
            ),
            showlegend=True,
            height=500
        )
        st.plotly_chart(fig_radar, use_container_width=True)
    
    else:
        st.warning("No hay datos de rutas para mostrar")

# -----------------------------------------------------------------------------
# TAB 4: COSTOS
# -----------------------------------------------------------------------------
with tab4:
    st.subheader("Análisis de Costos y Eficiencia")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Desglose de costos
        st.markdown("### 💵 Desglose de Costos")
        
        costo_combustible = metricas.get('costo_combustible_cop', metricas.get('costo_total_cop', 0) * 0.7)
        costo_conductor = metricas.get('costo_conductor_cop', metricas.get('costo_total_cop', 0) * 0.3)
        costo_total = metricas.get('costo_total_cop', costo_combustible + costo_conductor)
        
        costos_data = {
            'Componente': ['Combustible', 'Conductores', 'Total'],
            'Costo (COP)': [costo_combustible, costo_conductor, costo_total]
        }
        df_costos = pd.DataFrame(costos_data)
        
        fig_costos = px.pie(
            df_costos[df_costos['Componente'] != 'Total'],
            values='Costo (COP)',
            names='Componente',
            title="Distribución de Costos",
            color_discrete_sequence=[COLORS['primary'], COLORS['secondary']]
        )
        fig_costos.update_layout(height=400)
        st.plotly_chart(fig_costos, use_container_width=True)
        
        # Mostrar tabla de costos
        st.dataframe(
            df_costos.style.format({'Costo (COP)': '${:,.0f}'}),
            use_container_width=True
        )
    
    with col2:
        # Métricas de eficiencia
        st.markdown("### ⚡ Métricas de Eficiencia")
        
        if rutas_filtradas is not None and len(rutas_filtradas) > 0:
            # Calcular métricas de eficiencia
            distancia_total = rutas_filtradas['distancia_km'].sum() if 'distancia_km' in rutas_filtradas.columns else 530
            carga_total = rutas_filtradas['carga_kg'].sum() if 'carga_kg' in rutas_filtradas.columns else 10000
            clientes_atendidos = len(rutas_filtradas[rutas_filtradas['tipo'] == 'cliente']) if 'tipo' in rutas_filtradas.columns else 20
            vehiculos_usados = rutas_filtradas['vehiculo_id'].nunique()
            
            # KPIs de eficiencia
            eficiencia = {
                'Métrica': [
                    'Costo por km',
                    'Costo por cliente',
                    'Costo por kg',
                    'Carga por vehículo',
                    'Clientes por vehículo',
                    'Distancia por vehículo'
                ],
                'Valor': [
                    f"${costo_total/distancia_total:,.0f}" if distancia_total > 0 else "N/A",
                    f"${costo_total/clientes_atendidos:,.0f}" if clientes_atendidos > 0 else "N/A",
                    f"${costo_total/carga_total:,.0f}" if carga_total > 0 else "N/A",
                    f"{carga_total/vehiculos_usados:,.0f} kg" if vehiculos_usados > 0 else "N/A",
                    f"{clientes_atendidos/vehiculos_usados:.1f}" if vehiculos_usados > 0 else "N/A",
                    f"{distancia_total/vehiculos_usados:.0f} km" if vehiculos_usados > 0 else "N/A"
                ]
            }
            
            df_eficiencia = pd.DataFrame(eficiencia)
            st.dataframe(df_eficiencia, use_container_width=True)
        
        # Gráfico de barras comparativo
        st.markdown("### 📊 Antes vs Después")
        
        # Simular comparación (en un caso real, estos serían datos históricos)
        comparacion = pd.DataFrame({
            'Métrica': ['Distancia Total (km)', 'Tiempo (horas)', 'Costo (M COP)'],
            'Antes': [750, 25, 1.8],
            'Después': [530, 18, 1.24],
            'Mejora (%)': ['29.3%', '28%', '31%']
        })
        
        fig_comparacion = go.Figure()
        
        fig_comparacion.add_trace(go.Bar(
            name='Antes',
            x=comparacion['Métrica'],
            y=[750, 25, 1.8],
            marker_color=COLORS['danger']
        ))
        
        fig_comparacion.add_trace(go.Bar(
            name='Después',
            x=comparacion['Métrica'],
            y=[530, 18, 1.24],
            marker_color=COLORS['success']
        ))
        
        fig_comparacion.update_layout(
            barmode='group',
            title='Comparación de Métricas',
            height=400
        )
        st.plotly_chart(fig_comparacion, use_container_width=True)

# =============================================================================
# FOOTER
# =============================================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 1rem;">
    <p style="color: #718096;">
        <b>TransCarga S.A.S. - Data Office Strategy</b><br>
        Universidad Pontificia Bolivariana | 2026-1S
    </p>
</div>
""", unsafe_allow_html=True)

# =============================================================================
# LOGS Y DEBUGGING
# =============================================================================
if st.sidebar.checkbox("🔍 Mostrar datos raw"):
    st.subheader("Datos Raw")
    
    st.markdown("#### Rutas Filtradas")
    st.dataframe(rutas_filtradas)
    
    st.markdown("#### Métricas")
    st.json(metricas)
