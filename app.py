import streamlit as st

st.title("🔬 Microscópio Virtual de Mineralogia")

st.write("Projeto desenvolvido por Tatiane Fernandes")

mineral = st.selectbox(
    "Selecione um mineral",
    ["HM", "HE", "Magnetita", "Goethita", "Quartzo"]
)

st.write(f"Mineral selecionado: {mineral}")

if st.button("🎲 Gerar Nova Amostra"):
    st.success("Nova amostra gerada!")

