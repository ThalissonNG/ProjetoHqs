import os
from flask import render_template, redirect, url_for

def hq(nome_pasta):
    caminho = r'E:\Mega'+'\\'+nome_pasta

    pastas = os.listdir(caminho)
    arquivos = [item for item in pastas if os.path.isfile(os.path.join(caminho, item))]
    # print(arquivos)

    return render_template('home_hq.html', arquivos=arquivos)