import os

SECRET_KEY = "dev"
DEBUG = True
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "pass"
DB_NAME = "grupo16"

# Google Configuration
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)
