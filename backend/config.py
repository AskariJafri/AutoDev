import os

CONFIG = {
    'DB_HOST': os.environ['DB_HOST'],
    'DB_PORT': int(os.environ.get('DB_PORT', 5432)),
    'DB_USER': os.environ['DB_USER'],
    'DB_PASSWORD': os.environ['DB_PASSWORD'],
    'PAGE_SIZE': 20,
    'PAGE_NUMBER': 1
}