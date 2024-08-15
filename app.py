import streamlit as st 
from PIL import Image

st.title("Mi primera página")

st.header ("Hola, como va todo")
st.write ("diferente tipo de letra")
image = Image.open("Cosmo guapo.jpeg")

st.image(image, caption="La Leyenda")

texto = st.text_input("Bom dia". "fabella")
st.write("El texto escrito es", texto)

st.subheader("Ahora usemos 2 columnas")
col1, col2 = st.colums(2)

with col1:
  st.subheader("Esta es la primera columna")

