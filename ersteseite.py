import streamlit as st
from PIL import Image
st.title("Fehmki und Finni Seite <3")
st.text("Hallo Fehmki das ist meine Seite für dich <3")
bild_path = "Süßis.JPEG"
if "show_image" not in st.session_state:
    st.session_state.show_image = False
Knopf = st.button("Süßes bild <3")
if Knopf:
    st.session_state.show_image = True

if st.session_state.show_image:
    image = Image.open(bild_path)
    st.image(image, caption="Süßis.JPEG", use_column_width= True)

zweiterknopf = st.button("Ich vermisse dich  :(")
if zweiterknopf:
    st.text_area(" ")
    st.text("Ich dich auch Baby :(")