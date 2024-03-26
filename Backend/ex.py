#!/usr/bin/python3

from models import User, Link

print('kkkk')

users = User.all()
try:
    u = User('f', 33, 'juj')
    u.save()
except Exception as e:
    print(e.args[0])
# print(users)

