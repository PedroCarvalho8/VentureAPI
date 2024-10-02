import streamlit as st
import requests


def alternar_frente() -> None:
    try:
        requests.get("http://localhost/frente")
    except Exception as e:
        st.error(e)


def alternar_tras() -> None:
    try:
        requests.get("http://localhost/tras")
    except Exception as e:
        st.error(e)


st.button("Frente", on_click=alternar_frente)
st.button("Tras", on_click=alternar_tras)

