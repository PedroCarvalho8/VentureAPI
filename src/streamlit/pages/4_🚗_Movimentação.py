import streamlit as st
from src.repositories.arduino_interaction import movimentacao, Movimentacao

st.title("Sistema de movimentação")

st.write("Status da movimentação do robô: " + movimentacao.status.value.upper())

col1, col2, col3 = st.columns(3)

col1.button(
    label="Frente",
    icon="⏩",
    on_click=movimentacao.andar,
    args=(Movimentacao.Direcoes.FRENTE,),
    use_container_width=True
)
col2.button(
    label="Trás",
    icon="⏪",
    on_click=movimentacao.andar,
    args=(Movimentacao.Direcoes.TRAS,),
    use_container_width=True
)
col3.button(
    label="Parar",
    icon="⏸️",
    on_click=movimentacao.parar,
    use_container_width=True
)
