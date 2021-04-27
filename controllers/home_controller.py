from flask import request, jsonify

from models.user import User
from daos.user_dao_impl import UserDAOImpl as u_dao


def route(app):
    @app.route("/", methods=['GET', 'POST'])
    def hello():
        return "Welcome to the Tuition System!"

    @app.route("/users", methods=['POST'])
    def get_user():
        user = User.json_parse(request.json)
        # Bad practice here
        returned_user = u_dao.get_user(user)
        return jsonify(returned_user)
