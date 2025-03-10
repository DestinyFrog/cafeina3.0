from peewee import IntegerField, CharField, DecimalField

from models.baseModel import BaseModel

class ElementModel(BaseModel):
	atomic_number = IntegerField( unique=True, primary_key=True )
	oficial_name = CharField()
	latin_name = CharField( null=True )
	atomic_radius = DecimalField( null=True )
	category = CharField()
	atomic_mass = DecimalField( null=True )
	eletronegativity = DecimalField( null=True )
	period = IntegerField()
	family = IntegerField()
	symbol = CharField( max_length=3 )
	fase = CharField()
	xpos = IntegerField()
	ypos = IntegerField()
	layers = CharField()
	electronic_configuration = CharField()
	oxidation_state = CharField()
	discovery_year = IntegerField( null=True )
	discovery = CharField( null=True )
	another_names = CharField()
 
	def _to_dict(self, q):
		return {
      		"atomic_number": q.atomic_number,
			"name": self._handle_names(q),
			"pos": {
				"x": q.xpos,
				"y": q.ypos
			},
			"atomic_radius": q.atomic_radius,
			"category": q.category,
			"atomic_mass": q.atomic_mass,
			"eletronegativity": q.eletronegativity,
			"period": q.period,
			"family": q.family,
			"symbol": q.symbol,
			"fase": q.fase,
			"layers": q.layers,
			"electronic_configuration": q.electronic_configuration,
			"oxidation_state": q.oxidation_state,
			"discovery_year": q.discovery_year,
			"discovery": q.discovery,
			"another_names": q.another_names
		}

	def _handle_names(self, q):
		return {
			"oficial": q.oficial_name,
			"latin": q.latin_name
		}