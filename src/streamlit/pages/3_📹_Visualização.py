import streamlit as st
import time
from PIL import Image
import os
from src.streamlit.sidebar_custom import custom_sidebar


custom_sidebar()

frame_dir = "temp_frames"

st.title("Visualização da câmera")

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
                        for i in range(50):
                            os.remove(os.path.join(frame_dir, frames[i]))
                    except FileNotFoundError:
                        pass

        time.sleep(0.1)
