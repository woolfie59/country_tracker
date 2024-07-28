from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.country import Country, country_schema, countries_schema
from models.visited import Visited

country_controller = Blueprint('country_controller', __name__)

@country_controller.route('/country/<country_name>', methods=['GET'])
def check_country_visited(country_name):
    try:
        country = Country.query.filter_by(name=country_name).first()
        if not country:
            return {'message': 'Country not found'}, 404

        visits = Visited.query.filter_by(country_id=country.id).all()
        if visits:
            return {'country': country_name, 'visited': True}
        else:
            return {'country': country_name, 'visited': False}

    except Exception as e:
        return {'message': f'An error occurred: {e}'}, 500