import streamlit as st

from constantes import *

# ---- Contantes ----
color_remarcar = "#649d91"
color_link = "#8cbcb1"




def link_button_html(titulo, link):
    enlace = f'<a href={link} style="text-decoration: none; color: {color_link};">{titulo}</a>'

    return enlace





# Link Variables

enlace_track = link_button_html(link="https://lllit3.bandcamp.com/album/silencio-esperado",titulo="Silencio Esperado")


enlace_moicflo = link_button_html(link="https://www.moicflo.com/",titulo="Moicflo")


enlace_ecunderground = link_button_html(link="https://www.ecunderground.com/", titulo="EC Underground")

enlace_aftherneo = link_button_html(link="https://soundcloud.com/neonites",titulo="AfterHoursNeo")

# -----------------------------



st.image("assets/banner.png", width=720, channels='RGB', use_container_width=True)


st.divider()


col1,col2 = st.columns(2, vertical_alignment='top')

with col1:
    st.markdown(body="""
<a href="https://lllit3.bandcamp.com/album/silencio-esperado" target="_blank" style="outline:none" tabindex="-1">
    <img class="imagen-album" src="https://f4.bcbits.com/img/a1653011087_10.jpg" style="display: block; height: auto; border: 0; width: 100%;" width="238" alt="Company logo" title="Company logo" height="auto">
</a>
""",unsafe_allow_html=True)
 
with col2:
    with st.container():
        st.markdown("""
<h3>Tracklist</h3>
<ol class="tracklist">
    <li>1. Gradientes</li>
    <li>2. paK.q</li>
    <li>3. Pull xet</li>
    <li>4. Pull bud</li>
    <li>5. Glep</li>
    <li>6. Frosting Image</li>
    <li>7. Expectativa Dub</li>
    <li>8. Dub Niebla</li>
    <li>9. D-M-O._continue</li>
    <li>10. D-M-O._</li>
    <li>11. D-M-O</li>
    <li>12. Joteo Telepático</li>
</ol>


                                   
<a class="link_support" href="https://lllit3.bandcamp.com/album/silencio-esperado" src="" target="_blank">Support</a>
                    
<br>
                    """,
                    unsafe_allow_html=True)




st.markdown(f"""
<p>{enlace_track} is an album by LLLIT, which embraces a stimulating mood of sonic experimentation to transport listeners on a unique journey through 12 tracks. This album combines immersive sounds and richly textured aural landscapes.

The album is not only a testament to the creativity of LLLIT - who in addition to being the main composer is the creator of the cover art and responsible for all multimedia content - but also to the collaboration with key figures in the art and music world.

            
> releases December 31, 2024</p>
""", unsafe_allow_html=True)



st.divider()



st.subheader("Preview")
# LINK SOUNDCLOUD
st.markdown("""
<iframe width="100%" height="300" scrolling="no" frameborder="no" allow="autoplay" src="https:/w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/playlists/1931462323&color=%23210d0dauto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=falseshow_teaser=true&visual=true"></iframe><div style="font-size: 10px; color: #cccccc;line-break:anywhere;word-break: normal;overflow: hidden;white-space: nowrap;text-overflow: ellipsis;font-family: Roboto,Tahoma,sans-serif;font-weight: 100;"><a href="https://soundcloud.comlllit_3" title="LLLIT" target="_blank" style="color: #cccccc; text-decoration: none;">LLLIT</a>· <a href="https://soundcloud.com/lllit_3/sets/silencio-esperado" title="Silencio Esperado[Preview] | Released" target="_blank" style="color: #cccccc; text-decoration: none;">SilencioEsperado [Preview] | Released</a></div>
""", unsafe_allow_html=True)

st.divider()

st.subheader("Creditos:")

st.markdown(f"""
> <p style="color:{color_remarcar}">Florence Meuleman</p> 
<p>Known as moiCflo, she stands out as a multi-faceted entrepreneur who leads {enlace_ecunderground}, a label dedicated to quality electronic music. With a background that spans public relations, audiovisual programming, creative design and consulting, Florence brings her strategic and artistic vision to spread the word about this project. You can explore more about her on her website: {enlace_moicflo} </p>
            
""", unsafe_allow_html=True)


st.markdown(f"""        
> <p style="color:{color_remarcar};">Daniel Vargas</p>        
<p>
Manager of AfterHoursNeo and host of the AFT / HRS Radio program broadcast on Saturdays and Sundays on Alternativa FM 100.3 ({enlace_aftherneo}), amplifies the album's scope by adding to the intimate and dynamic atmosphere that characterizes his program's concept. His curatorial approach, geared towards groove and beats perfect for afterhours, resonates deeply with the exploratory nuances of {enlace_track}.
</p>
""", unsafe_allow_html=True)


st.divider()
st.markdown(f"""
<p>Together, these collaborators elevate LLLIT's proposal to a higher level, positioning {enlace_track} as an immersive and unforgettable sound experience. Soon available on all digital platforms.</p>
            
""", unsafe_allow_html=True)
st.markdown("""
> license
            
#### © all rights reserved
""")


st.divider()








col1,col2,col3 = st.columns(3)
with col1:
    pass
with col2:
    st.page_link(page="pages/registro.py", icon="🎁", label="Get Promotional Code")
    
with col3:
    pass








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

