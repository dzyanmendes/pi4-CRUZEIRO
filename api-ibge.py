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
totalNascimento = data_grafico["nascimento"]
incrementoPop = data_grafico["incrementoPopulacional"]
totalObito = data_grafico["obito"]
dataUpdate = data_json["horario"]
df= json_normalize(data_json["projecao"])
df2= json_normalize(data_json["projecao"]["periodoMedio"])
df3 = data_grafico
st.header('SIAD - IBGE - UNIVESP')
st.bar_chart(df)
st.bar_chart(df2)
st.bar_chart(df3)