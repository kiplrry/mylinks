"""instanciates classes
 
important:: Ensure you import all necessary model classes
in this init, or else Base will not create the 
table

"""
from models.engine.dbstorage import Storage
from models.usermodels.user import User
from models.usermodels.admin import Admin
from models.resources.link import Link


storage = Storage()
storage.reload()
