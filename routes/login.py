from flask import render_template, request, redirect, url_for, flash
import json
import os

def login():
    # def procurar_usuario(user, senha):
    #     caminho_base = os.path.dirname(__file__)
    #     caminho_json = os.path.join(caminho_base,'usuarios.json')
    #     with open(caminho_json, 'r', encoding='utf-8') as f: dados = json.load(f)
    #     print(f"Dados do json :{dados}")

    # procurar_usuario('admin','admin')

    if request.method == 'POST':        
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        # print(usuario, senha)

        if usuario == 'admin' and senha == 'admin':
            return redirect(url_for('home'))
        else:
            flash('Usuário ou senha inválidos. Tente novamente.', 'login')
    return render_template('login.html')