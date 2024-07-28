from init import db, ma
from marshmallow import fields

class Visited(db.Model):
    __tablename__ = "visited" # name of the table
    # table attributes
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date) # date of visit to country
    
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False) # which user visited the country
    country_id = db.Column(db.Integer, db.ForeignKey("countries.id"), nullable=False) # which country was visited

    user = db.relationship("User", back_populates="visiteds") # relation to user
    country = db.relationship("Country", back_populates="visiteds", cascade="all, delete") # relation to country

class VisitedSchema(ma.Schema):
    user = fields.Nested("UserSchema", only=["id", "name", "email"])
    country = fields.Nested("CountrySchema", exclude=["visiteds"])

    class Meta:
        fields = ( "id", "date", "user", "country" )


visited_schema = VisitedSchema()
visiteds_schema = VisitedSchema(many=True)