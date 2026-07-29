from flask import Flask, render_template
from config import config
from models import db

def create_app(config_name='default'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)

    # Register blueprints
    from routes.main_routes import main
    from routes.auth_routes import auth
    from routes.admin_routes import admin
    from routes.chatbot_routes import chatbot

    app.register_blueprint(main)
    app.register_blueprint(auth)
    app.register_blueprint(admin)
    app.register_blueprint(chatbot)

    # Create database tables
    with app.app_context():
        db.create_all()
        _seed_admin(app)

    # Error handlers
    @app.errorhandler(404)
    def not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def server_error(e):
        return render_template('500.html'), 500

    return app


def _seed_admin(app):
    """Create a default admin account if none exists."""
    from models import User
    admin = User.query.filter_by(role='admin').first()
    if not admin:
        admin_user = User(name='Administrator', email='admin@hospital.com', role='admin')
        admin_user.set_password('admin123')
        db.session.add(admin_user)
        db.session.commit()
        print("✅ Default admin created: admin@hospital.com / admin123")


if __name__ == '__main__':
    app = create_app('development')
    app.run(debug=True, host='0.0.0.0', port=5000)
