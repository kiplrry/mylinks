#!/usr/bin/python3

from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
from server.api.views.authview import *
from server.api.views.userview import *
