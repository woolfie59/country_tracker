from init import db, ma
from marshmallow import fields

class Country(db.Model):
    __tablename__ = "countires"

    id = db.Column(db.Integer, primary_key=True)
    capital = db.Column(db.String) # the capital of the country
    visited = db.Column(db.Boolean, nullable=False) # has been visited, true or false

    user = db.relationship("User", back_populates="countries")
    visited = db.relationship("Visited", back_populates="countires")

class CountrySchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["name"])
    visited = fields.Nested("CountrySchema", exclude=("country"))

    class Meta:
        fields = ("id", "capital", "visited", "user")

country_schema = CountrySchema()
countries_schema = CountrySchema(many=True)
