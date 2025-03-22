# app/config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///logs.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LOG_FILE = 'app_logs.log'
    MODEL_PATH = 'app/detection_model/model.pkl'
    SAMPLE_DATA_PATH = 'data/sample_data.csv'

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
