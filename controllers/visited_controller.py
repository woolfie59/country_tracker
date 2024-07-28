from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.visited import Visited, visited_schema, visiteds_schema
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

@visited_controller.route('/visiteds', methods=['POST'])
def create_visited():
    try:
        data = request.get_json()
        new_visited = Visited(
            date=data['date'],
            user_id=data['user_id'],
            country_id=data['country_id']
        )
        db.session.add(new_visited)
        db.session.commit()
        return visited_schema.dump(new_visited), 201
    except Exception as e:
        return {'message': f'An error occurred: {e}'}, 500

@visited_controller.route('/visiteds/<int:id>', methods=['PUT'])
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