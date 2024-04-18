from server.api.views import api
from models import User
from flask_restx import Resource
from flask import jsonify, make_response, request, abort
from flask_login import login_required



@api.route('/users')
class UserClass:
    def get(self):
        """get all users"""
        all_users = User.all()
        if all_users:
            json_users = [user.to_dict() for user in all_users]
            print(json_users)
            return jsonify({'users': json_users})
        return jsonify({'users': 'none'})



@api.route('/users', methods=['POST'], strict_slashes=False)
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
# @app_views.route('/users', methods=['POST'], strict_slashes=False)
# def create_user():
#     """get all users"""
#     if not request.get_json():
#         abort(400, 'not valid json data')
#     data = request.get_json()
#     required = set(["name", "username", "age"])
#     if all(data.values()) and required & set(data) == required:
#         user = User(**data)
#         res = user.save()
#         print(res)
#         if not res:
#             print('not res')
#             abort(409)
    
    
#         return make_response(jsonify({'user_id':res}), 200)
#     abort(403, 'missing data')
