from flask import request, jsonify
from services.user_services import get_answer


def process_prompt():
    body = request.get_json()
    ans = get_answer(body.get('question'))
    return jsonify({ 'answer' : ans })