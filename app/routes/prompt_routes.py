from flask import Blueprint
from controllers.prompt_controller import process_prompt, test_func

prompt_bp = Blueprint('prompt', __name__)

prompt_bp.route('/', methods=['GET'])(test_func)
prompt_bp.route('/inference', methods=['POST'])(process_prompt)
