from flask import request, jsonify
from services.user_services import add_document, get_all_documents, get_filtered_documents, delete_document_by_id


def get_all():
    args = request.args
    page, per_page = int(args.get('page', 1)), int(args.get('per_page', 10))
    return jsonify(get_all_documents(page=page, per_page=per_page))


def get_documents_by_filters():
    args = request.args
    tags, search_term = args.getlist('tags'), args.get('search_term')
    documents = get_filtered_documents(filter_dict={'tags': tags, 'search_term': search_term})
    return jsonify(documents)


def delete_document():
    args = request.args
    id = args.get('id')
    status = delete_document_by_id(document_id=id)

    if status:
        return jsonify("Success")
    return jsonify("Error")


def add():
    status = False
    try:
        form = request.form
        files = request.files
        status = add_document(form.get('user_id'), form.get('title'), form.get('topic'), files=files)
        return jsonify("Success"), 200
    except Exception as e:
        if not status:
            return jsonify({'error': str(e)}), 400
        return jsonify({'error': str(e)}), 500