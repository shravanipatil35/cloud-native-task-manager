from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import secrets
from urllib.parse import quote_plus

db = SQLAlchemy()


def _database_uri():
    database_url = os.environ.get('DATABASE_URL')
    if database_url:
        return database_url

    password = os.environ.get('POSTGRES_PASSWORD')
    if not password:
        if os.environ.get('FLASK_ENV') == 'production':
            raise RuntimeError('POSTGRES_PASSWORD or DATABASE_URL is required in production')
        return 'sqlite:///app.db'

    username = quote_plus(os.environ.get('POSTGRES_USER', 'taskmanager'))
    database = quote_plus(os.environ.get('POSTGRES_DB', 'taskmanager_db'))
    host = os.environ.get('DB_HOST', 'postgres')
    port = os.environ.get('DB_PORT', '5432')
    return f'postgresql://{username}:{quote_plus(password)}@{host}:{port}/{database}'


def create_app():
    """Application factory function"""
    load_dotenv()

    app = Flask(
        __name__,
        template_folder='../templates',
        static_folder='../static'
    )

    production = os.environ.get('FLASK_ENV') == 'production'
    secret_key = os.environ.get('SECRET_KEY')
    if production and not secret_key:
        raise RuntimeError('SECRET_KEY is required in production')

    app.config['SECRET_KEY'] = secret_key or secrets.token_hex(32)
    app.config['SQLALCHEMY_DATABASE_URI'] = _database_uri()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_SORT_KEYS'] = False

    # Initialize extensions
    db.init_app(app)
    CORS(app)

    # Register blueprints
    from app.routes import main_bp, api_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    # Create DB tables
    with app.app_context():
        try:
            db.create_all()
            app.logger.info("Database tables created successfully")
        except Exception as e:
            app.logger.warning(f"Database init warning: {str(e)}")

    return app
