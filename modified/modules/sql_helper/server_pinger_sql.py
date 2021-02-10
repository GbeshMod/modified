
from sqlalchemy import Column, UnicodeText

from modified.modules.sql_helper import BASE, SESSION


class Serverpinger(BASE):
    __tablename__ = "serverpinger"
    url = Column(UnicodeText, primary_key=True)

    def __init__(self, url):
        self.url = url


Serverpinger.__table__.create(checkfirst=True)


def add_ping(url):
    pinger = Serverpinger(url)
    SESSION.add(pinger)
    SESSION.commit()


def rmping(url):
    rmpinger = SESSION.query(Serverpinger).get(url)
    if rmpinger:
        SESSION.delete(rmpinger)
        SESSION.commit()


def get_all_url():
    stark = SESSION.query(Serverpinger).all()
    SESSION.close()
    return stark


def is_ping_indb(url):
    try:
        return SESSION.query(Serverpinger).filter(Serverpinger.url == url).one()
    except:
        return None
    finally:
        SESSION.close()
