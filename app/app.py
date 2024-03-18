from flask import Flask
from routes.prompt_routes import prompt_bp

app = Flask(__name__)

app.register_blueprint(prompt_bp, url_prefix='/prompt')


if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=5000, debug=True)






