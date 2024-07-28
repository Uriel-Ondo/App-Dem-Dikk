from flask import Flask, send_from_directory
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS
from models import db

app = Flask(__name__)
CORS(app)  # Activer CORS pour toute l'application

app.config.from_object('config.Config')

db.init_app(app)

# Swagger UI configuration
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Dakar Dem Dikk API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Import blueprints
from routes.buses import buses_bp
from routes.trajets import trajets_bp
from routes.horaires import horaires_bp

app.register_blueprint(buses_bp, url_prefix='/buses')
app.register_blueprint(trajets_bp, url_prefix='/trajets')
app.register_blueprint(horaires_bp, url_prefix='/horaires')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/create_db', methods=['GET'])
def create_db():
    with app.app_context():
        db.create_all()
    return "Tables created successfully!"

if __name__ == '__main__':
    app.run(debug=True)
