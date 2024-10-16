import streamlit as st
from src.streamlit.sidebar_custom import custom_sidebar


custom_sidebar()

st.title("FAQ - Sistema de Requisição e Coleta de Itens")

faq = {
    "1. Como faço para solicitar um item?": (
        "Para solicitar um item, vá para a página 'Solicitação de produtos', escolha os produtos desejados na lista e clique no botão 'Solicitar'. O sistema processará sua solicitação e iniciará a detecção em tempo real."
    ),
    "2. O que acontece após eu solicitar um item?": (
        "Após a solicitação, o sistema começará a detectar o item solicitado em tempo real. Você será notificado assim que o item for encontrado."
    ),
    "3. Como posso ver o histórico das minhas solicitações?": (
        "Na página 'Histórico de solicitações', você pode visualizar todas as suas requisições anteriores, incluindo o status de cada item (Requisitado, Encontrado, Retornado, Cancelado)."
    ),
    "4. Posso cancelar uma solicitação?": (
        "Atualmente, não há uma funcionalidade para cancelar solicitações após serem feitas. As requisições são mantidas no sistema até que o item seja encontrado ou o sistema seja reiniciado."
    ),
    "5. O que significa o status de cada item no histórico?": (
        "Requisitado: O item foi solicitado e está aguardando detecção.\n"
        "Encontrado: O item solicitado foi detectado pelo sistema.\n"
        "Retornado: O item foi coletado ou processado com sucesso.\n"
        "Cancelado: O item foi cancelado, normalmente ao reiniciar o sistema."
    ),
    "6. Como posso saber se o sistema encontrou o item que solicitei?": (
        "Quando um item solicitado for detectado, você receberá uma notificação instantânea na interface do usuário."
    ),
    "7. O que faço se um item solicitado não for encontrado?": (
        "Se um item solicitado não for encontrado, você pode tentar solicitá-lo novamente ou entrar em contato com o suporte para mais assistência."
    ),
    "8. Posso solicitar vários itens de uma vez?": (
        "Sim! Você pode selecionar vários produtos na página 'Solicitação de produtos' usando a funcionalidade de múltipla seleção."
    ),
    "9. Como posso baixar o histórico das minhas solicitações?": (
        "Na página 'Histórico de solicitações', você encontrará um botão 'Baixar histórico' que permite exportar suas requisições em formato CSV."
    ),
    "10. Como funciona a detecção em tempo real?": (
        "O sistema utiliza uma câmera para monitorar o ambiente em tempo real. Quando um item solicitado é detectado, o sistema registra a detecção e notifica o usuário."
    ),
    "11. Onde são armazenados os dados das minhas solicitações?": (
        "Os dados são armazenados em um banco de dados SQLite local, garantindo que suas requisições e detecções sejam registradas de forma segura."
    ),
    "12. O que fazer se eu encontrar um erro ou bug?": (
        "Se você encontrar um erro ou bug, entre em contato com o suporte através da opção de feedback na interface ou envie um e-mail para nossa equipe."
    )
}

for question, answer in faq.items():
    st.expander(question, expanded=False).write(answer)
