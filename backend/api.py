from flask import Blueprint, request, jsonify
from services import search

search_blueprint = Blueprint('search', __name__)

@search_blueprint.route('/search', methods=['GET'])
def get_search_results():
    query = request.args.get('query')
    limit = int(request.args.get('limit', 10)) if 'limit' in request.args else None
    offset = int(request.args.get('offset', 0)) if 'offset' in request.args else None

    results, meta = search(query, limit=limit, offset=offset)
    return jsonify({
        'results': [result.to_dict() for result in results],
        'meta': {
            'total_records': meta['count'],
            'current_page': meta['page_number']
        }
    })