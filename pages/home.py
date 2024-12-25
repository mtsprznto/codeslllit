import streamlit as st

from constantes import *

# ---- Contantes ----
color_remarcar = "#649d91"

color_link = "#8cbcb1"

color_verde = "#008000"
color_naranja = "#FFA500"

enlace_html = f'<a href="https://lllit3.bandcamp.com/album/silencio-esperado" style="text-decoration: none; color: {color_link};">Silencio Esperado</a>'


# -----------------------------

st.image("assets/banner.png", width=720, channels='RGB')


st.divider()

st.image("https://f4.bcbits.com/img/a1653011087_10.jpg")





st.markdown(f"""
{enlace_html} es una album de LLLIT, que abraza un estimulante ánimo de experimentación sonora para transportar a los oyentes a un viaje único a través de 12 tracks. Este álbum combina sonidos envolventes y paisajes auditivos ricos en texturas.

El álbum no solo es un testimonio de la creatividad de LLLIT —quien además de ser el compositor principal es el creador de la carátula y responsable de todo el contenido multimedia—, sino también de la colaboración con figuras clave en el mundo del arte y la música
            
> releases December 31, 2024
""", unsafe_allow_html=True)



st.divider()




st.subheader("Creditos:")

st.markdown(f"""
> <p style="color:{color_remarcar}">Florence Meuleman</p> 
<p style="">Conocida como moiCflo, destaca como una emprendedora multifacética que lidera EcuUnderground (ecunderground.com), un sello dedicado a la música electrónica de calidad. Con una trayectoria que abarca relaciones públicas, programación audiovisual, diseño creativo y consultoría, Florence aporta su visión estratégica y artística para difundir este proyecto. Puedes explorar más sobre ella en su sitio web: [Moicflo](www.moicflo.com) </p>
            
""", unsafe_allow_html=True)

# st.markdown(f'<p style="color:{color_verde};">Florence Meuleman</p>', unsafe_allow_html=True)

st.markdown(f"""        
> <p style="color:{color_remarcar};">Daniel Vargas</p>        
Encargado de AfterHoursNeo y anfitrión del programa AFT / HRS Radio que se transmite los sábados y domingos por Alternativa FM 100.3 (soundcloud.com/neonites), amplifica el alcance del álbum al sumarlo a la atmósfera íntima y dinámica que caracteriza el concepto de su programa. Su enfoque curatorial, orientado hacia el groove y los beats perfectos para los afterhours, resuena profundamente con los matices exploratorios de Silencio Esperado.
</p>
""", unsafe_allow_html=True)


st.divider()
st.markdown("""

En conjunto, estos colaboradores elevan la propuesta de LLLIT a un nivel superior, posicionando :blue[Silencio Esperado] como una experiencia sonora inmersiva e inolvidable. Próximamente disponible en todas las plataformas digitales, este álbum promete ser un hito en la música experimental.
            

> license
            
#### © all rights reserved
""")

st.divider()
st.subheader("PREVIEW")

st.markdown("""
<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https://w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1931462323&color=%23210d0d&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break: anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis; font-family: Roboto,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.com/lllit_3" title="LLLIT" target="_blank" style="color: #cccccc; text-decoration: none;">LLLIT</a> · <a href="https://soundcloud.com/lllit_3/sets/silencio-esperado" title="Silencio Esperado [Preview] | Released" target="_blank" style="color: #cccccc; text-decoration: none;">Silencio Esperado [Preview] | Released</a></div>
""", unsafe_allow_html=True)






st.divider()
st.page_link(page="pages/registro.py", icon="🎁", label="Obtener Codigo Promocional")








# ---- LINKS ---------


st.divider()

st.markdown("## Links")

col1, col2, col3 = st.columns(3)


with col1:
    st.link_button("Soundcloud", SOUNDCLOUD_LINK, use_container_width=True)
with col2:
    st.link_button("Bandcamp", BANDCAMP_LINK, use_container_width=True)
with col3:
    st.link_button("Spotify", SPOTIFY_LINK, use_container_width=True)

