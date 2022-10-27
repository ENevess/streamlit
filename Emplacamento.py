# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import openpyxl

#Configuração do tamanho da tela
st.set_page_config(layout="wide")

#path do arquivo
file = "Saida_Emplacamentos.xlsx"


#Add Título e logo 
st.image('Logo DAF - HiRes.png', width= 64)
st.title("DAF - Histórico")



#Carrega Dataset e faz limpeza.
df = pd.read_excel(file)
df['CNPJ'] = df['CPFCNPJPROPRIETARIO'].astype(str)
df = df.drop(['CPFCNPJPROPRIETARIO'], axis=1)
df = df[['CNPJ','NOMEPROPRIETARIO','Total Chassis','Total DAF','Total Mercedes', 'Total Iveco','Total Volkswagen', 'Total Scania', 'Total Volvo']]

#

#Função para filtrar
def filter(cnpj):
    filter = df["CNPJ"]==cnpj
    df_filtered = df.loc[df['CNPJ'] == str(cnpj)]
    if len(df_filtered) == 0:
        st.write("CNPJ não encontrado. ")
        st.write("Verifique o número preenchido.")
        st.write("Ou CNPJ sem emplacamentos DAF ou modelos concorrentes")
    else:
        st.write(df_filtered)


#Display Informação inicial
cnpj = st.text_input("Digite o CNPJ para pesquisa  (Apenas números)")
st.write("Exemplo: 14775519000156")

if cnpj:
    filter(cnpj)

