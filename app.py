from flask import Flask
from routes.home import home
from routes.login import login

app = Flask(__name__)
app.secret_key = 'THALISSON'

app.add_url_rule('/', view_func=login, methods=['GET', 'POST'])
app.add_url_rule('/home', view_func=home)

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0'
    )