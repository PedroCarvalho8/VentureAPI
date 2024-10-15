import streamlit as st
import pandas as pd
from src.streamlit.sidebar_custom import custom_sidebar
from src.repositories.db_interaction import *
from streamlit_extras.metric_cards import style_metric_cards
from streamlit_theme import st_theme


custom_sidebar()

if 'theme' not in st.session_state:
    st.session_state.theme = st_theme()

st.title("Histórico de solicitações")

dados = get_items_solicitacoes()

dados_df = pd.DataFrame(dados, columns=["Id", "Produto", "Status"])

requisitados = dados_df.query('Status == "Requisitado"')
encontrados = dados_df.query('Status == "Encontrado"')
retornados = dados_df.query('Status == "Retornado"')
cancelados = dados_df.query('Status == "Cancelado"')

dados_df['Status'] = dados_df['Status'].apply(
    lambda x:
    "🟡 " + x if x == "Requisitado" else
    "🔵 " + x if x == "Encontrado" else
    "🟢 " + x if x == "Retornado" else
    "🔴 " + x if x == "Cancelado" else
    x
)

col1, col2 = st.columns(2)

col2.write("Métricas das requisições")

col1.dataframe(dados_df, hide_index=True, use_container_width=True)

col2_1, col2_2 = col2.columns(2)

backgroun_color = st.session_state.theme.get('backgroundColor')
border_color = st.session_state.theme.get('secondaryBackgroundColor')
main_color = st.session_state.theme.get('primaryColor')

col2_1.metric(label="🟡 Requisitados", value=len(requisitados))
col2_2.metric(label="🔵 Encontrados", value=len(encontrados))
col2_1.metric(label="🟢 Retornados", value=len(retornados))
col2_2.metric(label="🔴 Cancelados", value=len(cancelados), help="Requisições são canceladas quando o sistema é reiniciado e o seu status está em 'requisitado'")

col2.metric(label="🗂️ Total", value=len(dados_df))

style_metric_cards(background_color=backgroun_color, border_left_color='a', border_color=border_color, box_shadow=False)

