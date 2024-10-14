import streamlit as st
import json
import pandas as pd


from src.repositories.db_interaction import get_msg


if "itens_coletados" not in st.session_state:
    st.session_state.itens_coletados = []


@st.fragment(run_every="2s")
def atualizar_itens_coletados():
    dados = get_msg(table='detected_items')
    st.session_state.itens_coletados = dados

    st.write(f"Total de itens detectados: {len(st.session_state.itens_coletados)}")

    dados_df = pd.DataFrame([json.loads(dado[1]) for dado in st.session_state.itens_coletados])

    if not dados_df.empty:
        try:
            dados_agrupados = dados_df.groupby('class_name', as_index=False)['object_count'].max()

            st.dataframe(dados_agrupados)

        except KeyError:
            st.write("Erro: Chave 'class_name' ou 'object_count' não encontrada nos dados.")
    else:
        st.write("Nenhum dado disponível para exibição.")


atualizar_itens_coletados()
