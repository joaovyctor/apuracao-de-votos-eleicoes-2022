# -*- coding: utf-8 -*-
"""apuração eleições 2022.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZWmt5-U4_6796kgivYb_2kIhyea6GeQM
"""

import requests
import json
import pandas as pd
import time
from datetime import datetime

data = requests.get(
    
    'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')

json_data = json.loads(data.content)

candidato = []
partido = []
votos = []
porcentagem = []

for infos in json_data['cand']:

    if infos['seq'] in '1 2 3 4 '.split(' '):
        candidato.append(infos['nm'])
        votos.append(infos['vap'])
        porcentagem.append(infos['pvap'])

df_eleicao = pd.DataFrame(
    list(zip(candidato, votos, porcentagem)),
  columns=['Candidato', 'Nº votos', 'Porcentagem']
 )

print(df_eleicao)
time.sleep(60)