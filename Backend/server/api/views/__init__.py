#!/usr/bin/python3
from flask_restx import Api
from flask import Blueprint
app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
api = Api(app=app_views)
from server.api.views.authview import *
from server.api.views.userview import *
from server.api.views.linkview import *
