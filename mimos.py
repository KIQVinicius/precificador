import streamlit as st

# Título do aplicativo
st.title("Cálculo de Custo")

# Entrada para o número de etapas
num_etapas = st.number_input("Quantas etapas o processo possui?", min_value=1, step=1, value=1)

# Lista para armazenar os custos de cada etapa
etapas = []

# Formulário para entrada dos custos por etapa
for i in range(num_etapas):
    with st.expander(f"Etapa {i + 1}"):
        nome_etapa = st.text_input(f"Nome da Etapa {i + 1}")
        custo_etapa = st.number_input(f"Custo da Etapa {i + 1} (R$)", min_value=0.0, step=0.01)
        etapas.append({"nome": nome_etapa, "custo": custo_etapa})

# Entrada para a margem de lucro
margem_lucro = st.slider("Margem de Lucro (%)", min_value=0, max_value=100, value=20)

# Botão para calcular o custo final
if st.button("Calcular Custo Final e Preço Final"):
    # Calculando o custo total
    custo_total = sum(etapa["custo"] for etapa in etapas)
    preco_final = custo_total * (1 + margem_lucro / 100)

    # Exibindo os resultados
    st.subheader("Resultados")
    st.write(f"**Custo Total do Processo: R$ {custo_total:.2f}**")
    st.write(f"**Preço Final (com {margem_lucro}% de lucro): R$ {preco_final:.2f}**")

    # Detalhando os custos por etapa
    st.subheader("Detalhamento dos Custos por Etapa")
    for i, etapa in enumerate(etapas):
        nome = etapa["nome"]
        custo = etapa["custo"]
        st.write(f"- Etapa {i + 1}: {nome} - Custo: R$ {custo:.2f}")
