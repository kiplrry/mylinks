#!/usr/bin/python3
from testuser import User
from testdb import Storage
from sqlalchemy.exc import IntegrityError

storage = Storage()
storage.start()
# Barry =  User( id=31, name='barry', age='20')
# jamie =  User( id=30, name='Jamie', age='19')
# storage.new(Barry)
# storage.new(jamie)


ans = storage.get(User, 32)
print(ans.__dict__)

# try:
#     storage.save()
# except IntegrityError:
#     print('duplicate')
    

