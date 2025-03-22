import os
from flask import Flask, render_template, jsonify
from app.routes import app_routes

# Initialize Flask app
app = Flask(__name__)
app.config.from_object('config.Config')

# Register Blueprints
app.register_blueprint(app_routes)

# Home Route
@app.route('/')
def index():
    return render_template('index.html')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
