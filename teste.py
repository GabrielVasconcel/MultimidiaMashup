import streamlit as st
import os
import base64
# from separate_vocals_instruments import separate_vocals_instruments

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


img = get_img_as_base64("tez.png")  

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
#background-image: url("https://img.freepik.com/vetores-gratis/fundo-de-pentagrama-musical-brilhante-com-notas-sonoras_1017-31220.jpg");
background-image: url("https://e1.pxfuel.com/desktop-wallpaper/166/548/desktop-wallpaper-night-phone-night-sky-mobile.jpg"); #definir imagem de fundo
background-size: 100%;
background-position: center;
background-repeat: no-repeat;
background-attachment: local;
}}

# [data-testid="stSidebar"] > div:first-child {{
# background-image: url("data:image/png;base64,{img}");
# background-position: center; 
# background-repeat: no-repeat;
# background-attachment: fixed;
# }}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
    
st.markdown(page_bg_img, unsafe_allow_html=True)


def main():
    st.markdown("<h1 style='text-align: center; color: white;'>BEM VINDO AO MASHUP CRAFT LAB</h1>", unsafe_allow_html=True)

    # Primeiro painel Upload
    st.markdown("<h2 style='text-align: center; color: white;'>Insira abaixo os arquivos de música que você deseja separar</h2>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white;'></h1>", unsafe_allow_html=True) #espaço

    col1, col2 = st.columns(2)

    # Upload de arquivos .wav
    with col1:
        uploaded_file1 = st.file_uploader("Upload do arquivo .wav que desejas pegar os vocais", type="wav")

    with col2:
        uploaded_file2 = st.file_uploader("Upload do arquivo .wav que desejas pegar o instrumental", type="wav")

    # Primeiro painel download
    st.markdown("<h2 style=' text-align: center; color: white;'>Faça o download abaixo dos arquivos gerados</h2>", unsafe_allow_html=True)
    st.markdown("<h2 style=' color: white;'></h2>", unsafe_allow_html=True) #espaço

    col3, col4 = st.columns(2)

    # Download de arquivos
    with col3:
        download_button1 = st.download_button(label="Download dos vocais", data=b'', file_name='arquivo_1.wav', mime='audio/wav')

    with col4:
        download_button2 = st.download_button(label="Download do instrumental", data=b'', file_name='arquivo_2.wav', mime='audio/wav')

    st.markdown("<h1 style='text-align: center; color: white;'>ÁREA MASHUP</h1>", unsafe_allow_html=True)

#------------------------------------------------------------------------------------------------------------------------

    # Segundo painel upload
    st.markdown("<h1 style='text-align: center; color: white;'>Insira abaixo os arquivos de música que você deseja juntar</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white;'></h1>", unsafe_allow_html=True) #espaço

    col5, col6 = st.columns(2)

    with col5:
        uploaded_file3 = st.file_uploader("Upload de arquivo .wav que desejas que seja os vocais do mashup", type="wav")

    with col6:
        uploaded_file4 = st.file_uploader("Upload de arquivo .wav que desejas que seja o instrumental do mashup", type="wav")


    # Segundo painel download
    st.markdown("<h1 style='text-align: center; color: white;'>Faça o download abaixo do mashup</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white;'></h1>", unsafe_allow_html=True) #espaço

    col7, col8, col9, col10, col11 = st.columns(5)

    with col9:
        download_button3 = st.download_button(label="Mashup", data=b'', file_name='arquivo_3.wav', mime='audio/wav')


if __name__ == "__main__":
    main()
