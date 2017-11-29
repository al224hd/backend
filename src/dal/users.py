from mongo_client import db_conn
import jwt

"""
    db_conn.users   => client.api.users
"""

"""Auth user by comparing username and password in users collection"""

#returns role and encoded
def auth_and_return_user(form):
    username = form['username']
    password = form['password']

    found_user = db_conn.users.find_one({'username': username, 'password': password})

    if found_user:
        payload = {'username': found_user['username'], 'role': found_user['role']}
        encoded = jwt.encode(payload, 'super-secret')
        return encoded, found_user['role']

    else:
        return AttributeError()


"""Search for user by username"""


def check_user_token(token):
    payload = jwt.decode(token, 'super-secret')
    username = payload.get('username')

    found_user = db_conn.users.find_one({'username': username})
    if found_user:
        return username
    else:
        return AttributeError()


"""Iterates users collection and returns dict of usernames with role"""


def get_users_with_role(form):
    users = []
    for user in db_conn.users.find({'role': form['role']}):
        users.append({'username': user['username']})

    return users