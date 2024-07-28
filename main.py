import os

from flask import Flask

from init import db, ma, bcrypt, jwt

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")

    app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    from controllers.cli_controller import db_commands
    app.register_blueprint(db_commands)

    from controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    from controllers.visited_controller import visiteds_bp
    app.register_blueprint(visiteds_bp)

    from controllers.country_controller import country_controller
    app.register_blueprint(country_controller)

    if __name__ == '__main__':
        app.run(debug=True)

    return app