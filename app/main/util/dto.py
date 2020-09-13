from flask_restx import Namespace, fields


class LogDto:
    api = Namespace('logs', description='logs related operations')
    logs = api.model('logs', {
        'logger': fields.String(required=True, description='logger name'),
        'level': fields.String(required=False, description='level {info, debug, error}'),
        'msg': fields.String(required=True, description='message info'),
        'public_id': fields.String(description='logger Identifier')
    })

class HealthDto:
    api = Namespace('logs', description='logs related operations')
    health = api.model('logs', {
        'logger': fields.String(required=True, description='logger name'),
        'level': fields.String(required=False, description='level {info, debug, error}'),
        'msg': fields.String(required=True, description='message info'),
        'public_id': fields.String(description='logger Identifier')
    })