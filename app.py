from dotenv import load_dotenv
from flask import Flask

from routes.elementRoute import route as ElementRoute
from routes.moleculaRoute import route as MoleculaRoute

load_dotenv()

app = Flask(__name__)

app.register_blueprint(ElementRoute)
app.register_blueprint(MoleculaRoute)

@app.route("/")
def hello():
	return "Hello, World!"

if __name__ == '__main__':
	app.run(debug=True)