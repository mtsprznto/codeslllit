import streamlit as st
import pathlib

st.set_page_config(page_title="LLLIT | Codes", initial_sidebar_state="collapsed", page_icon="assets/favicon.ico", layout="centered")

# ----------------- Load CSS -----------------
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")

# LOAD CSS
css_path = pathlib.Path("assets/styles.css")
load_css(css_path)


# ----------------- Pages -----------------


home_page =st.Page(
    page="pages/home.py",
    title="Album Info",
    icon="💿",
    default=True
)

registro_page = st.Page(
    page="pages/registro.py", 
    title="Codes Promocional", 
    icon='🖊️'
)

pg = st.navigation(
    {
        "Home": [home_page],
        "Code": [registro_page]
    },
    expanded=True
)

pg.run()