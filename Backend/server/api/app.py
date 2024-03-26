#!/usr/bin/python3

from flask import Flask, make_response, jsonify
from flask_cors import CORS
from models import storage
from server.api.views import app_views

app =Flask(__name__)

app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, origins='*')


@app.teardown_appcontext
def closedb(error):
    '''close the db after session ends'''
    storage.close()

@app.errorhandler(404)
def err_404(error):
    '''404 error handler'''
    return make_response(jsonify({'error': 'not found'}),
                         404)

@app.errorhandler(409)
def err_409(err):
    '''conflict err'''
    return make_response(jsonify({'error': 'duplicate'}),
                         409)




if __name__ == "__main__":
    app.run(debug=True, threaded=True, host='0.0.0.0')