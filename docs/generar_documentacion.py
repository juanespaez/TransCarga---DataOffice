"""
Generador de Documentacion PDF - TransCarga ETL
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.pdfgen import canvas
import os
from datetime import datetime

# Configuracion
OUTPUT_DIR = r'C:\Users\danie\OneDrive\Documentos\TransCarga_ETL\docs'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Colores
AZUL = HexColor('#1a365d')
AZUL_C = HexColor('#2b6cb0')
GRIS = HexColor('#4a5568')
VERDE = HexColor('#38a169')

def crear_portada(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(AZUL)
    canvas.rect(0, 0, letter[0], letter[1], fill=1)
    canvas.setStrokeColor(VERDE)
    canvas.setLineWidth(4)
    canvas.line(50, 500, letter[0]-50, 500)
    canvas.setFillColor(white)
    canvas.setFont('Helvetica-Bold', 36)
    canvas.drawCentredString(letter[0]/2, 600, "TransCarga S.A.S.")
    canvas.setFont('Helvetica-Bold', 24)
    canvas.drawCentredString(letter[0]/2, 550, "Data Office Strategy")
    canvas.setFillColor(HexColor('#90cdf4'))
    canvas.setFont('Helvetica', 18)
    canvas.drawCentredString(letter[0]/2, 480, "Documentacion Tecnica")
    canvas.drawCentredString(letter[0]/2, 455, "ETL Pipeline & Route Optimization")
    canvas.setFillColor(white)
    canvas.setFont('Helvetica', 12)
    canvas.drawCentredString(letter[0]/2, 200, f"Fecha: {datetime.now().strftime('%d/%m/%Y')}")
    canvas.drawCentredString(letter[0]/2, 50, "Vehicle Routing Problem con Google OR-Tools")
    canvas.restoreState()

def crear_header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFillColor(AZUL)
    canvas.rect(0, letter[1]-40, letter[0], 40, fill=1)
    canvas.setFillColor(white)
    canvas.setFont('Helvetica-Bold', 10)
    canvas.drawString(50, letter[1]-25, "TransCarga S.A.S. - Documentacion Tecnica")
    canvas.setFillColor(GRIS)
    canvas.setFont('Helvetica', 9)
    canvas.drawString(50, 30, f"Generado: {datetime.now().strftime('%Y-%m-%d')}")
    canvas.drawRightString(letter[0]-50, 30, f"Pagina {doc.page}")
    canvas.restoreState()

def crear_tabla(datos, col_widths, header_color=AZUL):
    table = Table(datos, colWidths=col_widths)
    style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), header_color),
        ('TEXTCOLOR', (0, 0), (-1, 0), white),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('TOPPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), HexColor('#f7fafc')),
        ('TEXTCOLOR', (0, 1), (-1, -1), black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('GRID', (0, 0), (-1, -1), 1, HexColor('#e2e8f0')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 1), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ])
    for i in range(1, len(datos)):
        if i % 2 == 0:
            style.add('BACKGROUND', (0, i), (-1, i), HexColor('#edf2f7'))
    table.setStyle(style)
    return table

def main():
    output_path = os.path.join(OUTPUT_DIR, 'TransCarga_ETL_Documentacion.pdf')
    doc = SimpleDocTemplate(output_path, pagesize=letter, rightMargin=50, leftMargin=50, topMargin=60, bottomMargin=50)
    styles = getSampleStyleSheet()
    
    styles.add(ParagraphStyle(name='Titulo1', parent=styles['Heading1'], fontSize=24, textColor=AZUL, spaceAfter=20, spaceBefore=30))
    styles.add(ParagraphStyle(name='Titulo2', parent=styles['Heading2'], fontSize=16, textColor=AZUL_C, spaceAfter=12, spaceBefore=20))
    styles.add(ParagraphStyle(name='Titulo3', parent=styles['Heading3'], fontSize=13, textColor=GRIS, spaceAfter=8, spaceBefore=15))
    styles.add(ParagraphStyle(name='Cuerpo', parent=styles['Normal'], fontSize=11, textColor=black, spaceAfter=8, alignment=TA_JUSTIFY, leading=14))
    styles.add(ParagraphStyle(name='Codigo', parent=styles['Code'], fontSize=9, textColor=HexColor('#2d3748'), backColor=HexColor('#edf2f7'), spaceAfter=10, leftIndent=20, leading=12))
    
    story = []
    
    # PORTADA
    story.append(PageBreak())
    
    # INDICE
    story.append(Paragraph("Indice de Contenidos", styles['Titulo1']))
    story.append(Spacer(1, 20))
    for item in ["1. Resumen Ejecutivo", "2. Arquitectura del Proyecto", "3. Pipeline ETL", "4. Modelo de Optimizacion VRP", "5. Herramientas y Tecnologias", "6. Datasets Utilizados", "7. Resultados", "8. Conclusiones"]:
        story.append(Paragraph(item, styles['Cuerpo']))
    story.append(PageBreak())
    
    # 1. RESUMEN
    story.append(Paragraph("1. Resumen Ejecutivo", styles['Titulo1']))
    story.append(Paragraph("Este documento presenta la documentacion tecnica del proyecto de optimizacion de rutas de entrega para TransCarga S.A.S., una empresa logistica colombiana con operaciones en Medellin y Cali. El proyecto implementa un pipeline ETL completo que extrae datos de fuentes abiertas del gobierno colombiano y los utiliza en un modelo de optimizacion basado en el Problema de Enrutamiento de Vehiculos (VRP).", styles['Cuerpo']))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Resultados Principales:", styles['Titulo3']))
    story.append(crear_tabla([['Metrica', 'Valor'], ['Clientes atendidos', '20'], ['Distancia optimizada', '530 km'], ['Vehiculos utilizados', '5'], ['Carga total', '10,000 kg'], ['Costo estimado', '$1,239,878 COP'], ['Tiempo de resolucion', '60 segundos']], [2.5*inch, 2.5*inch]))
    story.append(PageBreak())
    
    # 2. ARQUITECTURA
    story.append(Paragraph("2. Arquitectura del Proyecto", styles['Titulo1']))
    story.append(Paragraph("El proyecto sigue una arquitectura de pipeline ETL clasica, extendida con una capa de optimizacion. Los datos fluyen desde las fuentes externas hasta el modelo de optimizacion a traves de cuatro etapas principales:", styles['Cuerpo']))
    story.append(Spacer(1, 10))
    story.append(crear_tabla([['Etapa', 'Componente', 'Entrada', 'Salida'], ['1', 'Extraccion', 'APIs datos.gov.co', 'datos/raw/'], ['2', 'Transformacion', 'datos/raw/', 'datos/processed/'], ['3', 'Carga', 'datos/processed/', 'datos/output/'], ['4', 'Optimizacion', 'datos/output/', 'datos/results/']], [0.7*inch, 1.5*inch, 1.8*inch, 1.5*inch]))
    story.append(Spacer(1, 15))
    story.append(Paragraph("Estructura de Directorios:", styles['Titulo3']))
    story.append(Paragraph("TransCarga_ETL/ -- notebooks/ (4 Jupyter notebooks) -- datos/ (raw/, processed/, output/, results/) -- logs/ -- scripts de validacion", styles['Codigo']))
    
    # 3. PIPELINE ETL
    story.append(Paragraph("3. Pipeline ETL", styles['Titulo1']))
    story.append(Paragraph("3.1 Notebook 01: Extraccion de Datos", styles['Titulo2']))
    story.append(Paragraph("Este notebook extrae datos de multiples fuentes abiertas del gobierno colombiano utilizando APIs REST de datos.gov.co.", styles['Cuerpo']))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Fuentes de Datos:", styles['Titulo3']))
    story.append(crear_tabla([['Fuente', 'Dataset', 'Registros'], ['datos.gov.co', 'DIVIPOLA Municipios', '1,121'], ['datos.gov.co', 'Precios Combustible', '5,000+'], ['datos.gov.co', 'Parque Automotor', '5,000+'], ['datos.gov.co', 'Terminales Transporte', '1,000+']], [1.8*inch, 2*inch, 1.5*inch]))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Codigo de Extraccion:", styles['Titulo3']))
    story.append(Paragraph("def descargar_api(url, nombre, limite=5000): params = {'$limit': limite} response = requests.get(url, params=params, timeout=60) if response.status_code == 200: return pd.DataFrame(response.json())", styles['Codigo']))
    story.append(Spacer(1, 10))
    story.append(Paragraph("3.2 Notebook 02: Transformacion", styles['Titulo2']))
    story.append(Paragraph("La fase de transformacion limpia y procesa los datos extraidos.", styles['Cuerpo']))
    story.append(crear_tabla([['Operacion', 'Descripcion'], ['Limpieza DIVIPOLA', 'Filtrar Antioquia y Valle, validar coordenadas'], ['Limpieza Combustible', 'Convertir precios a numerico'], ['Limpieza Clientes', 'Validar coordenadas, convertir horarios'], ['Matriz Distancias', 'Calcular distancias Haversine'], ['Matriz Tiempos', 'Calcular tiempos de viaje']], [2*inch, 4*inch]))
    story.append(Spacer(1, 10))
    story.append(Paragraph("3.3 Notebook 03: Carga", styles['Titulo2']))
    story.append(Paragraph("Genera los archivos finales para el modelo de optimizacion.", styles['Cuerpo']))
    story.append(crear_tabla([['Archivo', 'Descripcion'], ['optimizacion_clientes.csv', '200 clientes con coordenadas'], ['optimizacion_vehiculos.csv', '64 vehiculos con capacidades'], ['optimizacion_bodegas.csv', '2 bodegas (Medellin, Cali)'], ['matriz_distancias.csv', 'Matriz 52x52 de distancias'], ['config_modelo.json', 'Parametros de configuracion VRP']], [2.5*inch, 3.5*inch]))
    story.append(PageBreak())
    
    # 4. MODELO VRP
    story.append(Paragraph("4. Modelo de Optimizacion VRP", styles['Titulo1']))
    story.append(Paragraph("4.1 Definicion del Problema", styles['Titulo2']))
    story.append(Paragraph("El Problema de Enrutamiento de Vehiculos (VRP) busca determinar las rutas optimas para una flota de vehiculos que deben entregar productos a un conjunto de clientes geograficamente distribuidos.", styles['Cuerpo']))
    story.append(Spacer(1, 10))
    story.append(Paragraph("El CVRP (Capacitated VRP) incluye restricciones de capacidad:", styles['Cuerpo']))
    story.append(Paragraph("Minimizar: Sum(i,j) c_ij * x_ij Sujeto a: - Cada cliente visitado exactamente una vez - Capacidad del vehiculo no excedida - Cada ruta empieza y termina en el deposito", styles['Codigo']))
    story.append(Spacer(1, 10))
    story.append(Paragraph("4.2 Implementacion con Google OR-Tools", styles['Titulo2']))
    story.append(Paragraph("Se utilizo Google OR-Tools, una libreria open-source para optimizacion combinatoria basada en Constraint Programming.", styles['Cuerpo']))
    story.append(crear_tabla([['Componente', 'Proposito'], ['RoutingIndexManager', 'Gestion de indices de nodos'], ['RoutingModel', 'Modelo de enrutamiento'], ['DistanceCallback', 'Callback de distancias'], ['AddDimensionWithVehicleCapacity', 'Restriccion de capacidad'], ['GuidedLocalSearch', 'Estrategia de busqueda metaheuristica']], [2.5*inch, 4*inch]))
    story.append(Spacer(1, 10))
    story.append(Paragraph("Codigo Principal:", styles['Titulo3']))
    story.append(Paragraph("manager = pywrapcp.RoutingIndexManager(n_locations, n_vehicles, 0) routing = pywrapcp.RoutingModel(manager) routing.RegisterTransitCallback(distance_callback) routing.AddDimensionWithVehicleCapacity(...) solution = routing.SolveWithParameters(search_parameters)", styles['Codigo']))
    story.append(Spacer(1, 10))
    story.append(Paragraph("4.3 Notebook 04: Optimizacion", styles['Titulo2']))
    story.append(Paragraph("Este notebook ejecuta el modelo de optimizacion y genera las rutas optimizadas con visualizacion grafica.", styles['Cuerpo']))
    story.append(PageBreak())
    
    # 5. HERRAMIENTAS
    story.append(Paragraph("5. Herramientas y Tecnologias", styles['Titulo1']))
    story.append(crear_tabla([['Categoria', 'Herramienta', 'Version', 'Proposito'], ['Lenguaje', 'Python', '3.12', 'Desarrollo principal'], ['Notebooks', 'Jupyter Lab', '4.x', 'Documentacion interactiva'], ['Datos', 'pandas', '2.x', 'Manipulacion de datos'], ['Datos', 'numpy', '1.x', 'Calculos numericos'], ['APIs', 'requests', '2.x', 'Peticiones HTTP'], ['Optimizacion', 'OR-Tools', '9.x', 'Solver VRP'], ['Visualizacion', 'matplotlib', '3.x', 'Graficos']], [1.3*inch, 1.3*inch, 0.8*inch, 2.5*inch]))
    story.append(Spacer(1, 15))
    story.append(Paragraph("Dependencias:", styles['Titulo3']))
    story.append(Paragraph("pandas>=2.0.0, numpy>=1.24.0, requests>=2.31.0, ortools>=9.8.0, matplotlib>=3.7.0, jupyter>=1.0.0", styles['Codigo']))
    
    # 6. DATASETS
    story.append(Paragraph("6. Datasets Utilizados", styles['Titulo1']))
    story.append(Paragraph("6.1 DIVIPOLA - Municipios Geolocalizados", styles['Titulo2']))
    story.append(crear_tabla([['Campo', 'Tipo', 'Descripcion'], ['cod_dpto', 'int', 'Codigo departamento'], ['nom_dpto', 'str', 'Nombre departamento'], ['nom_mpio', 'str', 'Nombre municipio'], ['latitud', 'float', 'Coordenada latitud'], ['longitud', 'float', 'Coordenada longitud']], [1.5*inch, 0.8*inch, 3.5*inch]))
    story.append(Spacer(1, 10))
    story.append(Paragraph("6.2 Precios de Combustible", styles['Titulo2']))
    story.append(crear_tabla([['Campo', 'Tipo', 'Descripcion'], ['departamentonombre', 'str', 'Nombre departamento'], ['producto', 'str', 'Tipo de combustible'], ['precio', 'int', 'Precio por galon (COP)']], [2*inch, 0.8*inch, 3*inch]))
    story.append(Spacer(1, 10))
    story.append(Paragraph("6.3 Datos Generados", styles['Titulo2']))
    story.append(Paragraph("Se generaron datos simulados basados en coordenadas reales: 200 clientes (coordenadas DIVIPOLA), 85 vehiculos, datos de trafico por hora/zona, 6 peajes principales.", styles['Cuerpo']))
    
    # 7. RESULTADOS
    story.append(PageBreak())
    story.append(Paragraph("7. Resultados de la Optimizacion", styles['Titulo1']))
    story.append(crear_tabla([['Metrica', 'Valor', 'Unidad'], ['Distancia Total', '530', 'km'], ['Clientes Atendidos', '20', 'clientes'], ['Vehiculos Utilizados', '5', 'vehiculos'], ['Carga Total', '10,000', 'kg'], ['Costo Combustible', '861,289', 'COP'], ['Costo Conductores', '378,589', 'COP'], ['Costo Total', '1,239,878', 'COP']], [2*inch, 1.5*inch, 1.5*inch]))
    story.append(Spacer(1, 15))
    story.append(Paragraph("Archivos Generados:", styles['Titulo3']))
    story.append(crear_tabla([['Archivo', 'Descripcion'], ['rutas_optimizadas.csv', 'Detalle de cada parada por vehiculo'], ['rutas_optimizadas.png', 'Visualizacion grafica de rutas'], ['metricas_optimizacion.json', 'Metricas de la solucion'], ['reporte_vehiculos.csv', 'Resumen por vehiculo']], [2.5*inch, 3.5*inch]))
    
    # 8. CONCLUSIONES
    story.append(Paragraph("8. Conclusiones", styles['Titulo1']))
    story.append(Paragraph("Logros:", styles['Titulo3']))
    story.append(Paragraph("• Extraccion automatica de datos de fuentes gubernamentales abiertas<br/>• Pipeline ETL reproducible y documentado en Jupyter Notebooks<br/>• Modelo de optimizacion VRP funcional con Google OR-Tools<br/>• Reduccion de distancia total a 530 km para 20 clientes<br/>• Estimacion de costos operativos de $1.24M COP<br/>• Visualizacion de rutas optimizadas", styles['Cuerpo']))
    story.append(Spacer(1, 15))
    story.append(Paragraph("Recomendaciones:", styles['Titulo3']))
    story.append(Paragraph("• Ampliar el numero de clientes para validar escalabilidad<br/>• Incluir restricciones de ventanas de tiempo (Time Windows)<br/>• Integrar datos de trafico en tiempo real<br/>• Desarrollar interfaz de usuario para operadores<br/>• Implementar sistema de monitoreo en produccion", styles['Cuerpo']))
    story.append(Spacer(1, 30))
    story.append(Paragraph("Generado automaticamente - TransCarga S.A.S. Data Office - 2026", styles['Titulo3']))
    
    # CONSTRUIR PDF
    doc.build(story, onFirstPage=crear_portada, onLaterPages=crear_header_footer)
    print(f"[OK] Documentacion generada: {output_path}")
    return output_path

if __name__ == '__main__':
    main()
