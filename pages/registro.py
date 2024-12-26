import streamlit as st
from utils.validate import is_valid_email, is_valid_phone, is_valid_country,get_user_ip, is_unique_ip, save_redeemed_ip
from utils.search_code import remove_code, remove_code_cloud
from utils_bd.users import UserService
from utils_bd.codes import CodesService
from utils_bd.ip_address import IpAddressService
from models.user import User
from constantes import CORREO
from utils.enviar_correo import enviar_correo



import pandas as pd

import os

st.image("assets/banner.png", width=720, channels='RGB')



st.subheader("Promotional Code")
st.write("To get your bandcamp code, fill out the form below:")


def registro():


    with st.form(key="form"):

        nombre = st.text_input("Name")
        apellido = st.text_input("Last name")
        telefono = st.text_input("Phone number", help="Includes area code", placeholder="56XXXXXXXX")
        correo = st.text_input("Email", help="Enter a valid email address", placeholder="correo@correo.com")
        pais = st.text_input("Country", help="Type the first letter in capital letters", placeholder="Chile, Mexico, Argentina, United States")
        comentario = st.text_area("Comment", help="Leave us a message", max_chars=200)


        submit_button = st.form_submit_button(label="Send to", type='secondary')

        st.divider()

        codes_respuesta = st.empty()

        code_canje = st.empty()

        if submit_button:
            if not nombre or not apellido or not correo or not telefono or not pais or not comentario :

                st.error("Please complete all fields before submitting the form.", icon="🛸")
                
            elif any(char.isdigit() for char in nombre) or any(char.isdigit() for char in apellido):
                st.error("First Name/Last Name must be valid", icon='🚫')

            elif not is_valid_email(correo):
                st.error("Please enter a valid email address.", icon="📧")
            
            # elif not telefono.isnumeric():
            #     st.error("Please, enter a valid phone number", icon='📞')
            #     st.error("")
            # elif not is_valid_phone(telefono):
            #     st.error("Please, enter a valid phone number", icon='📞')
            
            # elif not is_valid_country(pais):
            #     st.error("Please enter a valid country", icon='🌍')
            
            else:
                
                try:
                    
                    # Validar si el correo ya estan en la base de datos
                    if UserService.validate_user_email(correo):
                        st.error("The email is already registered", icon="📧")
                        return
                    
                    else:
                        # Obtener la IP del usuario
                        ip_address = get_user_ip()
                        
                        # Validar si la IP ya está en la base de datos
                        if not is_unique_ip(ip_address):
                            st.error("Sorry, you have already redeemed a code.", icon="😢")
                            st.markdown(f"In case you want to recover your code send an email to: {CORREO}")
                        else:
                            

                            # Obtener un código de Bandcamp
                            code = CodesService.get_code()
                            

                            if code:
                                
                                # Guardar la información de la IP canjeada
                                save_redeemed_ip(ip_address)

                                # Guardo la ip en mi base de datos
                                IpAddressService.register_ip({"ip_address": ip_address})

                                # Crear una instancia de la clase User
                                user = User(nombre, apellido, telefono, correo, pais, comentario, code)

                                # Registrar al usuario en la base de datos
                                UserService.register_user(user.to_dict())
                                
                                
                                # Enviar el código por correo electrónico
                                enviar_correo(correo, code.code)
                                
                                
                                st.balloons()   
                                codes_respuesta.success(f"Thank you for registering", icon="🚀")

                                code_canje.text_area("Save your redemption code", value=code.code, height=100, disabled=True, help="Remember to save your code, as it will not be displayed again.")

                                st.link_button("Redeem your code here!", "https://lllit3.bandcamp.com/yum")

                                #Eliminar el codigo de la base de datos
                                CodesService.delete_code(code.code)

                            else:
                                codes_respuesta.error("Sorry, there are no more codes available.", icon="😢")
                
                except Exception as e:
                    st.error(f"An error occurred while registering the user.", icon="🚫")
                    print(e)

                
registro()