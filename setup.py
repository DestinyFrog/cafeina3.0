import json

from models.elementModel import ElementModel
from models.moleculaModel import MoleculaModel

MoleculaModel.drop_table()
ElementModel.drop_table()

ElementModel.create_table()
MoleculaModel.create_table()

with open("data/elements.json") as file:
	text = file.read()
	elements = json.loads(text)
	ElementModel.insert_many(elements).execute()


MoleculaModel.insert(
    uid="5ef70e4b-7ea8-4b05-8ea5-3cd43c2d9315",
	iupac_name= "água",
	popular_name= "água",
	another_names= "",
	organic= False,
	term= "HHO",
	formula= "H<2>O",
	z1= """inorganic\n\nO 1 2 3 4\nH 1\nH 2\nX 3\nX 4\n\nangV"""
).execute()

MoleculaModel.insert(
    uid="34beeae0-3b76-4193-9169-d3c8b08233f2",
	iupac_name= "amônia",
	popular_name= "amônia",
	another_names= "",
	organic= False,
	term= "HHHN",
	formula= "NH<3>",
	z1= """inorganic\n\nN 1 2 3 4\nH 1\nH 2\nH 3\nX 4\n\npirA"""
).execute()

