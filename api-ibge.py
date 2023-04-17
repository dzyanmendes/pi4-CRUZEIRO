import urllib3
import streamlit as st
import json 
import matplotlib.pyplot  as plt
import numpy as np
import requests
import pandas as pd
from pandas import json_normalize 
url = urllib3.PoolManager()
urlIBGE = "https://servicodados.ibge.gov.br/api/v1/projecoes/populacao/BR"
response = url.request('GET', urlIBGE)
data_response = response.data.decode("utf-8")
data_json = json.loads(data_response)
data_populacao = data_json["projecao"]
data_grafico = data_json["projecao"]["periodoMedio"]
dataUpdate = data_json["horario"]
df= json_normalize(data_json["projecao"])
df2 = data_grafico
st.header('SIAD - IBGE - UNIVESP')
st.markdown('Este sistema tem por objetivo, facilitar a visualização e centralização de consultas de informações do IBGE')
if st.sidebar.button("População/Nascimentos/Óbitos"):
 st.header("Projeção Populacional")
 st.bar_chart(df)
 st.bar_chart(df2)
 st.markdown('Ultima Consulta:')
 st.text(dataUpdate)