from init import db, ma
from marshmallow import fields


class User(db.Model):
    # name of table
    __tablename__ = "users"

    # attributes of the table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    visiteds = db.relationship("Visited", back_populates="user")
    countries = db.relationship("Country", back_populates="user")

class UserSchema(ma.Schema):
    visiteds = fields.List(fields.Nested('VisitedSchema', exclude=["user"]))
    countries = fields.List(fields.Nested('CountrySchema', exclude=["user"]))
    class Meta:
        fields = ("id", "name", "email", "password", "is_admin", "visiteds", "countries")


# to handle a single user object
user_schema = UserSchema(exclude=["password"])

# to handle a list of user objects
user_schema = UserSchema(many=True, exclude=["password"])