import uuid
import datetime

from app.main import db
from app.main.model.logs import Log


def save_new_log(data):
    #log = Log.query.filter_by(logger=data['logger']).first()
    
    if data['logger'] is not None:
        new_log = Log(
            public_id=str(uuid.uuid4()),
            logger=data['logger'],
            level=data['level'],
            msg=data['msg'],
            created_at=datetime.datetime.utcnow()
        )
        save_changes(new_log)
        response_object = {
            'status': 'success',
            'message': 'Successfully saved.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'logger is not specified...',
        }
        return response_object, 409


def get_all_logs():
    return Log.query.all()


def get_a_log(public_id):
    return Log.query.filter_by(public_id=public_id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()