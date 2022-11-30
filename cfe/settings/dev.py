from .base import *
import os



# SECRET_KEY = os.environ['SECRET_KEY']
# print(os.environ.get("SECRET_KEY"))
# 
LOGIN_URL  =""
LOGOUT_REDIRECT_URL = ""
LOGIN_REDIRECT_URL = ""
REDIRECT_FIELD_NAME = "next"


# settings static

STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# MEDIA FIELDS ==> use 

MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media/"



# CLODINARY FOR MEDIA MANAGEMENT

import cloudinary
import cloudinary_storage



# CLOUDINARY_STORAGE  = {
#     # ENVIRON LATTER
#     "CLOUD_NAME":config('CLOUDINARY_CLOUD_NAME'),
#     "API_KEY":config("CLOUDINARY_API_KEY"),
#     "API_SECRET":config("CLOUDINARY_API_SECRET")
# }


# DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"



# EMAIL SESSTINGS

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
EMAIL_HOST = config("EMAIL_HOST")
EMAIL_HOST_USER="apikey"
EMAIL_HOST_PASSWORD=config("BLOGO_EMAIL_API_KEY")
EMAIL_PORT = config("EMAIL_PORT")
EMAIL_USE_TLS=True


AUTH_USER_MODEL = "account.CustomUser"
