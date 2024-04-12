from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from waitress import serve
from constants import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS, MAX_FILE_SIZE
from routes.prompt_routes import prompt_bp
from routes.user_routes import user_bp
from routes.document_routes import document_bp
from database import db
import llm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.config['MAX_CONTENT_LENGTH'] = MAX_FILE_SIZE

CORS(app)

print("Connecting to the database...")
db.init_app(app)

from models.user import User
from models.document import Document

with app.app_context():
    print("Initializing the Large Language Model")
    llm.init()

    migrate = Migrate(app, db)

    app.register_blueprint(prompt_bp, url_prefix='/prompt')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(document_bp, url_prefix='/document')


print(f"Server is ready")



if __name__ == '__main__':  # Running the app

    serve(app, host='127.0.0.1', port=8080)






