import streamlit as st 
from PIL import Image

st.title("Mi primera página")

st.header ("Hola, como va todo")
st.write ("diferente tipo de letra")
image = Image.open("Interfaces cosmo guapo.jpeg")
