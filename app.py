import streamlit as st

# Configuración de la página
st.set_page_config(
    page_title="Fernandez Abogados",
    page_icon="⚖️",
    layout="wide"
)

# Logo y título principal
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://via.placeholder.com/150", width=150)  # Reemplaza con tu logo
with col2:
    st.title("Fernandez Abogados")
    st.markdown("**Especialistas en derecho pensional y laboral**")

# Barra lateral con menú de navegación
with st.sidebar:
    st.header("Servicios")
    selected = st.radio(
        "Seleccione una opción:",
        ["Inicio", "Bonos pensionales", "Liquidación RAIS", "Liquidación RPM", "Actuariales Otros"]
    )

# Contenido principal según selección
if selected == "Inicio":
    st.header("Bienvenido a Fernandez Abogados")
    st.write("""
    Nuestro bufete se especializa en asesoría legal en materia pensional y laboral. 
    Ofrecemos servicios profesionales para garantizar sus derechos.
    """)
    
    st.subheader("Nuestros Servicios")
    st.markdown("""
    - **Bonos pensionales**: Asesoría especializada en reconocimiento y liquidación
    - **Liquidación RAIS**: Cálculo preciso de su liquidación
    - **Liquidación RPM**: Análisis de su régimen de prima media
    - **Actuariales Otros**: Estudios técnicos especializados
    """)
    
    st.subheader("Contáctenos")
    st.write("📞 Teléfono: [Ingrese su teléfono]")
    st.write("📧 Email: [Ingrese su email]")
    st.write("🏢 Dirección: [Ingrese su dirección]")

elif selected == "Bonos pensionales":
    st.header("Bonos Pensionales")
    st.write("Contenido sobre bonos pensionales...")
    # Aquí puedes agregar formularios, explicaciones, etc.

elif selected == "Liquidación RAIS":
    st.header("Liquidación RAIS")
    st.subheader("Seleccione el Factor de Ajuste Pensional (FAP)")
    fap_options = {
        "FAP 1 - Sector Público (2017)": 0.8912,
        "FAP 2 - Sector Privado (2018)": 0.9125,
        "FAP 3 - Mixto (2019)": 0.9341,
        "FAP 4 - Especial (2020)": 0.9567
    }
    
    selected_fap = st.selectbox(
        "Elija el FAP aplicable:",
        options=list(fap_options.keys()),
        index=0  # Opción por defecto
    )
    
    # Mostrar el valor del FAP seleccionado
    fap_value = fap_options[selected_fap]
    st.info(f"El FAP seleccionado es: {fap_value}")
    
    # Sección de entrada de datos
    st.subheader("Datos para Liquidación")
    col1, col2 = st.columns(2)
    
    with col1:
        salario_promedio = st.number_input(
            "Salario promedio mensual (Últimos 10 años):",
            min_value=0.0,
            value=3000000.0,
            step=100000.0
        )
        
        tiempo_servicio = st.number_input(
            "Tiempo de servicio (Años):",
            min_value=0.0,
            value=20.0,
            step=0.5
        )
    
    with col2:
        semanas_cotizadas = st.number_input(
            "Semanas cotizadas:",
            min_value=0,
            value=1000,
            step=50
        )
        
        edad_jubilacion = st.number_input(
            "Edad de jubilación:",
            min_value=40,
            value=57,
            step=1
        )
    
    # Cálculos básicos (fórmula de ejemplo - ajustar según normativa real)
    if st.button("Calcular Liquidación"):
        # Fórmula simplificada para ejemplo
        base_liquidacion = salario_promedio * tiempo_servicio
        liquidacion_bruta = base_liquidacion * fap_value
        bonificacion = (semanas_cotizadas / 1000) * 0.1 * liquidacion_bruta
        liquidacion_neta = liquidacion_bruta + bonificacion
        
        # Mostrar resultados
        st.success("## Resultados de la Liquidación")
        
        resultados = {
            "Base de liquidación": f"${base_liquidacion:,.2f}",
            "FAP aplicado": f"{fap_value} ({selected_fap.split('-')[0]})",
            "Liquidación bruta": f"${liquidacion_bruta:,.2f}",
            "Bonificación por semanas": f"${bonificacion:,.2f}",
            "**Liquidación neta estimada**": f"**${liquidacion_neta:,.2f}**"
        }
        
        for k, v in resultados.items():
            st.metric(label=k, value=v)
        
        # Advertencia legal
        st.warning("""
        **Nota:** Este cálculo es una estimación basada en parámetros generales. 
        Para una valoración exacta, consulte con nuestro equipo jurídico.
        """)
    
    # Información adicional
    st.markdown("---")
    st.subheader("¿Qué es el FAP?")
    st.write("""
    El Factor de Ajuste Pensional (FAP) es un índice técnico que permite actualizar el valor 
    de las pensiones considerando variables como:
    - Expectativa de vida
    - Tasas de interés
    - Inflación
    - Otros factores actuariales
    """)
    st.write("Contenido sobre liquidación RAIS...")

elif selected == "Liquidación RPM":
    st.header("Liquidación RPM")
    st.write("Contenido sobre liquidación RPM...")

elif selected == "Actuariales Otros":
    st.header("Actuariales Otros")
    st.write("Contenido sobre estudios actuariales...")

# Pie de página
st.markdown("---")
st.markdown("© 2023 Fernandez Abogados - Todos los derechos reservados")
