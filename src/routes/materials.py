"""
Materials route
"""

from flask import Blueprint, send_from_directory
from utils.response import response
from pymongo import MongoClient

UPLOAD_FOLDER = './materials'
MATERIALS = Blueprint('materials', __name__)
CLIENT = MongoClient('mongodb:27017')
DB = CLIENT.api


@MATERIALS.route('/materials/<company>/<product_id>/<path:filename>')
def get_file(company, product_id, filename):
    try:
        return send_from_directory(UPLOAD_FOLDER + '/' + company + '/' + product_id, filename)
    except Exception:
         return response('No such file', 404)
