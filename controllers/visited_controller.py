from datetime import datetime

from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from init import db
from models.visited import Visited, visited_schema, visiteds_schema
from controllers.country_controller import countries_bp

visiteds_bp = Blueprint("visiteds", __name__, url_prefix="/visiteds")
visiteds_bp.register_blueprint(countries_bp)


@visiteds_bp.route("/")
def get_all_visiteds():
    stmt = db.select(Visited).order_by(Visited.date.desc())
    visiteds = db.session.scalars(stmt)
    return visiteds_schema.dump(visiteds)


@visiteds_bp.route("/<int:visited_id>")
def get_one_visited(visited_id):
    stmt = db.select(Visited).filter_by(id=visited_id)
    visited = db.session.scalar(stmt)
    if visited:
        return visited_schema.dump(visited)
    else:
        return {"error": f"Visit with id {visited_id} not found"}, 404


@visiteds_bp.route("/", methods=["POST"])
@jwt_required()
def create_visit():
    body_data = request.get_json()
    date_visited_str = body_data.get("date_visited")
    if date_visited_str:
        try:
            date_visited = datetime.strptime(date_visited_str, "%Y-%m-%d").date()
        except ValueError:
            return {"error": "Invalid date format. Please use YYYY-MM-DD"}, 400
    else:
        date_visited = datetime.today().date()

    visited = Visited(
        date=date_visited,
        user_id=get_jwt_identity()
    )

    db.session.add(visited)
    db.session.commit()
    return visited_schema.dump(visited)


@visiteds_bp.route("/<int:visited_id>", methods=["DELETE"])
@jwt_required()
def delete_visited(visited_id):
    stmt = db.select(Visited).filter_by(id=visited_id)
    visited = db.session.scalar(stmt)
    if visited:
        db.session.delete(visited)
        db.session.commit()
        return {"message": f"Visit deleted successfully"}
    
    else:
        return {"error": f"Visit with id {visited_id} not found"}, 404
    
@visiteds_bp.route("/<int:visited_id>", methods=["PUT", "PATCH"])
@jwt_required()
def update_visited(visited_id):
    body_data = request.get_json()
    stmt = db.select(Visited).filter_by(id=visited_id)
    visited = db.session.scalar(stmt)
    if visited:
        visited.date = body_data.get("date") or visited.date
        db.session.commit()
        return visited_schema.dump(visited)
    else:
        return {"errer": f"Visit with id {visited_id} not found"}, 404