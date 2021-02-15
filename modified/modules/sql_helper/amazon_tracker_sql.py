
from sqlalchemy import Column, String, UnicodeText

from modified.modules.sql_helper import BASE, SESSION


class Anp(BASE):
    __tablename__ = "anp"
    amazon_url = Column(UnicodeText, primary_key=True)
    budget = Column(String(14))

    def __init__(self, amazon_url, budget):
        self.amazon_url = amazon_url
        self.budget = budget


Anp.__table__.create(checkfirst=True)

def add_new_tracker(amazon_url, budget: int):
    tracker_adder = Anp(str(amazon_url), str(budget))
    SESSION.add(tracker_adder)
    SESSION.commit()

def get_tracker_info(amazon_url: str):
    try:
        s__ = SESSION.query(Anp).get(str(amazon_url))
        return str(s__.budget), str(s__.amazon_url)
    finally:
        SESSION.close()
        
def is_tracker_in_db(amazon_url: str):
    try:
        s__ = SESSION.query(Anp).get(str(amazon_url))
        if s__:
            return str(s__.budget)
    finally:
        SESSION.close()
        
        
def get_all_urls():
    stark = [r.amazon_url for r in SESSION.query(Anp).all()]
    SESSION.close()
    return stark

def get_all_tracker():
    s = SESSION.query(Anp).all()
    SESSION.close()
    return s


def rm_tracker(amazon_url: str):
    warner = SESSION.query(Anp).get(str(amazon_url))
    if warner:
        SESSION.delete(warner)
        SESSION.commit()
