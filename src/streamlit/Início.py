import streamlit as st

st.markdown('''
# Sistema de Requisição e Coleta de Itens com Visão Computacional

![Sistema de Requisição e Coleta](https://via.placeholder.com/800x200.png?text=Sistema+de+Requisi%C3%A7%C3%A3o+e+Coleta)

## 📖 Descrição do Projeto

Este projeto é um **Sistema de Requisição e Coleta de Itens** que utiliza um módulo de **visão computacional** para detectar e coletar itens em tempo real. O sistema é projetado para notificar os usuários quando os itens solicitados são encontrados, aumentando a eficiência na coleta.

## ⚙️ Tecnologias Utilizadas

- **Python**: A linguagem principal para desenvolvimento.
- **Streamlit**: Framework para criar aplicações web interativas.
- **OpenCV**: Biblioteca para processamento de imagens e visão computacional.
- **YOLO (You Only Look Once)**: Algoritmo de detecção de objetos em tempo real.
- **SQLite**: Banco de dados local para gerenciamento de dados.

## 🚀 Funcionalidades

- **Requisição de Itens**: Usuários podem solicitar itens específicos para detecção.
- **Detecção em Tempo Real**: O sistema utiliza uma câmera para detectar itens solicitados e notificar o usuário.
- **Notificações**: Alerta instantâneo quando um item solicitado é encontrado.
- **Interface Intuitiva**: Interface amigável construída com Streamlit, permitindo fácil interação.

## 🔄 Fluxo de Trabalho

1. O usuário faz uma requisição para coletar um item (ex: "Fósforo").
2. O sistema inicia a detecção em tempo real usando a câmera.
3. Quando o item solicitado é detectado, o sistema registra a detecção e notifica o usuário.
4. O histórico de solicitações e detecções é armazenado em um banco de dados SQLite.
''')