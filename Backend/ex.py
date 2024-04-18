#!/usr/bin/python3

from models import User, Link

user = User.query.filter_by(username='rero').first()

link = Link(name='insta', url='insta.com/ll', descr='my insta')

link.user = user
print(user)