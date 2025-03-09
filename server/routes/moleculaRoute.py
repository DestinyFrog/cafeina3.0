from flask import Blueprint, jsonify, make_response, request

from models.moleculaModel import MoleculaModel
from config import API_PREFIX

route = Blueprint('molecula', __name__, url_prefix=f'{API_PREFIX}/molecula')

@route.route("/", methods=["GET"])
def get_all_molecula():
	data = MoleculaModel().get_all()
	return jsonify(data)

@route.route("/<uuid:uid>", methods=["GET"])
def get_one_molecula_by_uid(uid:str):
	moleculaModel = MoleculaModel()
	query = moleculaModel.get( MoleculaModel.uid == uid )
	data = moleculaModel._to_dict(query)
	return jsonify(data)

@route.route("/<uuid:uid>/svg", methods=["GET"])
def get_one_molecula_svg_by_uid(uid:str):
	mode = request.args.get('mode') or "default"
 
	moleculaModel = MoleculaModel()
	query = moleculaModel.get( MoleculaModel.uid == uid )
	svg = moleculaModel._get_svg(query, mode)

	resp = make_response(svg)
	resp.mimetype = "image/svg+xml"
	return resp