from flask import Flask
from models.user import db
from controllers.user_controller import *

from config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://' + DB_USER + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_NAME 
db.init_app(app)

app.register_blueprint(user_api)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)