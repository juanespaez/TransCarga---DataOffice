"""
EDA Simplificado - TransCarga S.A.S.
Genera visualizaciones sin emojis para compatibilidad con Windows CMD
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import json
import warnings
warnings.filterwarnings('ignore')

# Configuracion
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 11

COLORS = {
    'primary': '#1a365d',
    'secondary': '#2b6cb0',
    'success': '#38a169',
    'warning': '#dd6b20',
}

base_path = r'C:\Users\danie\OneDrive\Documentos\TransCarga_ETL\datos'
img_path = r'C:\Users\danie\OneDrive\Documentos\TransCarga_ETL\img'
doc_path = r'C:\Users\danie\OneDrive\Documentos\TransCarga_ETL\documentacion'

print("=" * 60)
print("EDA - TRANSCARGA S.A.S.")
print("=" * 60)

# Cargar datos
clientes = pd.read_csv(f'{base_path}/processed/clientes_clean.csv')
vehiculos = pd.read_csv(f'{base_path}/processed/vehiculos_clean.csv')
combustible = pd.read_csv(f'{base_path}/processed/combustible_clean.csv')
rutas = pd.read_csv(f'{base_path}/results/rutas_optimizadas.csv')

print(f"\nDatos cargados:")
print(f"  - Clientes: {len(clientes)}")
print(f"  - Vehiculos: {len(vehiculos)}")
print(f"  - Combustible: {len(combustible)}")
print(f"  - Rutas: {len(rutas)}")

# ============================================================================
# 1. CLIENTES POR DEPARTAMENTO
# ============================================================================
print("\n[1/8] Generando grafico de clientes por departamento...")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
dept_counts = clientes['departamento'].value_counts()
colors = [COLORS['primary'], COLORS['secondary']]

axes[0].bar(dept_counts.index, dept_counts.values, color=colors, edgecolor='black')
axes[0].set_title('Clientes por Departamento', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Departamento')
axes[0].set_ylabel('Numero de Clientes')
for i, v in enumerate(dept_counts.values):
    axes[0].text(i, v + 2, str(v), ha='center', fontweight='bold')

axes[1].pie(dept_counts.values, labels=dept_counts.index, autopct='%1.1f%%', colors=colors, startangle=90)
axes[1].set_title('Proporcion de Clientes', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig(f'{img_path}/eda_clientes_departamento.png', dpi=150, bbox_inches='tight')
plt.close()
print("  OK: eda_clientes_departamento.png")

# ============================================================================
# 2. TOP 15 MUNICIPIOS
# ============================================================================
print("\n[2/8] Generando grafico de municipios...")

muni_counts = clientes['municipio'].value_counts().head(15)
fig, ax = plt.subplots(figsize=(14, 7))
bars = ax.barh(muni_counts.index[::-1], muni_counts.values[::-1], color=COLORS['secondary'], edgecolor='black')
ax.set_title('Top 15 Municipios con Mas Clientes', fontsize=14, fontweight='bold')
ax.set_xlabel('Numero de Clientes')
for bar, val in zip(bars, muni_counts.values[::-1]):
    ax.text(val + 0.5, bar.get_y() + bar.get_height()/2, str(val), va='center', fontweight='bold')
plt.tight_layout()
plt.savefig(f'{img_path}/eda_clientes_municipios.png', dpi=150, bbox_inches='tight')
plt.close()
print("  OK: eda_clientes_municipios.png")

# ============================================================================
# 3. DISTRIBUCION DE DEMANDA
# ============================================================================
print("\n[3/8] Generando graficos de demanda...")

# Buscar columna de demanda
demanda_col = 'capacidad_kg' if 'capacidad_kg' in clientes.columns else 'demanda_kg'

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Histograma
axes[0, 0].hist(clientes[demanda_col], bins=30, color=COLORS['primary'], edgecolor='black', alpha=0.7)
axes[0, 0].set_title('Histograma de Demanda', fontsize=12, fontweight='bold')
axes[0, 0].set_xlabel('Demanda (kg)')
axes[0, 0].set_ylabel('Frecuencia')
axes[0, 0].axvline(clientes[demanda_col].mean(), color='red', linestyle='--', linewidth=2, label=f'Media: {clientes[demanda_col].mean():.0f} kg')
axes[0, 0].legend()

# Boxplot
axes[0, 1].boxplot(clientes[demanda_col], vert=True, patch_artist=True, boxprops=dict(facecolor=COLORS['secondary']))
axes[0, 1].set_title('Boxplot de Demanda', fontsize=12, fontweight='bold')
axes[0, 1].set_ylabel('Demanda (kg)')

# Por departamento
for dept in clientes['departamento'].unique():
    subset = clientes[clientes['departamento'] == dept]
    axes[1, 0].hist(subset[demanda_col], bins=20, alpha=0.6, label=dept, edgecolor='black')
axes[1, 0].set_title('Demanda por Departamento', fontsize=12, fontweight='bold')
axes[1, 0].set_xlabel('Demanda (kg)')
axes[1, 0].set_ylabel('Frecuencia')
axes[1, 0].legend()

# Curva acumulada
demanda_acum = clientes[demanda_col].sort_values().cumsum()
demanda_acum_pct = demanda_acum / demanda_acum.max() * 100
axes[1, 1].plot(range(len(demanda_acum)), demanda_acum_pct, color=COLORS['success'], linewidth=2)
axes[1, 1].fill_between(range(len(demanda_acum)), demanda_acum_pct, alpha=0.3, color=COLORS['success'])
axes[1, 1].set_title('Demanda Acumulada (Curva ABC)', fontsize=12, fontweight='bold')
axes[1, 1].set_xlabel('Clientes ordenados por demanda')
axes[1, 1].set_ylabel('Demanda Acumulada (%)')
axes[1, 1].axhline(80, color='red', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.savefig(f'{img_path}/eda_demanda_distribucion.png', dpi=150, bbox_inches='tight')
plt.close()
print("  OK: eda_demanda_distribucion.png")

# ============================================================================
# 4. DISTRIBUCION GEOGRAFICA
# ============================================================================
print("\n[4/8] Generando mapa geografico...")

fig, ax = plt.subplots(figsize=(12, 10))
for dept, color in zip(clientes['departamento'].unique(), [COLORS['primary'], COLORS['secondary']]):
    subset = clientes[clientes['departamento'] == dept]
    ax.scatter(subset['longitud'], subset['latitud'], c=color, label=dept, alpha=0.6, s=50, edgecolor='white')

ax.set_title('Distribucion Geografica de Clientes', fontsize=14, fontweight='bold')
ax.set_xlabel('Longitud')
ax.set_ylabel('Latitud')
ax.legend(title='Departamento')
ax.grid(True, alpha=0.3)
ax.annotate('Medellin (Bodega)', xy=(-75.56, 6.25), fontsize=10, ha='center', color='red', fontweight='bold')
ax.annotate('Cali (Bodega)', xy=(-76.52, 3.45), fontsize=10, ha='center', color='red', fontweight='bold')

plt.tight_layout()
plt.savefig(f'{img_path}/eda_clientes_geografico.png', dpi=150, bbox_inches='tight')
plt.close()
print("  OK: eda_clientes_geografico.png")

# ============================================================================
# 5. VEHICULOS POR TIPO
# ============================================================================
print("\n[5/8] Generando graficos de vehiculos...")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
tipo_counts = vehiculos['tipo'].value_counts()
colors_tipos = [COLORS['primary'], COLORS['secondary'], COLORS['success'], COLORS['warning']]

axes[0].bar(tipo_counts.index, tipo_counts.values, color=colors_tipos[:len(tipo_counts)], edgecolor='black')
axes[0].set_title('Vehiculos por Tipo', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Tipo de Vehiculo')
axes[0].set_ylabel('Cantidad')
for i, v in enumerate(tipo_counts.values):
    axes[0].text(i, v + 1, str(v), ha='center', fontweight='bold')

axes[1].pie(tipo_counts.values, labels=tipo_counts.index, autopct='%1.1f%%', colors=colors_tipos[:len(tipo_counts)], startangle=90)
axes[1].set_title('Proporcion por Tipo', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig(f'{img_path}/eda_vehiculos_tipo.png', dpi=150, bbox_inches='tight')
plt.close()
print("  OK: eda_vehiculos_tipo.png")

# ============================================================================
# 6. CAPACIDAD DE VEHICULOS
# ============================================================================
print("\n[6/8] Generando graficos de capacidad...")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

capacidad_col = 'capacidad_kg' if 'capacidad_kg' in vehiculos.columns else vehiculos.select_dtypes(include=[np.number]).columns[-1]

vehiculos.boxplot(column=capacidad_col, by='tipo', ax=axes[0])
axes[0].set_title('Capacidad por Tipo de Vehiculo', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Tipo de Vehiculo')
axes[0].set_ylabel('Capacidad (kg)')
plt.suptitle('')

axes[1].hist(vehiculos[capacidad_col], bins=20, color=COLORS['success'], edgecolor='black', alpha=0.7)
axes[1].set_title('Distribucion de Capacidad', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Capacidad (kg)')
axes[1].set_ylabel('Frecuencia')
axes[1].axvline(vehiculos[capacidad_col].mean(), color='red', linestyle='--', linewidth=2, label=f'Media: {vehiculos[capacidad_col].mean():.0f} kg')
axes[1].legend()

plt.tight_layout()
plt.savefig(f'{img_path}/eda_vehiculos_capacidad.png', dpi=150, bbox_inches='tight')
plt.close()
print("  OK: eda_vehiculos_capacidad.png")

# ============================================================================
# 7. PRECIOS DE COMBUSTIBLE
# ============================================================================
print("\n[7/8] Generando graficos de combustible...")

# Normalizar nombre de columna si existe
if 'departamentonombre' in combustible.columns:
    combustible['departamento'] = combustible['departamentonombre']
elif 'departamento' not in combustible.columns:
    combustible['departamento'] = 'Colombia'

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].hist(combustible['precio'], bins=30, color=COLORS['warning'], edgecolor='black', alpha=0.7)
axes[0].set_title('Distribucion de Precios de Combustible', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Precio (COP/galon)')
axes[0].set_ylabel('Frecuencia')
media_precio = combustible['precio'].mean()
axes[0].axvline(media_precio, color='red', linestyle='--', linewidth=2, label=f'Media: ${media_precio:,.0f}')
axes[0].legend()

# Usar seaborn para boxplot mas robusto
if 'departamento' in combustible.columns:
    combustible.boxplot(column='precio', by='departamento', ax=axes[1])
    axes[1].set_title('Precios por Departamento', fontsize=12, fontweight='bold')
    axes[1].set_xlabel('Departamento')
    axes[1].set_ylabel('Precio (COP/galon)')
    plt.suptitle('')
else:
    axes[1].hist(combustible['precio'], bins=30, color=COLORS['secondary'], edgecolor='black', alpha=0.7)
    axes[1].set_title('Distribucion de Precios', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.savefig(f'{img_path}/eda_combustible.png', dpi=150, bbox_inches='tight')
plt.close()
print("  OK: eda_combustible.png")

# ============================================================================
# 8. RUTAS OPTIMIZADAS
# ============================================================================
print("\n[8/8] Generando graficos de rutas...")

rutas_norm = rutas.rename(columns={'orden': 'parada_num', 'demanda': 'carga_kg'})
resumen = rutas_norm.groupby('vehiculo_id').agg({'parada_num': 'count', 'carga_kg': 'sum'}).reset_index()
resumen.columns = ['Vehiculo', 'Paradas', 'Carga_Total']

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

axes[0].bar(resumen['Vehiculo'].astype(str), resumen['Paradas'], color=COLORS['primary'], edgecolor='black')
axes[0].set_title('Paradas por Vehiculo', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Vehiculo')
axes[0].set_ylabel('Numero de Paradas')
for i, v in enumerate(resumen['Paradas']):
    axes[0].text(i, v + 0.3, str(v), ha='center', fontweight='bold')

axes[1].bar(resumen['Vehiculo'].astype(str), resumen['Carga_Total'], color=COLORS['success'], edgecolor='black')
axes[1].set_title('Carga Entregada por Vehiculo', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Vehiculo')
axes[1].set_ylabel('Carga (kg)')

plt.tight_layout()
plt.savefig(f'{img_path}/eda_rutas_vehiculos.png', dpi=150, bbox_inches='tight')
plt.close()
print("  OK: eda_rutas_vehiculos.png")

# ============================================================================
# GUARDAR RESUMEN
# ============================================================================
print("\n" + "=" * 60)
print("GUARDANDO RESUMEN...")
print("=" * 60)

eda_summary = {
    'fecha_analisis': pd.Timestamp.now().strftime('%Y-%m-%d %H:%M'),
    'clientes': {
        'total': len(clientes),
        'por_departamento': clientes['departamento'].value_counts().to_dict(),
        'demanda_media_kg': round(clientes[demanda_col].mean(), 2),
        'demanda_total_kg': int(clientes[demanda_col].sum())
    },
    'vehiculos': {
        'total': len(vehiculos),
        'por_tipo': vehiculos['tipo'].value_counts().to_dict(),
        'capacidad_media_kg': round(vehiculos[capacidad_col].mean(), 2),
        'capacidad_total_kg': int(vehiculos[capacidad_col].sum())
    },
    'combustible': {
        'precio_medio_cop': round(combustible['precio'].mean(), 2),
        'precio_min_cop': int(combustible['precio'].min()),
        'precio_max_cop': int(combustible['precio'].max())
    },
    'optimizacion': {
        'vehiculos_utilizados': int(rutas_norm['vehiculo_id'].nunique()),
        'clientes_atendidos': int(len(rutas_norm[rutas_norm['carga_kg'] > 0])),
        'carga_total_kg': int(rutas_norm['carga_kg'].sum())
    }
}

with open(f'{doc_path}/eda_summary.json', 'w', encoding='utf-8') as f:
    json.dump(eda_summary, f, indent=2, ensure_ascii=False)

print("\nResumen guardado en: documentacion/eda_summary.json")
print("\nGraficos generados en: img/")
print("  - eda_clientes_departamento.png")
print("  - eda_clientes_municipios.png")
print("  - eda_demanda_distribucion.png")
print("  - eda_clientes_geografico.png")
print("  - eda_vehiculos_tipo.png")
print("  - eda_vehiculos_capacidad.png")
print("  - eda_combustible.png")
print("  - eda_rutas_vehiculos.png")

print("\n" + "=" * 60)
print("EDA COMPLETADO EXITOSAMENTE")
print("=" * 60)
