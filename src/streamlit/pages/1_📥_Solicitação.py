from datetime import datetime
import streamlit as st
import json
import pandas as pd
from src.repositories.db_interaction import *
from src.streamlit.sidebar_custom import custom_sidebar


custom_sidebar()

image_path = 'images/logo.png'
icon_path = 'images/icon.png'

if "itens_solicitados" not in st.session_state:
    st.session_state.itens_solicitados = []

st.title("Solicitação de produtos")


@st.fragment(run_every="1s")
def atualizar_solicitacoes():
    st.logo(image_path, size="large", link=None, icon_image=icon_path)

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
        st.write("Produtos solicitados")
        itens_solicitados_df = pd.DataFrame(st.session_state.itens_solicitados, columns=['Produto'])
        itens_solicitados_df['Produto'] = itens_solicitados_df['Produto'].apply(lambda x: json.loads(x)['class_name'])
        st.dataframe(itens_solicitados_df, hide_index=True, use_container_width=True)
    else:
        st.write("Nenhum produto solicitado até o momento.")

atualizar_solicitacoes()


def solicitar_item(itens: str):
    for item in itens:
        msg = {
                'class_name': item,
                'status': "Requisitado",
                'timestamp': str(datetime.now()),
            }


        st.session_state.itens_solicitados.append(json.dumps(msg))

        send_msg(msg=json.dumps(msg), table='items_to_detect')

        insert_item_solicitacoes(msg)


itens_a_solicitar = st.multiselect(
    "Escolha os produtos",
    options=["Colgate", "Creme De Leite", "Fosforo", "Gelatina", "Polpa De Tomate", "Sabonete", "Toddynho"]
)
st.button("Solicitar", on_click=solicitar_item, args=(itens_a_solicitar,), use_container_width=True)
