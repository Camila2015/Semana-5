import streamlit as st 
from PIL import Image

st.title("Mi primera página")

st.header ("Hola, como va todo")
st.write ("diferente tipo de letra")
image = Image.open("Cosmo guapo.jpeg")

st.image(image, caption="La Leyenda")

texto = st.text_input("Bom dia", "fabella")
st.write("El texto escrito es", texto)

st.subheader("Ahora usemos 2 columnas")
col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia de usuario")
  resp = st.checkbox("Estoy de acuerdo")
  if resp:
    st.write("correcto!")

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("Que modalidad es la principal en tu interfaz", ("visual", "auditiva", "táctil"))
  if modo == "visual":
    st.write("La vista es fundamental para tu interfaz")
  if modo == "auditiva":
    st.write("La audición es fundamental para tu interfaz")
  if modo == "táctil":
     st.write("El tacto es fundamental para tu interfaz")
    




