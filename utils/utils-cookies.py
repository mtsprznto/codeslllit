import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
import uuid

# Inicializar el gestor de cookies
cookies = EncryptedCookieManager(prefix="myapp")

# Asegurarse de que las cookies están disponibles
if not cookies.ready():
    st.stop()

# Obtener o generar un identificador único
if 'unique_id' not in cookies:
    cookies['unique_id'] = str(uuid.uuid4())
    cookies.save()

unique_id = cookies['unique_id']