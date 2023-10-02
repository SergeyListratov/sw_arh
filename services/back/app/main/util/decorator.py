from functools import wraps

from flask import request

from app.main.service.auth_helper import Auth
from typing import Callable


def token_required(f) -> Callable:
    @wraps(f)
    def decorated(*args, **kwargs):

        data, status = Auth.check_token(request)
        token = data.get('data')

        if status != 200:
            return data, status

        return f(*args, **kwargs)

    return decorated