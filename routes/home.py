from mega import Mega
from flask import render_template

def home():
    mega = Mega()
    m = mega.login(email= 'manoelthalisson28@gmail.com', password='Liferkill123*')

    detils = m.get_user()
    print(detils['name'])
    print(detils['email'])
    arquivos = m.get_files()
    print(arquivos)
    # mega.login()

    return render_template('home.html')