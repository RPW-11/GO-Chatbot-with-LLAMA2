from flask import request, jsonify
from services.user_services import register


def register_user():
    body = request.get_json()
    status = register(body.get('username'))

    if status:
        return jsonify("Success")
    return jsonify("Register Error")
    