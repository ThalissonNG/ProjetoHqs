from flask import render_template, request, redirect, url_for, flash

def login():
    if request.method == 'POST':
        
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        print(usuario, senha)

        if usuario == 'admin' and senha == 'admin':
            return redirect(url_for('home'))
        else:
            flash('Usuário ou senha inválidos. Tente novamente.', 'login')
    return render_template('login.html')