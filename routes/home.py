import os
from flask import render_template

def home():
    caminho = r'E:\Mega'
    pastas = []

    itens = os.listdir(caminho)
    print(itens)

    # Para cada item na lista de itens
    for item in itens:
        # Junta o caminho 'caminho' com o nome do item para formar o caminho completo
        caminho_completo = os.path.join(caminho, item)
        print(caminho_completo)
        
        # Verifica se o caminho completo corresponde a uma pasta (diretório)
        if os.path.isdir(caminho_completo):
            # Se for uma pasta, adiciona o nome do item na lista 'pastas'
            pastas.append(item)
    print(pastas)
    return render_template('home.html', pastas=pastas)