from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask.cli import FlaskGroup
from waitress import serve
from constants import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from routes.prompt_routes import prompt_bp
from database import db
import llm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS

CORS(app)

print("Connecting to the database...")
db.init_app(app)

from models.user import User

with app.app_context():
    print("Initializing the Large Language Model")
    llm.init()

    migrate = Migrate(app, db)

    app.register_blueprint(prompt_bp, url_prefix='/prompt')


print(f"Server is ready")



if __name__ == '__main__':  # Running the app

    serve(app, host='127.0.0.1', port=8080)






