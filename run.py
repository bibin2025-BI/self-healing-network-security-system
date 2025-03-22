# run.py
from app import app
from app.config import config
import os

def main():
    env = os.environ.get('FLASK_ENV', 'development')
    app.config.from_object(config[env])
    print(f"Starting the application in {env} mode.")
    app.run(host='0.0.0.0', port=5000, debug=app.config['DEBUG'])

if __name__ == '__main__':
    main()
