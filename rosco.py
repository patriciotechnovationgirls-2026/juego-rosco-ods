import streamlit as st
import time

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Rosco ODS", layout="wide")

# --- ESTILOS CSS COMPACTOS ---
st.markdown("""
    <style>
    .main-rosco {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 8px;
        padding: 10px;
        background-color: #ffffff;
        border-radius: 15px;
        margin-top: -40px; 
    }
    .letra-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 42px;
    }
    .letra-circulo {
        width: 38px;
        height: 38px;
        border-radius: 50% !important;
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 15px;
        color: white;
        border: 2px solid #fff;
    }
    .actual {
        border: 4px solid #000 !important;
        transform: scale(1.15);
        box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
    }
    .tipo-label { font-size: 8px; margin-top: 2px; font-weight: bold; color: #777; }
    #MainMenu {visibility: hidden;} 
    header {visibility: hidden;}    
    .stInfo { font-size: 20px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS A-Z ---
if 'rosco_data' not in st.session_state:
    st.session_state.rosco_data = [
        {"letra": "A", "tipo": "Contiene", "pista": "estado de quien no tiene alimentos suficientes.", "palabra": "HAMBRE", "ods": "ODS 2: Hambre Cero"},
        {"letra": "B", "tipo": "Comienza con", "pista": "estado de plenitud física y mental que se busca garantizar para todas las edades.", "palabra": "BIENESTAR", "ods": "ODS 3: Salud y Bienestar"},
        {"letra": "C", "tipo": "Comienza con", "pista": "variación global del estado del sistema terrestre que requiere medidas urgentes.", "palabra": "CLIMA", "ods": "ODS 13: Acción por el Clima"},
        {"letra": "D", "tipo": "Comienza con", "pista": "situación de disparidad entre personas, géneros o naciones.", "palabra": "DESIGUALDAD", "ods": "ODS 10: Reducción de Desigualdades"},
        {"letra": "E", "tipo": "Comienza con", "pista": "proceso de aprendizaje que debe ser inclusivo, equitativo y de calidad.", "palabra": "EDUCACION", "ods": "ODS 4: Educación de Calidad"},
        {"letra": "F", "tipo": "Contiene", "pista": "animales marinos cuya población debemos gestionar de forma sostenible.", "palabra": "PECES", "ods": "ODS 14: Vida Submarina"},
        {"letra": "G", "tipo": "Comienza con", "pista": "principio de igualdad de derechos y oportunidades entre hombres y mujeres.", "palabra": "GENERO", "ods": "ODS 5: Igualdad de Género"},
        {"letra": "H", "tipo": "Contiene", "pista": "enfermedad que se previene con saneamiento e higiene adecuados.", "palabra": "CHOLERA", "ods": "ODS 6: Agua Limpia y Saneamiento"},
        {"letra": "I", "tipo": "Comienza con", "pista": "motor de desarrollo basado en nuevas ideas, infraestructuras y procesos.", "palabra": "INNOVACION", "ods": "ODS 9: Industria, Innovación e Infraestructura"},
        {"letra": "J", "tipo": "Comienza con", "pista": "valor que busca que todos tengan acceso a instituciones eficaces y tribunales.", "palabra": "JUSTICIA", "ods": "ODS 16: Paz, Justicia e Instituciones Sólidas"},
        {"letra": "K", "tipo": "Contiene", "pista": "mil vatios de potencia eléctrica.", "palabra": "KILO", "ods": "ODS 7: Energía Asequible y No Contaminante"},
        {"letra": "L", "tipo": "Comienza con", "pista": "espacios urbanos donde habita la mayoría de la población mundial.", "palabra": "LOCALIDADES", "ods": "ODS 11: Ciudades y Comunidades Sostenibles"},
        {"letra": "M", "tipo": "Comienza con", "pista": "componentes de la naturaleza usados en la producción que deben gestionarse responsablemente.", "palabra": "MATERIALES", "ods": "ODS 12: Producción y Consumo Responsables"},
        {"letra": "N", "tipo": "Comienza con", "pista": "entorno natural y ecosistemas terrestres que debemos proteger de la deforestación.", "palabra": "NATURALEZA", "ods": "ODS 15: Vida de Ecosistemas Terrestres"},
        {"letra": "O", "tipo": "Comienza con", "pista": "grandes masas de agua salada que regulan el clima y albergan biodiversidad.", "palabra": "OCEANOS", "ods": "ODS 14: Vida Submarina"},
        {"letra": "P", "tipo": "Comienza con", "pista": "condición de privación extrema que el ODS 1 busca erradicar.", "palabra": "POBREZA", "ods": "ODS 1: Fin de la Pobreza"},
        {"letra": "Q", "tipo": "Contiene", "pista": "productos peligrosos que deben gestionarse para reducir la polución.", "palabra": "QUIMICOS", "ods": "ODS 12: Producción y Consumo Responsables"},
        {"letra": "R", "tipo": "Comienza con", "pista": "acción de transformar materiales desechados en nuevos recursos.", "palabra": "RECICLAJE", "ods": "ODS 12: Producción y Consumo Responsables"},
        {"letra": "S", "tipo": "Comienza con", "pista": "servicios para la eliminación higiénica de desechos humanos.", "palabra": "SANEAMIENTO", "ods": "ODS 6: Agua Limpia y Saneamiento"},
        {"letra": "T", "tipo": "Comienza con", "pista": "actividad productiva que debe realizarse en condiciones de dignidad.", "palabra": "TRABAJO", "ods": "ODS 8: Trabajo Decente y Crecimiento Económico"},
        {"letra": "U", "tipo": "Comienza con", "pista": "zonas de alta densidad poblacional que requieren planificación sostenible.", "palabra": "URBANAS", "ods": "ODS 11: Ciudades y Comunidades Sostenibles"},
        {"letra": "V", "tipo": "Comienza con", "pista": "derecho fundamental en los ecosistemas; lo opuesto a la extinción.", "palabra": "VIDA", "ods": "ODS 15: Vida de Ecosistemas Terrestres"},
        {"letra": "W", "tipo": "Contiene", "pista": "unidad de potencia usada para medir consumo energético.", "palabra": "WATT", "ods": "ODS 7: Energía Asequible y No Contaminante"},
        {"letra": "X", "tipo": "Contiene", "pista": "actitud de odio o rechazo a los extranjeros.", "palabra": "XENOFOBIA", "ods": "ODS 10: Reducción de Desigualdades"},
        {"letra": "Y", "tipo": "Contiene", "pista": "colaboración y alianzas internacionales para lograr las metas.", "palabra": "AYUDA", "ods": "ODS 17: Alianzas para lograr los Objetivos"},
        {"letra": "Z", "tipo": "Comienza con", "pista": "espacio geográfico afectado por conflictos donde se debe restaurar la paz.", "palabra": "ZONA", "ods": "ODS 16: Paz, Justicia e Instituciones Sólidas"}
    ]
# --- SESSION STATE ---
if 'index' not in st.session_state: st.session_state.index = 0
if 'resultados' not in st.session_state: st.session_state.resultados = {}
if 'tiempo' not in st.session_state: st.session_state.tiempo = 360
if 'activo' not in st.session_state: st.session_state.activo = True
if 'finalizado' not in st.session_state: st.session_state.finalizado = False
if 'key' not in st.session_state: st.session_state.key = 0

def siguiente():
    total = len(st.session_state.rosco_data)
    if len(st.session_state.resultados) >= total:
        st.session_state.finalizado = True
        return
    idx = (st.session_state.index + 1) % total
    while idx in st.session_state.resultados:
        idx = (idx + 1) % total
    st.session_state.index = idx

def validar():
    k = f"res_{st.session_state.key}"
    if k in st.session_state:
        intento = st.session_state[k].upper().strip()
        actual = st.session_state.rosco_data[st.session_state.index]
        if intento:
            if intento == actual['palabra']:
                st.session_state.resultados[st.session_state.index] = {"status": "correcto", "word": intento}
                st.toast("✅ ¡Correcto!", icon="🟢")
            else:
                st.session_state.resultados[st.session_state.index] = {"status": "incorrecto", "word": intento}
                st.toast(f"❌ Error: {actual['palabra']}", icon="🔴")
            st.session_state.key += 1
            st.session_state.activo = True
            siguiente()

# --- RENDERIZADO ---

# Rosco Visual
html_str = '<div class="main-rosco">'
for i, d in enumerate(st.session_state.rosco_data):
    res = st.session_state.resultados.get(i, {"status": "pendiente"})['status']
    color = "#ffc107" if res == "pendiente" else "#28a745" if res == "correcto" else "#dc3545"
    clase = "actual" if i == st.session_state.index and not st.session_state.finalizado else ""
    # Label abreviado para el rosco
    short_label = "C." if d["tipo"] == "Comienza con" else "Cont."
    html_str += f'<div class="letra-wrapper"><div class="letra-circulo {clase}" style="background-color: {color};">{d["letra"]}</div><div class="tipo-label">{short_label}</div></div>'
html_str += '</div>'
st.markdown(html_str, unsafe_allow_html=True)

ph_timer = st.empty()

if not st.session_state.finalizado:
    actual = st.session_state.rosco_data[st.session_state.index]
    
    # Texto de Pista Mejorado
    st.markdown(f"**{actual['ods']}**")
    texto_pista = f"**{actual['tipo']} la letra {actual['letra']}:** {actual['pista']}"
    st.info(texto_pista)
    
    c1, c2 = st.columns(2)
    if c1.button("🛑 DETENER", use_container_width=True):
        st.session_state.activo = False
        st.rerun()
    if c2.button("⏩ PASAPALABRA", use_container_width=True):
        st.session_state.activo = True
        st.session_state.key += 1
        siguiente()
        st.rerun()

    if not st.session_state.activo:
        st.text_input("Ingresá tu respuesta:", key=f"res_{st.session_state.key}", on_change=validar)

    if st.session_state.activo:
        while st.session_state.tiempo > 0 and st.session_state.activo:
            m, s = divmod(st.session_state.tiempo, 60)
            ph_timer.metric("🕒 TIEMPO", f"{m:02d}:{s:02d}")
            time.sleep(1)
            st.session_state.tiempo -= 1
            if st.session_state.tiempo <= 0:
                st.session_state.finalizado = True
                st.rerun()
    else:
        m, s = divmod(st.session_state.tiempo, 60)
        ph_timer.metric("⏸️ PAUSA", f"{m:02d}:{s:02d}")
else:
    st.subheader("🏁 Resumen")
    aciertos = sum(1 for v in st.session_state.resultados.values() if v['status'] == "correcto")
    st.metric("Puntuación", f"{aciertos} / {len(st.session_state.rosco_data)}")
    
    data_final = []
    for i, d in enumerate(st.session_state.rosco_data):
        res = st.session_state.resultados.get(i, {"status": "pendiente"})
        status_icon = "✅" if res['status'] == "correcto" else "❌"
        data_final.append({
            "Estado": status_icon,
            "Letra": d["letra"],
            "Palabra": d["palabra"],
            "Objetivo": d["ods"]
        })
    
    st.table(data_final)
    if st.button("🔄 Reiniciar"):
        for k in list(st.session_state.keys()): del st.session_state[k]
        st.rerun()
