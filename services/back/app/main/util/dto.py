from flask_restx import Namespace, fields


class SwitchDto:
    api = Namespace('switch', description='switch related operations')
    switch = api.model('switch', {
        'ip': fields.String(required=True, description='ip'),
        'model': fields.String(required=True, description='model'),
        'serial': fields.String(required=True, description='serial'),
        'created_on': fields.Date(required=True, description='user Identifier'),
    })

class PaginationDto:
    api = Namespace('pagination', description='')
    pagination = api.model('pagination', {
        'itemsPerPage': fields.Integer,
        'order': fields.String,
        'page': fields.Integer,
        'pagesCount': fields.Integer,
        'sort': fields.String(required=False),
        'totalCount': fields.Integer
    })

class SwitchGroupedDto:
    api= Namespace('switch', description='switch related operations')
    switch = api.model('switch', {
        'data': fields.List(fields.Nested(SwitchDto.switch)),
        'pagination': fields.Nested(PaginationDto.pagination)
    })

class SwitchDetailsDto:
    api = Namespace('switch', description='switch related operations')
    switch = api.model('switch', {
        'id': fields.String(required=True),
        'model': fields.String(required=True, description='model'),
        'serial': fields.String(required=True, description='serial'),
        'created_on': fields.Date(required=True, description='user Identifier'),
    })

class SwitchDetailsGridDto:
    api= Namespace('switch', description='switch related operations')
    details = api.model('switch', {
        'ip': fields.String(),
        'data': fields.List(fields.Nested(SwitchDetailsDto.switch)),
        'pagination': fields.Nested(PaginationDto.pagination)
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'login': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
