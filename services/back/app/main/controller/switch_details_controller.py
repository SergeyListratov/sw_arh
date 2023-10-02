from app.main.controller.grid_super_controller import GridSuperController
from app.main.model.switch import Switch
from app.main.util.decorator import token_required
from sqlalchemy import or_, func, and_


from ..util.dto import SwitchDetailsGridDto

api = SwitchDetailsGridDto.api
_details = SwitchDetailsGridDto.details


@api.route('/details/<ip>')
@api.param('ip', 'Switch ip')
class SwitchDetails(GridSuperController):
    
    def search(self, data, search_str):
        if search_str:
            s = f'%{search_str}%'
            data = data.where(or_(Switch.model.like(s), Switch.serial.like(s)))
        
        return data
    
    @api.doc('switch details')
    @token_required
    @api.marshal_with(_details)
    def post(self, ip):
        query = Switch.query.filter(Switch.ip == ip)
        
        result = self.filter_sort_paginate(query)
        result['ip'] = ip
                
        return result