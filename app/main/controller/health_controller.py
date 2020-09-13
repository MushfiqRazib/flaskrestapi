from flask import request
from flask import jsonify
from flask_restx import Resource
from ..util.dto import HealthDto
from ..service.logs_service import save_new_log, get_all_logs, get_a_log

api = HealthDto.api
_health = HealthDto.health

@api.route('/health')
@api.response(404, 'Log is not found.')
class Log(Resource):
    @api.doc('get all logs')
    @api.marshal_with(_health)
    def get(self):
        """get all logs"""
        alllogs = get_all_logs()
        if alllogs is not None:
            api.abort(404)
        else:
            return alllogs