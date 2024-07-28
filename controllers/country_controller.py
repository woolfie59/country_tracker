from datetime import date

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.country import Country, country_schema, countries_schema
from models.visited import Visited

country_controller = Blueprint('country_controller', __name__)

countries_bp = Blueprint("countries", __name__, url_prefix="/<int:visit_id>/countires")

@country_controller.route('/country/<country_name>', methods=['GET'])
def check_country_visited(country_name):

    try:
        country = Country.query.filter_by(name=country_name).first()

        if not country:
            return jsonify({'message': 'Country not found'}), 404
        
        visited = Visited.query.filter_by(name=country_name).first()
        
        if visited:
            return jsonify({'country': country_name, 'visited': True})
        else:
            return jsonify({'country': country_name, 'visited': False})
        
    except Exception as e:
        return jsonify({'message': f'An error occured: {e}'}), 500