from app.main.controller.grid_super_controller import GridSuperController
from app.main.model.switch import Switch
from app.main.util.decorator import token_required
from flask_restx import Resource
from sqlalchemy.orm.exc import NoResultFound
from flask import send_file


from ..util.dto import SwitchDetailsGridDto

api = SwitchDetailsGridDto.api
_details = SwitchDetailsGridDto.details


@api.route('/download/<id>')
@api.param('id', 'Switch id')
class SwitchDownload(Resource):
    
    @api.doc('switch download')
    @token_required
    @api.marshal_with(_details)
    def post(self, id):
        try:
            found = Switch.query.filter(Switch.id == id).one()
            
            return send_file(found.file_path, mimetype='text/csv', as_attachment=True)
        except NoResultFound:
            response_object = {
                'status': 'fail',
                'message': 'Not found.'
            }
            return response_object, 404