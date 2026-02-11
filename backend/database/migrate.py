from flask_migrate import Migrator
from app import db

migrator = Migrator(db)

def migrate():
    migrator.up()