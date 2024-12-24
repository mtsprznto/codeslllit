import streamlit as st

from constantes import *

st.title("SILENCIO ESPERADO")



st.divider()


st.image("https://f4.bcbits.com/img/a1653011087_10.jpg")


st.markdown("""
**Silencio Esperado** es una album de LLLIT, que abraza un estimulante ánimo de experimentación sonora para transportar a los oyentes a un viaje único a través de 12 tracks. Este álbum combina sonidos envolventes y paisajes auditivos ricos en texturas, mostrando un enfoque audaz hacia la innovación musical.

El álbum no solo es un testimonio de la creatividad de LLLIT —quien además de ser el compositor principal es el creador de la carátula y responsable de todo el contenido multimedia—, sino también de la colaboración con figuras clave en el mundo del arte y la música
            
> releases December 31, 2024

**Florence Meuleman**, conocida como moiCflo, destaca como una emprendedora multifacética que lidera EcuUnderground (ecunderground.com), un sello dedicado a la música electrónica de calidad. Con una trayectoria que abarca relaciones públicas, programación audiovisual, diseño creativo y consultoría, Florence aporta su visión estratégica y artística para difundir este proyecto. Puedes explorar más sobre ella en su sitio web: moicflo.com.

**Daniel Vargas**, encargado de AfterHoursNeo y anfitrión del programa AFT / HRS Radio que se transmite los sábados y domingos por Alternativa FM 100.3 (soundcloud.com/neonites), amplifica el alcance del álbum al sumarlo a la atmósfera íntima y dinámica que caracteriza el concepto de su programa. Su enfoque curatorial, orientado hacia el groove y los beats perfectos para los afterhours, resuena profundamente con los matices exploratorios de Silencio Esperado.


En conjunto, estos colaboradores elevan la propuesta de LLLIT a un nivel superior, posicionando Silencio Esperado como una experiencia sonora inmersiva e inolvidable. Próximamente disponible en todas las plataformas digitales, este álbum promete ser un hito en la música experimental.
            

> license
            
#### © all rights reserved
""")

st.page_link(page="pages/registro.py", icon="🎁", label="Obtener Codigo Promocional")




st.divider()

st.markdown("## Links")

col1, col2, col3 = st.columns(3)


with col1:
    st.link_button("Soundcloud", SOUNDCLOUD_LINK, use_container_width=True)
with col2:
    st.link_button("Bandcamp", BANDCAMP_LINK, use_container_width=True)
with col3:
    st.link_button("Spotify", SPOTIFY_LINK, use_container_width=True)

