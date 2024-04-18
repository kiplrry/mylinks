from functools import wraps
from flask_login import current_user
from flask import abort
def role_required(*roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.role in roles:
                return func(*args, **kwargs)
            abort(409)
        return wrapper
    return decorator
