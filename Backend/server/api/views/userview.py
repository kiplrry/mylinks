from server.api.views import app_views
from helpers.decorators import role_required
from models import User
from flask import jsonify, make_response, request, abort
from flask_login import login_required, current_user


@app_views.route('/users', methods=['GET'], strict_slashes=False)
@login_required
def get_users():
    """get all users
    ---
    definitions:
      Users:
        type: object
        properties:
          all_users:
            type: object
    responses:
      200:
        description: Get the users in the database
        schema:
          $ref: '#/definitions/Users'
    

    """
    all_users = User.all()
    if all_users:
        json_users = [user.to_dict() for user in all_users]
        print(json_users)
        return jsonify({'users': json_users})
    return jsonify({'users': 'none'})



@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """get all users"""
    if not request.get_json():
        abort(400, 'not valid json data')
    data = request.get_json()
    required = set(["name", "username", "age"])
    if all(data.values()) and required & set(data) == required:
        user = User(**data)
        res = user.save()
        print(res)
        if not res:
            print('not res')
            abort(409)
    
    
        return make_response(jsonify({'user_id':res}), 200)
    abort(403, 'missing data')

@app_views.route('/users/<id_or_username>', methods=['GET'], strict_slashes=False)
@login_required
def get_user(id_or_username=None):
    """get a single user"""
    if not id_or_username:
        abort(409)
    user = User.get(id_or_username=id_or_username)
    if not user:
        abort(404, 'user not found')
    return make_response(jsonify({'user': user.to_dict()}))

@app_views.route('/users', methods=['PUT'], strict_slashes=False)
def update_user():
    """get all users"""
    if not request.get_json():
        abort(400, 'not valid json data')
    data = request.get_json()
    required = set(["name", "username", "age"])
    if all(data.values()) and required & set(data) == required:
        user = User(**data)
        res = user.save()
        print(res)
        if not res:
            print('not res')
            abort(409)
    
    
        return make_response(jsonify({'user_id':res}), 200)
    abort(403, 'missing data')

@app_views.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    user_det : dict = current_user.to_dict()
    details = {}
    details['user'] = user_det
    details['links'] = current_user.get_links()

    return make_response(jsonify(details))
