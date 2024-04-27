from os import environ


# BOT CONFIG
API_ID = environ.get("API_ID", 21165589)  # api id
API_HASH = environ.get("API_HASH", "8cc762f4873e84a7cf0cbfd66a07244b")  # api hash
BOT_TOKEN = environ.get("BOT_TOKEN", "7046411772:AAHPnRpW32IdLE2SoeUHP_bZpUkpeDy09EQ")  # bot token

# REDIS
REDIS_HOST = environ.get("REDIS_HOST", "redis-11906.c325.us-east-1-4.ec2.redns.redis-cloud.com")  # redis host uri
REDIS_PORT = environ.get("REDIS_PORT", 11906)  # redis port
REDIS_PASSWORD = environ.get(
    "REDIS_PASSWORD", "bIZ1Tn3cxgLq0mLzVqwSvu7lqt5c7M1t"
)  # redis password


ADMINS = [1676244457]
OWNER_ID = 2048030675  # Replace with your Telegram user ID
PRIVATE_CHAT_ID = -1002117369410  # CHAT WHERE YOU WANT TO STORE VIDEOS
USER_CHANNEL = -1002145872194
DUMP_CHANNEL = -1002018602619


# Config
COOKIE = environ.get("COOKIE", "YeF7XCeteHuiL845rTAgb6K8eyyTcwk8lnaSyMTD")
