import calendar
import logging
import datetime
import gevent
from peewee import SqliteDatabase
import config

DB = None


def background_service():
    """
    :return:
    """
    ctr = 0
    while 1:
        # do stuff here
        # logging.debug('{}'.format(ctr))
        ctr += 1
        gevent.sleep(1)


def get_db():
    """Get Application Database
    :return: DB
    """
    global DB
    if DB is None:
        DB = SqliteDatabase(config.db)

    return DB


def default_json_decode(obj):

    if isinstance(obj, datetime.datetime):
        if obj.utcoffset() is not None:
            obj = obj - obj.utcoffset()
    millis = int(
        calendar.timegm(obj.timetuple()) * 1000 +
        obj.microsecond / 1000
    )

    return millis
