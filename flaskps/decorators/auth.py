from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return "test"

    return decorated_function
