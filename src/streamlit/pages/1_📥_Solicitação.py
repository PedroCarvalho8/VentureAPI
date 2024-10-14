from datetime import datetime
import streamlit as st
import json
import pandas as pd
from src.repositories.db_interaction import *


st.set_page_config(
    page_title="Solicitação",
    page_icon="📥",
)


if "itens_solicitados" not in st.session_state:
    st.session_state.itens_solicitados = []

st.title("Sistema para solicitação de produtos")

@st.fragment(run_every="1s")
def atualizar_solicitacoes():

    items_detectados = get_msg(table='detected_items')

    if items_detectados:
        idxs_to_remove = []

        for item in items_detectados:
            detected_class_name = json.loads(item[1])['class_name'].upper()
            class_list = [json.loads(i).get('class_name').upper() for i in st.session_state.itens_solicitados]

            if detected_class_name in class_list:
                st.success(f"O item solicitado '{detected_class_name}' foi encontrado!")
                idx_to_remove = [i for i, c in enumerate(class_list) if c == detected_class_name]
                idxs_to_remove.extend(idx_to_remove)

        idxs_to_remove = [idx for idx in idxs_to_remove if idx < len(st.session_state.itens_solicitados)]

        if st.session_state.itens_solicitados and idxs_to_remove:
            for idx in sorted(set(idxs_to_remove), reverse=True):
                if 0 <= idx < len(st.session_state.itens_solicitados):
                    st.session_state.itens_solicitados.pop(idx)

    if st.session_state.itens_solicitados:
        st.write("Produtos solicidatos")
        itens_solicitados_df = pd.DataFrame(st.session_state.itens_solicitados, columns=['Item'])
        itens_solicitados_df['Item'] = itens_solicitados_df['Item'].apply(lambda x: json.loads(x)['class_name'])
        st.dataframe(itens_solicitados_df)
    else:
        st.write("Nenhum produto solicitado até o momento.")


atualizar_solicitacoes()


def solicitar_item(itens: str):
    for item in itens:
        msg = json.dumps(
            {
                'class_name': item,
                'timestamp': str(datetime.now()),
            }
        )

        st.session_state.itens_solicitados.append(msg)

        send_msg(msg=msg, table='items_to_detect')

itens_a_solicitar = st.multiselect("Escolha os produtos", options=["Fosforo", "Toddynho", "Pedro"])
st.button("Solicitar", on_click=solicitar_item, args=(itens_a_solicitar,))
