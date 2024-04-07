from flask import Blueprint
from controllers.document_controller import *


document_bp = Blueprint('document', __name__)

document_bp.route('/get-all', methods=['GET'])(get_all)
document_bp.route('/add', methods=['POST'])(add)