# STREAMLIT
import separate_vocals_instruments
import streamlit as st

caminho = "/content/separateMusic"
st.set_page_config(page_title="Mashup Maker")

st.subheader("Separador vocal/instrumental")
nome_musica = st.text_input("Nome da Música")
audio1 = st.file_uploader("Música", type=["wav"])
# separate_vocals_instruments(audio1, caminho)
# vocals = caminho + "/{}/vocals.wav".format(nome_musica)
# accompaniment = caminho + "/{}/accompaniment.wav".format(nome_musica)
st.download_button("Download vocais", data="vocals")
st.download_button("Download Instrumental", data="accompaniment")