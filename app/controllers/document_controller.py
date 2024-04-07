from flask import request, jsonify
from services.user_services import add_document, get_all_documents


def get_all():
    return jsonify(get_all_documents())


def add():
    body = request.get_json()
    status = add_document(body.get('user_id'), body.get('title'))

    if status:
        return jsonify("Success")
    return jsonify("Error")