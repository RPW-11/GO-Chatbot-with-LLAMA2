from flask import Blueprint
from controllers.prompt_controller import *


prompt_bp = Blueprint('prompt', __name__)

prompt_bp.route('/inference', methods=['POST'])(process_prompt)
