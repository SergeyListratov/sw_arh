from flask import request
from flask_restx import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto
from typing import Dict, Tuple

api = AuthDto.api
user_auth = AuthDto.user_auth

@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self) -> Tuple[Dict[str, str], int]:
        # get the post data
        post_data = request.json
        return Auth.login_user(data=post_data)


@api.route('/user-info')
class UserInfo(Resource):
    """
    User Information
    """
    @api.doc('get user information')
    def post(self) -> Tuple[Dict[str, str], int]:
        # get auth token
        auth_header = request.headers.get('Authorization')
        auth_header = auth_header.replace('Bearer ', '')
        return Auth.get_user_info(auth_header)