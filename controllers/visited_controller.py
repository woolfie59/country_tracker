from sqlalchemy.exc import IntegrityError
from datetime import datetime
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.visited import Visited, visited_schema, visiteds_schema
from models.user import User
from models.country import Country

visiteds_bp = Blueprint("visiteds", __name__, url_prefix="/visiteds")
visited_controller = Blueprint('visited_controller', __name__)

@visited_controller.route('/visiteds', methods=['GET'])
def get_all_visiteds():
    visiteds = Visited.query.all()
    return visiteds_schema.dump(visiteds)

@visited_controller.route('/visiteds/<int:id>', methods=['GET'])
def get_visited(id):
    visited = Visited.query.get_or_404(id)
    return visited_schema.dump(visited)

visiteds_bp = Blueprint('visiteds', __name__)

@visiteds_bp.route('/visiteds', methods=['POST'])
def add_visited():
    data = request.get_json()

    if not data.get('date') or not data.get('user_id') or not data.get('country_id'):
        return {"error": "Missing required fields: date, user_id, country_id"}, 400

    try:
        new_visit = Visited(
            date=datetime.strptime(data['date'], '%Y-%m-%d').date(),
            user_id=data['user_id'],
            country_id=data['country_id']
        )
        db.session.add(new_visit)
        db.session.commit()
        return {"message": "Visit added successfully"}, 201
    except IntegrityError as e:
        db.session.rollback()
        return {"error": str(e.orig)}, 500
    except Exception as e:
        return {"error": str(e)}, 500

@visited_controller.route('/visiteds/<int:id>', methods=['PUT', 'PATCH'])
def update_visited(id):
    try:
        data = request.get_json()
        visited = Visited.query.get_or_404(id)
        if 'date' in data:
            visited.date = data['date']
        if 'user_id' in data:
            visited.user_id = data['user_id']
        if 'country_id' in data:
            visited.country_id = data['country_id']
        db.session.commit()
        return visited_schema.dump(visited)
    except Exception as e:
        return {'message': f'An error occurred: {e}'}, 500

@visited_controller.route('/visiteds/<int:id>', methods=['DELETE'])
def delete_visited(id):
    try:
        visited = Visited.query.get_or_404(id)
        db.session.delete(visited)
        db.session.commit()
        return {'message': 'Visited record deleted successfully'}
    except Exception as e:
        return {'message': f'An error occurred: {e}'}, 500