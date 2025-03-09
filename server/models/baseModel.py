from peewee import Model

from database.conn import get_conn

class BaseModel(Model):
	class Meta:
		database = get_conn()
  
	def _to_dict(self, _):
		return {}
  
	def get_all(self):
		query = self.select()
		return list(map(self._to_dict, query))