#!/usr/bin/python3

from models import User, Link


print(User.query.filter_by(username='ijdo').first())

