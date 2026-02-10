from flask import current_app
from sqlalchemy import func
from database import db
from functools import wraps

def paginate(limit=10, offset=None):
    def decorator(func):
        @wraps(func)
        def wrapper(self, query, *args, **kwargs):
            limit = current_app.config['PAGE_SIZE']
            if limit is not None and limit < 1:
                raise ValueError('Invalid page size')
            if offset is not None and offset < 0:
                raise ValueError('Invalid offset')
            # Add pagination support using SQLAlchemy's paginate method
            return db.session.query(func).paginate(query, limit=limit, offset=offset)
        return wrapper
    return decorator

# Use the @paginate decorator to implement pagination in search function
@paginate()
def search(query, limit=10):
    return db.session.query(model).filter(func.lower(model.name) == func.lower(query)).all()