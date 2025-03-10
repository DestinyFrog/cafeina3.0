from flask import Flask, send_from_directory
from flask_cors import CORS

from routes.elementRoute import route as ElementRoute
from routes.moleculaRoute import route as MoleculaRoute
from config import PORT, MODE

app = Flask(__name__)
CORS(app)

app.register_blueprint(ElementRoute)
app.register_blueprint(MoleculaRoute)

@app.route('/')
def send_index():
	return send_from_directory('../build', "index.html")

@app.route('/<path:path>')
def send_build(path):
	return send_from_directory('../build', path)

if __name__ == '__main__':
	app.run( port=PORT, debug=(MODE == "development") )