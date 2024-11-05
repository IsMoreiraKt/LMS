from dotenv import load_dotenv
import os



load_dotenv()



class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False



class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL_DEV")
    DEBUG = True


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL_PROD")
    DEBUG = False