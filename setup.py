import uuid
import json
import os

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

zones = os.listdir("data/zones")

for zone in zones:
	name, *_ = zone.split(".")
	name = name.replace("_", " ")

	with open("data/zones/"+zone) as file:
		text = file.read()

		MoleculaModel.insert(
			uid=uuid.uuid4(),
			iupac_name= "",
			popular_name= name,
			another_names= "",
			organic= False,
			term= "",
			formula= "",
			z1=text
		).execute()
