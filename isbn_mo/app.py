import os
from flask import Flask
from dotenv import load_dotenv
from models.task import db
from controllers.task_controller import *

load_dotenv()

dbUri = os.getenv("DB_URI")
print(dbUri)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = dbUri
db.init_app(app)

app.register_blueprint(task_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4200)
