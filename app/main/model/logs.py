from .. import db
import datetime
from ..config import key
from sqlalchemy.sql import func


class Log(db.Model):
    """ log Model for storing different fib, fact response/request log related details """
    __tablename__ = "logs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # auto incrementing
    logger = db.Column(db.String) # the name of the logger. (e.g. log for fib, fact)
    level = db.Column(db.String) # info, debug, or error?
    public_id = db.Column(db.String(100), unique=True)
    msg = db.Column(db.String) # any custom log
    created_at = db.Column(db.DateTime, default=func.now()) # the current timestamp


    #def __init__(self, public_id=None, logger=None, level=None, msg=None, created_at=None):
     #   self.logger = logger
      #  self.level = level
       # self.msg = msg
        #self.public_id = public_id
        #self.created_at = created_at
    
    def __unicode__(self):
        return self.__repr__()
    
    def __repr__(self):
        return "<Log: %s - %s>" % (self.created_at.strftime('%m/%d/%Y-%H:%M:%S'), self.msg[:50])