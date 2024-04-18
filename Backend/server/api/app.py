#!/usr/bin/python3

from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage, User
from flask_login import LoginManager
from server.api.views import app_views
from flasgger import Swagger


app =Flask(__name__)

app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.config['SECRET_KEY'] = 'supersecret key'
cors = CORS(app, origins='*')
login_manager = LoginManager()
login_manager.init_app(app=app)
swag = Swagger(app=app)

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.filter_by(id=user_id).first()

@app.teardown_appcontext
def closedb(error):
    '''close the db after session ends'''
    storage.close()

@app.errorhandler(404)
def err_404(error):
    '''404 error handler'''
    return make_response(jsonify({'error': 'not found',
                                  "details": error.description,
                                  "err_code": error.code}),
                         404)

@app.errorhandler(409)
def err_409(err):
    '''conflict err'''
    return make_response(jsonify({'error': 'duplicate',
                                  "details": err.description,
                                  "err_code": err.code}),
                         409)

@app.errorhandler(405)
def err_405(err):
    """unauthorized"""
    print(err)
    return make_response(jsonify({'error': "unauthorized",
                                  "details": err.description,
                                  "err_code": err.code}
                                  ), 405)



if __name__ == "__main__":
    app.run(debug=True, threaded=True, host='0.0.0.0')