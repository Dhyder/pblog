import os 

class Config:
  SECRET_KEY= os.environ.get("SECRET_KEY")
  DATABASE_URL='postgresql+psycopg2://postgres:787898@localhost/cielito'
  UPLOADED_PHOTOS_DEST = "app/static"
  SQLALCHEMY_TRACK_MODIFICATIONS = True
  # SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:787898@localhost/cielito"

  # email configurations
  MAIL_SERVER='smtp.gmail.com'
  MAIL_PORT= 465
  MAIL_USE_SSL=True
  MAIL_USE_TLS= False
  MAIL_USERNAME= os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD= os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    
  SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:787898@localhost/cielito_test"

class DevConfig(Config):
  SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:787898@localhost/cielito"
  DEBUG = True

config_options = {
  "development": DevConfig,
  "production": ProdConfig,
  "test": TestConfig
}