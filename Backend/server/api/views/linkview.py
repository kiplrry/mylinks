from server.api.views import app_views
from helpers.decorators import role_required
from models import User, Link
from flask import jsonify, make_response, request, abort
from flask_login import login_required, current_user

@app_views.route('/links', strict_slashes=False)
@login_required
@role_required('admin', 'user')
def get_links():
    user: User = current_user
    links: list = user.get_links()

    return make_response(jsonify({"links": links}))

@app_views.route('/links', methods=['POST'],strict_slashes=False)
@login_required
def create_link():
    """create link"""
    if not request.get_json():
        abort(400, 'not valid json data')
    data = request.get_json()
    required = set(["name", "url", "descr"])
    if all(data.values()) and required & set(data) == required:
        link = Link(**data)
        user: User = current_user
        link.user_id = user.id
        res = link.save()
        print(res)
        if not res:
            print('not res')
            abort(409)
    
    
        return make_response(jsonify({'link_id':res}), 200)
    abort(403, 'missing data')

@app_views.route('/links/<id>', methods=['PUT'],strict_slashes=False)
@login_required
def update_link(id):
    link : Link = Link.get(id=id)
    if link.user_id != current_user.id:
        abort(500, 'unauthorized')
    if not request.get_json():
        abort(400, 'not valid json data')
    data = request.get_json()
    link.update(**data)
    return make_response(jsonify(link.to_dict()))