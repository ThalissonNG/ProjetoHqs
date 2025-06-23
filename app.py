from flask import Flask
from Routes.home import home
from Routes.login import login
from Routes.home_hq import hq

app = Flask(__name__)
app.secret_key = 'THALISSON'

app.add_url_rule('/', view_func=login, methods=['GET', 'POST'])
app.add_url_rule('/home', view_func=home)
app.add_url_rule('/home/<nome_pasta>', view_func=hq, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0'
    )