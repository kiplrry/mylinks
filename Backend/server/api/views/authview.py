from server.api.views import app_views
from models import User
from flask_login import login_user
from flask import request, abort, jsonify




@app_views.route('/auth', methods=['POST'], strict_slashes=False)
def login_post():
    if not request.get_json():
        abort(404, 'not valid json data')
    data: dict = request.get_json()
    required = set(["name"])
    if 'username' not in data:
        abort(404, 'missing username')
    user = User.query.filter_by(username=data['username']).first()
    if not user:
        abort(404)
    remember = data.get('remember')
    status = login_user(user, remember=remember)
    return jsonify({'done': status, 'user': user.to_dict()})