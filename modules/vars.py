#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "24228334"))
API_HASH = environ.get("API_HASH", "b84ddbab901f0f148a585e8607995b97")
BOT_TOKEN = environ.get("BOT_TOKEN", "8503807209:AAEOKlMoF7cRBaFv23Ml39yvXiSMgtQDDWw")

OWNER = int(environ.get("OWNER", "7681453297"))
CREDIT = environ.get("CREDIT", "DANNY")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '7681453297').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '7681453297').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))


