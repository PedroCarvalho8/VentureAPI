![Sistema de Requisição e Coleta](https://southcentralus1-mediap.svc.ms/transform/thumbnail?provider=spo&farmid=192809&inputFormat=png&cs=MDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtMDAwMDQ4MTcxMGE0fFNQTw&docid=https%3A%2F%2Fmy.microsoftpersonalcontent.com%2F_api%2Fv2.0%2Fdrives%2Fb!SJJrfGVRhEW02s7rXYvsfeVG_-HX6hBBnltmL013zMAj_y8sllI-RIncBPEerk5_%2Fitems%2F01QDCYR2V4NMFPIAOEYVDJJIB6VJTF7F6L%3Ftempauth%3Dv1e.eyJzaXRlaWQiOiI3YzZiOTI0OC01MTY1LTQ1ODQtYjRkYS1jZWViNWQ4YmVjN2QiLCJhcHBpZCI6IjAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDA0ODE3MTBhNCIsImF1ZCI6IjAwMDAwMDAzLTAwMDAtMGZmMS1jZTAwLTAwMDAwMDAwMDAwMC9teS5taWNyb3NvZnRwZXJzb25hbGNvbnRlbnQuY29tQDkxODgwNDBkLTZjNjctNGM1Yi1iMTEyLTM2YTMwNGI2NmRhZCIsImV4cCI6IjE3Mjg5NzIwMDAifQ.2wqn2xfnmh0uYDalKm2bt2-ckjbpGJkjd9_yL1c60bhB-6GxU6PN0Rq_zRNpB7Z6ojtLOB7rfnlCyCNkXRlSELGFPsIimUhffDzAuRS4PTOsjl2jq0cXIUntxcFQ7UKxMlS4ZZINDoxSmBC0ukmH4mCda3ukgQFOxucciZ3VzwSdoDHG1XsluOSeX8l2nq0zmvS57pAyW0qrSatbHkfK4W05O6KyvMT2XhVloFyN5BaA8ZEGx28M6fHKF3rHYpfON-NhfE5zJW7Kez6vNYDfzeOlG_ZIZUkmzB3yoq5InwjYlyn0u8Injfj3YxhO48P8meA5LDhetmT1aJMYn5DM2OChkKaOu2sbfSXhDy7yYruaOZCMLoM6pmVxjDgsS7MW.cFQ9OXo3fn0NGk-r4D4lRQmRvvsadYAuQchku352sz0%26version%3DPublished&cb=63864548528&encodeFailures=1&width=1366&height=593&action=Access)

# Sistema de Requisição e Coleta de Itens com Visão Computacional

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
