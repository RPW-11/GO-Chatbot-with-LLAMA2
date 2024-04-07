from flask import Blueprint
from controllers.user_controller import *


user_bp = Blueprint("user", __name__)

user_bp.route("/register", methods=['POST'])(register_user)
