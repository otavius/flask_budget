from flask import Blueprint, json, jsonify, abort, request
from ..models import User, Expense, db

bp_users = Blueprint('users', __name__, url_prefix='/users')


@bp_users.route('', methods=['GET'])
def index():
    users = User.query.all()
    result = []
    for user in users:
        result.append(user.serialize())
    return jsonify(result)

@bp_users.route('/create', methods=['POST'])
def create():
    if 'first_name' not in request.json or 'last_name' not in request.json or 'email' not in request.json or 'password' not in request.json or 'username' not in request.json:
        return abort(400)

    try:
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        email = request.json['email']
        password = request.json['password']
        username = request.json['username']
        
        new_user = User(first_name=first_name, last_name=last_name, email=email, password= password, username = username)
        
        new_user.insert()
        
        return jsonify(new_user.serialize())
    except:
        return abort(422)
       
@bp_users.route('/update/<int:id>', methods=['PUT'])
def update(id):
    update_user = User.query.get(id)
    # first_name = request.json['first_name']
    # last_name = request.json['last_name']
    # email = request.json['email']
    # password = request.json['password']
    username = request.json['username']    
    
    # update_user.first_name = first_name
    # update_user.last_name = last_name
    # update_user.email = email
    # update_user.password = password
    update_user.username = username
    
    db.session.commit()
    
    return jsonify(update_user.serialize())

@bp_users.route('/delete/<int:id>', methods=['Delete'])
def delete_user(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user.serialize())
    
    
    