from peewee import CharField, BooleanField, UUIDField, TextField

from models.baseModel import BaseModel
from z1.plugins.defaultPlugin import DefaultPlugin
from z1.plugins.organicPlugin import OrganicPlugin
from z1.plugins.lewisPlugin import LewisPlugin

class MoleculaModel(BaseModel):
	uid = UUIDField( primary_key=True )
	iupac_name = CharField()
	popular_name = CharField()
	another_names = CharField()
	organic = BooleanField()
	term = CharField()
	formula = CharField()
	z1 = TextField()
 
	def _to_dict(self, q):
		return {
			"uid": q.uid,
			"name": self._handle_names(q),
			"organic": q.organic == "organic",
			"formula": q.formula
		}

	def _handle_names(self, q):
		return {
			"iupac": q.iupac_name,
			"popular": q.popular_name,
			"another": q.another_names
		}

	def _get_svg(self, q, mode:str):
		Plugin = DefaultPlugin

		match (mode):
			case "organic":
				Plugin = OrganicPlugin

			case "lewis":
				Plugin = LewisPlugin
	
		z1 = q.z1
		crude_svg = Plugin(z1).get_svg()
		build_svg = crude_svg.build()
		return build_svg