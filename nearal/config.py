"""nearal development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = b'\xd8\x85\r2"R_\xd1\xcc\xf8K\xa9*\xe894\x84\xbd;\xb3rMr+'
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
NEARAL_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = NEARAL_ROOT/'var'/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

