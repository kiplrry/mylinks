#!/usr/bin/python3
from test.user import User
from test import storage
from sqlalchemy.exc import IntegrityError


us1 = User('barry', 34)
us2 = User('kk', 22)

storage.new(us1)
storage.new(us2)


# ans = storage.get(User, 32)
# print(ans.__dict__)

try:
    storage.save()
except IntegrityError:
    print('duplicate')
    

