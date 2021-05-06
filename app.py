from flask import Flask
from controllers import front_controller as fc
from flask_cors import CORS

app = Flask(__name__)

fc.route(app)
CORS(app)
if __name__ == '__main__':
    app.run(debug=True)
