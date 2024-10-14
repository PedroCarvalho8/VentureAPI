import streamlit as st


image_path = 'images/logo.png'
icon_path = 'images/icon.png'


def custom_sidebar():
    st.set_page_config(page_icon=icon_path)
    st.logo(image_path, size="large", link=None, icon_image=icon_path)
    # with st.sidebar:
    #     st.image(image_path, use_column_width='auto')
