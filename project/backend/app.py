# ------------------------
# Standard Imports
# ------------------------
from flask import Flask, jsonify
from flask_cors import CORS
from flask_caching import Cache
import logging
import sys
import os

# ------------------------
# Protection System
# ------------------------
try:
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
    from protection.protection import _P, _INSTANCE_ID, _CONTEXT_HASH, initialize_protection
    from protection.obfuscate_utils import _O
    _PROTECTED = True
    if not initialize_protection():
        logging.warning("Environment validation notice - running in limited mode")
except ImportError as e:
    logging.error(f"Protection modules not found: {e}")
    _PROTECTED = False
    _INSTANCE_ID = "unprotected"

# ------------------------
# Logging Configuration
# ------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# ------------------------
# Create Flask App
# ------------------------
app = Flask(__name__)

# ------------------------
# CORS Configuration
# ------------------------
CORS(app, resources={r"/*": {"origins": "*"}})

# ------------------------
# Database Configuration
# ------------------------
import os
from models import db

# Use SQLite for development if PostgreSQL is not available
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "sqlite:///ecopackai.db"
)

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# ------------------------
# Cache Configuration
# ------------------------
cache = Cache(config={"CACHE_TYPE": "SimpleCache"})
cache.init_app(app)

# ------------------------
# Register Middleware
# ------------------------
# from middleware.auth import require_api_key

# @app.before_request
# def check_api_key():
#     # Skip auth for health check and OPTIONS requests (CORS preflight)
#     if request.path == "/health" or request.method == "OPTIONS":
#         return None
#     return require_api_key()

# Temporarily disable API key authentication for development
@app.before_request
def check_api_key():
    # Environment validation check
    if _PROTECTED:
        try:
            if not _P.verify(False):
                logging.warning("Environment validation notice")
        except Exception as e:
            logging.warning(f"Validation check: {e}")
    pass

# ------------------------
# Register API Routes
# ------------------------
from flask import request
from predict import register_prediction_routes
register_prediction_routes(app)

# ------------------------
# Health Check Endpoint
# ------------------------
@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "UP",
        "service": "EcoPackAI API",
        "message": "Service is running successfully"
    }), 200

# ------------------------
# Run the Flask App
# ------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
