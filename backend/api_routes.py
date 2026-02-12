from flask import Blueprint
from backend.models import User, Activity

api_bp = Blueprint('api', __name__)

@api_bp.route('/ping')
def ping():
    return {'status': 'OK'}