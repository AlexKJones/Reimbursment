from flask import request, jsonify

from models.user import User
from daos.user_dao_impl import UserDAOImpl as u_dao
from login import login


def route(app):
    @app.route("/", methods=['GET', 'POST'])
    def hello():
        return "Welcome to the Tuition System!"

    @app.route("/login", methods=['POST'])
    def loginEmployee():
        user = User.json_parse(request.json)
        # Bad practice here
        returned_user = login.login(user)
        return jsonify(returned_user)
