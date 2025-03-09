from flask import Blueprint, jsonify

from models.elementModel import ElementModel
from config import API_PREFIX

route = Blueprint('element', __name__, url_prefix=f'{API_PREFIX}/element')

@route.route("/", methods=["GET"])
def get_all_element():
    data = ElementModel().get_all()
    return jsonify(data)

@route.route("/<int:atomic_number>", methods=["GET"])
def get_one_element_by_atomic_number(atomic_number:int):
    elementModel = ElementModel()
    query = elementModel.get( ElementModel.atomic_number == atomic_number )
    data = elementModel._to_dict(query)
    return jsonify(data)