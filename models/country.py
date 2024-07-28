from init import db, ma
from marshmallow import fields
from marshmallow.validate import And

class Country(db.Model):
    __tablename__ = "countries"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False) # name of the country
    visited = db.Column(db.Boolean, nullable=False) # has been visited, true or false

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    
    def __init__(self, name, visited=False, user_id=False):
        self.name = name
        self.visited = visited
        self.user_id = user_id

    user = db.relationship("User", back_populates="countries") # relation to the user model
    visiteds = db.relationship("Visited", back_populates="country") # relation to the visited model

class CountrySchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["name"])
    visiteds = fields.List(fields.Nested("VisitedSchema", exclude=["country"]))

    class Meta:
        fields = ("id", "name", "visited", "user")

country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)
