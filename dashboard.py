import streamlit as st
import sqlite3
import pandas as pd
from consultor import consultar_local
import time

st.title("📊 Dashboard de Ventas - Amazon Clon")
st.write("Aquí irán los análisis en tiempo real")

conn = sqlite3.connect('amazon_clon.db')

query = """
    SELECT PRODUCT_NAME, COUNT(*) as VENTAS
    FROM ventas
    GROUP BY PRODUCT_NAME
    ORDER BY VENTAS DESC
    LIMIT 5
"""
df = pd.read_sql_query(query, conn)

st.subheader("🔥 Top 5 Productos Más Vendidos")
st.dataframe(df)
st.bar_chart(df.set_index('PRODUCT_NAME'))

pregunta = st.text_input("💬 Pregunta a la IA local:")

if st.button("Consultar"):
    if pregunta:
        respuesta = consultar_local(pregunta)
        st.write(respuesta)

st.markdown('<meta http-equiv="refresh" content="1">', unsafe_allow_html=True)

conn.close()