from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        raise Exception("LA CONCHA DEL CREADOR DE FLASK")
        return "sarasa"
    return decorated_function
