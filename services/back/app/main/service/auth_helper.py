from app.main.model.user import User
from typing import Dict, Tuple

from ldap3 import Server, Connection, ALL
from config import d_name, ldsp_server, root_dn, adm_group

class Auth:
    @staticmethod
    def global_ldap_authentication(user_name, user_pwd, group=adm_group):
        flag = False
        ldap_user_name = user_name.strip()
        ldap_user_pwd = user_pwd.strip()

        server = Server(ldsp_server, get_info=ALL)
        connection = Connection(server,
                                user=f'{ldap_user_name}{d_name}',
                                password=ldap_user_pwd)
        if not connection.bind():
            return flag
        else:
            search_filter = f"(sAMAccountName={user_name})"
            search_attribute = ['memberOf']
            connection.search(search_base=root_dn,
                              search_filter=search_filter,
                              attributes=search_attribute)
            flag = any(map(lambda i: group in i, connection.response[0]['attributes']['memberOf']))

        return flag

    @staticmethod
    def login_user(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
        try:
            # тестовые данные
            
            user_name = data.get('login')
            password = data.get('password')
            
            if Auth.global_ldap_authentication(user_name, password):
                auth_token = User.encode_auth_token(user_name, password)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'api_token': auth_token#.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500


    @staticmethod
    def check_token(new_request):
        # get the auth token
        auth_header = new_request.headers.get('Authorization')
        auth_header = auth_header.replace('Bearer ', '')
        
        payload = User.decode_auth_token(auth_header)
        
        return Auth.login_user(payload)
            
    @staticmethod
    def get_user_info(auth_token):
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if resp:
                response_object = {
                    'id': '',
                    'name': resp['login'],
                    'roles': []
                }
                return response_object, 200
            response_object = {
                'status': 'fail',
                'message': resp
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401
            