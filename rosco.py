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
        {"letra": "A", "tipo": "Comienza con", "pista": "actividad del campo que permite cultivar alimentos para la población.", "palabra": "AGRICULTURA", "ods": "ODS 2: Hambre Cero"},
        {"letra": "B", "tipo": "Comienza con", "pista": "microorganismos, algunos dañinos, contra los que la medicina y la prevención trabajan constantemente.", "palabra": "BACTERIAS", "ods": "ODS 3: Salud y Bienestar"},
        {"letra": "C", "tipo": "Comienza con", "pista": "zonas donde se unen la tierra y el mar, muy afectadas por el aumento del nivel del agua.", "palabra": "COSTAS", "ods": "ODS 13: Acción por el Clima"},
        {"letra": "D", "tipo": "Comienza con", "pista": "trato injusto hacia personas por su origen, género u otras características.", "palabra": "DISCRIMINACION", "ods": "ODS 10: Reducción de Desigualdades"},
        {"letra": "E", "tipo": "Comienza con", "pista": "tarea de transmitir conocimientos y habilidades a otras personas.", "palabra": "ENSEÑANZA", "ods": "ODS 4: Educación de Calidad"},
        {"letra": "F", "tipo": "Contiene", "pista": "conjunto de animales que habitan mares y océanos y que deben protegerse de la sobreexplotación.", "palabra": "ARRECIFES", "ods": "ODS 14: Vida Submarina"},
        {"letra": "G", "tipo": "Comienza con", "pista": "protecciones legales que aseguran que se respeten los derechos de las personas.", "palabra": "GARANTIAS", "ods": "ODS 5: Igualdad de Género"},
        {"letra": "H", "tipo": "Contiene", "pista": "conjunto de hábitos de limpieza que ayudan a prevenir enfermedades.", "palabra": "HIGIENE", "ods": "ODS 6: Agua Limpia y Saneamiento"},
        {"letra": "I", "tipo": "Comienza con", "pista": "sector económico que transforma materias primas en productos elaborados.", "palabra": "INDUSTRIA", "ods": "ODS 9: Industria, Innovación e Infraestructura"},
        {"letra": "J", "tipo": "Comienza con", "pista": "procesos legales donde se resuelven conflictos según la ley.", "palabra": "JUICIOS", "ods": "ODS 16: Paz, Justicia e Instituciones Sólidas"},
        {"letra": "K", "tipo": "Contiene", "pista": "unidad de potencia usada para medir el consumo eléctrico.", "palabra": "KILOVATIO", "ods": "ODS 7: Energía Asequible y No Contaminante"},
        {"letra": "L", "tipo": "Comienza con", "pista": "materiales básicos usados en la construcción de viviendas y edificios.", "palabra": "LADRILLOS", "ods": "ODS 11: Ciudades y Comunidades Sostenibles"},
        {"letra": "M", "tipo": "Comienza con", "pista": "recursos que se transforman para fabricar productos de uso cotidiano.", "palabra": "MATERIAS", "ods": "ODS 12: Producción y Consumo Responsables"},
        {"letra": "N", "tipo": "Comienza con", "pista": "hogares naturales de aves y otros animales que deben protegerse en los ecosistemas.", "palabra": "NIDOS", "ods": "ODS 15: Vida de Ecosistemas Terrestres"},
        {"letra": "O", "tipo": "Comienza con", "pista": "trabajos que requieren habilidades prácticas y formación específica.", "palabra": "OFICIOS", "ods": "ODS 8: Trabajo Decente y Crecimiento Económico"},
        {"letra": "P", "tipo": "Comienza con", "pista": "ayudas económicas que reciben personas mayores o en situación vulnerable.", "palabra": "PENSIONES", "ods": "ODS 1: Fin de la Pobreza"},
        {"letra": "Q", "tipo": "Contiene", "pista": "espacio natural con árboles y senderos dentro o cerca de una ciudad.", "palabra": "PARQUE", "ods": "ODS 15: Vida de Ecosistemas Terrestres"},
        {"letra": "R", "tipo": "Comienza con", "pista": "lugar seguro donde las personas pueden protegerse tras perder su hogar por una crisis o desastre.", "palabra": "REFUGIO", "ods": "ODS 11: Ciudades y Comunidades Sostenibles"},
        {"letra": "S", "tipo": "Comienza con", "pista": "prestaciones básicas como transporte, salud o energía que necesita la población.", "palabra": "SERVICIOS", "ods": "ODS 9: Industria, Innovación e Infraestructura"},
        {"letra": "T", "tipo": "Comienza con", "pista": "espacios donde se aprende un oficio mediante la práctica.", "palabra": "TALLERES", "ods": "ODS 4: Educación de Calidad"},
        {"letra": "U", "tipo": "Comienza con", "pista": "acción de trabajar en conjunto para lograr un objetivo común.", "palabra": "UNION", "ods": "ODS 17: Alianzas para lograr los Objetivos"},
        {"letra": "V", "tipo": "Comienza con", "pista": "construcciones destinadas a que las personas tengan un lugar digno donde vivir.", "palabra": "VIVIENDAS", "ods": "ODS 11: Ciudades y Comunidades Sostenibles"},
        {"letra": "W", "tipo": "Contiene", "pista": "unidad que mide la potencia eléctrica de aparatos y sistemas de energía.", "palabra": "WATT", "ods": "ODS 7: Energía Asequible y No Contaminante"},
        {"letra": "X", "tipo": "Contiene", "pista": "rechazo o miedo irracional hacia personas de otras culturas o países.", "palabra": "XENOFOBIA", "ods": "ODS 10: Reducción de Desigualdades"},
        {"letra": "Y", "tipo": "Contiene", "pista": "ayuda que una persona, organización o país brinda a otros para mejorar su situación.", "palabra": "APOYO", "ods": "ODS 17: Alianzas para lograr los Objetivos"},
        {"letra": "Z", "tipo": "Comienza con", "pista": "excavaciones que se usan para instalar cañerías y mejorar servicios sanitarios.", "palabra": "ZANJAS", "ods": "ODS 6: Agua Limpia y Saneamiento"}
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
