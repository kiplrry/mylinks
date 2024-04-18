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
    parameters:
        - name: auth
          in: header
          description: auth key
          required: false
          schema: 
              properties:
                session:
                  description: key
                  example: skadaksdassd
                  type: string
    responses:
        '200': 
            description: ok
        '404':
            description: user not found
    """
    all_users = User.all()
    if all_users:
        json_users = [user.to_dict() for user in all_users]
        print(json_users)
        return jsonify({'users': json_users})
    return jsonify({'users': 'none'})



@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """create a user
    ---
    parameters:
        - name: user details
          in: body
          description: details of the user being created
          required: true
          schema: 
              properties:
                name:
                  description: name
                  example: larry
                  type: string
                username:
                  description: username
                  example: larry
                  type: string
                age:
                  description: age
                  example: 33
                  type: int
                gender:
                  description: username
                  example: M
                  type: enum
    responses:
        '201': 
            description: user created succesfully
            schema : 
                type: object
                properties:
                    user_id:
                        type: string
                        description: array of users
                example: 
                    user_id: 4cf71711-a47e-4067-8258-cae8253eb413
    """
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
    """get a single user
    ---

    parameters:
        - name: id_or_username
          in: path
          description: username or id of user being searched
          required: true
          schema: 
              properties:
                id_or_username:
                  description: username or id
                  example: 4cf71711-a47e-4067-8258-cae8253eb413
                  type: string
    responses:
        '200': 
            description: user found
            schema : 
                type: object
                properties:
                    user:
                        type: array
                        description: array of users
                        items: object
                example: 
                    user: {
                            "created_at": "Wed, 17 Apr 2024 10:46:59 GMT",
                            "email": null,
                            "gender": "M",
                            "id": "408e6954-aa4f-4551-8805-dac9bd29fd3c",
                            "name": "ian",
                            "password": "123456",
                            "role": "user",
                            "updated_at": "Wed, 17 Apr 2024 10:46:59 GMT",
                            "username": "iadjjdo"
                            }
        '404':
            description: user not found

    """
    if not id_or_username:
        abort(409)
    user = User.get(id_or_username=id_or_username)
    if not user:
        abort(404, 'user not found')
    return make_response(jsonify({'user': user.to_dict()}))

@app_views.route('/users/<id_or_username>', methods=['PUT'], strict_slashes=False)
@login_required
def update_user(id_or_username=None):
    """get a single user
    ---

    parameters:
        - name: id_or_username
          in: path
          description: username or id of user being searched, provided by admin only
          required: false
          schema: 
              properties:
                id_or_username:
                  description: username or id
                  example: 4cf71711-a47e-4067-8258-cae8253eb413
                  type: string
        - name: params
          in: body
          description: json params to be updated
          required: true
          schema:
                type: object
                example: {"name": "john",
                            "age": 22}
    responses:
        '200': 
            description: user updated
            schema : 
                type: object
                properties:
                    user:
                        type: array
                        description: array of users
                        items: object
                example: 
                    user: {
                            "created_at": "Wed, 17 Apr 2024 10:46:59 GMT",
                            "email": null,
                            "gender": "M",
                            "id": "408e6954-aa4f-4551-8805-dac9bd29fd3c",
                            "name": "ian",
                            "password": "123456",
                            "role": "user",
                            "updated_at": "Wed, 17 Apr 2024 10:46:59 GMT",
                            "username": "iadjjdo"
                            }
        '404':
            description: user not found

    """
    if not request.get_json():
        abort(400, 'not valid json data')
    user: User = current_user
    if id_or_username and user.role == 'admin':
        user = User.get(id_or_username=id_or_username)
    data = request.get_json()
    res: User = user.update(**data)
    print(res)
    if not res:
        print('user not found')
        abort(404)
    return make_response(jsonify({'user':res.to_dict()}), 200)

@app_views.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    user_det : dict = current_user.to_dict()
    details = {}
    details['user'] = user_det
    details['links'] = current_user.get_links()

    return make_response(jsonify(details))
