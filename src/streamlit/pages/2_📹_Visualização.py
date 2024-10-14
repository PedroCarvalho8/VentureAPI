import streamlit as st
import time
from PIL import Image
import os


frame_dir = "temp_frames"

st.set_page_config(page_title="Visualização", page_icon="📊")
st.title("Sistema de Requisição e Coleta de Itens - Feed de Câmera")

frame_placeholder = st.empty()

if not os.path.exists(frame_dir):
    st.error(f"O diretório '{frame_dir}' não existe.")
else:
    while True:
        if os.path.exists(frame_dir):
            frames = sorted(os.listdir(frame_dir), key=lambda x: int(x.split('_')[1].split('.')[0]))

            if frames:
                last_frame_path = os.path.join(frame_dir, frames[-1])

                if os.path.exists(last_frame_path):
                    try:
                        image = Image.open(last_frame_path)
                        frame_placeholder.image(image, caption="Detecção em Tempo Real", use_column_width=True)
                    except Exception as e:
                        st.error(f"Erro ao abrir o frame: {e}")

                if len(frames) > 100:
                    try:
                        os.remove(os.path.join(frame_dir, frames[0]))
                    except FileNotFoundError:
                        pass

        time.sleep(0.1)
