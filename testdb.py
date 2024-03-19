
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from testuser import Base

class Storage():

    __session = None
    engine = None

    def __init__(self):
        USER = 'larry'
        PASS = 'pass'
        HOST = 'localhost'
        DB = 'testing'
        self.engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(USER, PASS, HOST, DB)
                                      )

    def start(self):
        Base.metadata.create_all(bind= self.engine)
        Session = sessionmaker(bind=self.engine, expire_on_commit=False)
        scope = scoped_session(Session)
        self.__session = scope
    
    def new(self, obj=None):
        if obj is None:
            return
        self.__session.add_all(obj)
        
    def get(self, cls, id=None):
        ans = self.__session.query(cls).filter_by(id=id).first()
        return ans

    def save(self):
        self.__session.commit()
        self.__session.close()
