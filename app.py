import streamlit as st 
from PIL import Image

st.title("Cosmo Guapo")

st.header ("Amamos a los padrinos mágicos")
st.write ("Miren a un cosmo Guapo")
image = Image.open("Cosmo guapo.jpeg")

st.image(image, caption="La Leyenda")

texto = st.text_input("Bom dia", "fabella")
st.write("El texto escrito es", texto)

st.subheader("Ahora usemos 2 columnas")
col1, col2 = st.columns(2)

with col1:
  st.subheader("colores de los padrinos mágicos")
  st.write("Cosmo es verde y Wanda es rosada")
  resp = st.checkbox("¿Es verdad?")
  if resp:
    st.write("correcto!")

with col2:
  st.subheader("EHablemos de lo que hacen")
  modo = st.radio("Que pueden hacer", ("volar", "cumplir deseos", "hacer que la gente se enamore"))
  if modo == "volar":
    st.write("Si")
  if modo == "cumplir deseos":
    st.write("son muy buenos haciendo eso")
  if modo == "hacer que la gente se enamore":
     st.write("No, no pueden")
    
st.subheader("Uso de Botones")
if st.button("Presiona el boton si te parece que cosmo es guapo"):
  st.write("Gracias por decir que es guapo")
else:
  st.write("no has presionado aún")

with st.sidebar:
  st.subheader("configura la modalidad")
  mod_radio = st.radio(
    "Escoge la modalidad a usar",
    ("visual", "auditiva", "haptica")
  )
  




