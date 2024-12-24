import streamlit as st
from utils.validate import is_valid_email, is_valid_phone, is_valid_country,get_user_ip, is_unique_ip, save_redeemed_ip
from utils.search_code import remove_code
from utils_bd.users import UserService
from models.user import User
from constantes import CORREO
from utils.enviar_correo import enviar_correo

import os

st.title("Silencio Esperado")
st.subheader("Codes Promocial")
st.write("Para obtener tu codigo de bandcamp, rellena el siguiente formulario:")


def registro():


    with st.form(key="form"):

        nombre = st.text_input("Nombre")
        apellido = st.text_input("Apellido")
        telefono = st.text_input("Numero de telefono", help="Incluye el codigo de area", placeholder="56XXXXXXXX")
        correo = st.text_input("Email", help="Ingresa un correo valido", placeholder="correo@correo.com")
        pais = st.text_input("Pais", help="Escribe la primera letra en mayuscula", placeholder="Chile, Mexico, Argentina, United States")
        comentario = st.text_area("Comentario", help="Dejanos un mensaje", max_chars=200)


        submit_button = st.form_submit_button(label="Enviar", type='secondary')

        st.divider()

        codes_respuesta = st.empty()

        code_canje = st.empty()

        if submit_button:
            if not nombre or not apellido or not correo or not telefono or not pais or not comentario :

                st.error("Por favor, complete todos los campos antes de enviar el formulario.", icon="🛸")
                
            elif any(char.isdigit() for char in nombre) or any(char.isdigit() for char in apellido):
                st.error("Nombre/Apellido tienen que ser validos", icon='🚫')

            elif not is_valid_email(correo):
                st.error("Por favor, ingrese un correo válido.", icon="📧")
            
            elif not telefono.isnumeric():
                st.error("Por favor, ingrese un numero de telefono valido", icon='📞')
            elif not is_valid_phone(telefono):
                st.error("Por favor, ingrese un numero de telefono valido", icon='📞')
            elif not is_valid_country(pais):
                st.error("Por favor, ingrese un pais valido", icon='🌍')
            else:
                
                try:
                    # Crear la carpeta 'data' si no existe
                    if not os.path.exists('data'):
                        os.makedirs('data')

                    # Validar si el correo ya estan en la base de datos
                    
                    if UserService.validate_user_email(correo):
                        st.error("El correo ya esta registrado", icon="📧")
                        return
                    else:
                        # Obtener la IP del usuario
                        ip_address = get_user_ip()
                        
                        # Validar si la IP ya está en la base de datos
                        if not is_unique_ip(ip_address):
                            st.error("Lo siento, ya has canjeado un código", icon="😢")
                            st.markdown(f"En el caso de que lo quieras recuperar tu codigo envia un correo a: {CORREO}")
                        else:
                            # Obtener un código de Bandcamp
                            code = remove_code()

                            if code:

                                # Guardar la información de la IP canjeada
                                save_redeemed_ip(ip_address)

                                # Crear una instancia de la clase User
                                user = User(nombre, apellido, telefono, correo, pais, comentario, code)

                                # Registrar al usuario en la base de datos
                                UserService.register_user(user.to_dict())
                                
                                
                                # Enviar el código por correo electrónico
                                enviar_correo(correo, code)
                                
                                
                                st.balloons()   
                                codes_respuesta.success(f"Gracias por registrarte", icon="🚀")

                                code_canje.text_area("Guarda tu codigo de canje", value=code, height=100, disabled=True, help="Recuerda guardar tu codigo, ya que no se volvera a mostrar")

                                st.link_button("Canjea tu codigo aqui!", "https://bandcamp.com/yum")
                            else:
                                codes_respuesta.error("Lo siento, no hay más códigos disponibles.", icon="😢")
                
                except Exception as e:
                    st.error(f"Ocurrió un error al registrar al usuario. Error: {e}", icon="🚫")
                    print(e)

                
registro()