from peewee import CharField, BooleanField, UUIDField

from models.baseModel import BaseModel
from z1.plugins.defaultPlugin import DefaultPlugin

class MoleculaModel(BaseModel):
	uid = UUIDField( primary_key=True )
	iupac_name = CharField()
	popular_name = CharField()
	another_names = CharField()
	organic = BooleanField()
	term = CharField()
	formula = CharField()
	z1 = CharField()
 
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

	def _get_svg(self, q):
		z1 = q.z1
		crude_svg = DefaultPlugin(z1).get_svg()
		build_svg = crude_svg.build()
		return build_svg