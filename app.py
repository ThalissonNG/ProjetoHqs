from flask import Flask
from routes.home import home
from routes.login import login
from routes.home_hq import hq

app = Flask(__name__)
app.secret_key = 'THALISSON'

app.add_url_rule('/', view_func=home, methods=['GET', 'POST'])
app.add_url_rule('/home', view_func=home)
app.add_url_rule('/pagina', view_func=hq, methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5001
    )