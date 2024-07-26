from init import db, ma
from marshmallow import fields

class Visited(db.Model):
    __tablename__ = "visited"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date) # date of country visit
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship('User', back_populates='visiteds')

class VisitedSchema(ma.Schema):

    user = fields.Nested('UserSchema', only=["id", "name", "email"])

    class Meta:
        fields = ( "id", "date", "user" )



visited_schema = VisitedSchema()
visiteds_schema = VisitedSchema(many=True)