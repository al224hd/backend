"""
Categories Route
"""

from flask import Blueprint, request
from dal.categories import dal_get_categories, dal_create_category
from utils.response import response
from exceptions.WrongCredentials import WrongCredentials
from exceptions.AlreadyExists import AlreadyExists

CATEGORIES = Blueprint('CATEGORIES', __name__)


@CATEGORIES.route('/categories')
def get_categories():
    """Gets all available categories"""
    categories_data = dal_get_categories()
    return response(categories_data, 200)


@CATEGORIES.route('/categories', methods=['POST'])
def create_categories():
    """Creates a new category"""

    try:

        dal_create_category(request.form)
        return response('Category created', 201)

    except AttributeError:
        return response('Broken JWT', 400)
    except WrongCredentials:
        return response('Invalid credentials', 400)
    except AlreadyExists:
        return response('Category exists', 409)