from app.main.controller.grid_super_controller import GridSuperController
from app.main.model.switch import Switch
from app.main.util.decorator import token_required
from sqlalchemy import or_, func, and_


from ..util.dto import SwitchGroupedDto

api = SwitchGroupedDto.api
_switch = SwitchGroupedDto.switch

@api.route('/grouped')
class SwitchList(GridSuperController):
    
    def search(self, data, search_str):
        if search_str:
            s = f'%{search_str}%'
            data = data.where(or_(Switch.ip.like(s), Switch.model.like(s), Switch.serial.like(s)))
        
        return data
    
    @api.doc('list_of_grouped_switches')
    @token_required
    @api.marshal_with(_switch)
    def post(self):
        subq = Switch.query.with_entities(
            Switch.ip,
            func.max(Switch.created_on).label('maxdate')
        ).group_by(Switch.ip).subquery('t2')
        
        query = Switch.query.join(
            subq,
            and_(
                Switch.ip == subq.c.ip,
                Switch.created_on == subq.c.maxdate
            )
        )
                
        return self.filter_sort_paginate(query)