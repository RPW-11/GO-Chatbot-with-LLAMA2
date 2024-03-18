from flask import Flask
from waitress import serve
from routes.prompt_routes import prompt_bp
import llm

llm.init()

app = Flask(__name__)
app.register_blueprint(prompt_bp, url_prefix='/prompt')



if __name__ == '__main__':  # Running the app
    serve(app, host='127.0.0.1', port=8080)






