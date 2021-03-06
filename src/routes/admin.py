"""
Admin routes
"""

from flask import Blueprint, request
from utils.response import response
from dal.admin import auth_and_return_admin, create_default_admin

ADMIN = Blueprint('admin', __name__)



@ADMIN.route('/admins', methods=['POST'])
def admin_actions():
    """When requested create admin account"""

    if request.method == 'POST':
        create_default_admin()
    return response('Admin account has been created', 201)


@ADMIN.route('/admins/auth', methods=['POST'])
def admin_auth():
    """Authenticates an admin"""

    if request.method == 'POST':
        try:

            encoded_data = auth_and_return_admin(request.form)
            return response('Successfully logged in as admin', 200, {'token': encoded_data.decode('utf-8')})

        except AttributeError:
            return response('Wrong credentials', 400)
