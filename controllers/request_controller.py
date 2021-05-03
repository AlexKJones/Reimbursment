from flask import jsonify, request
from werkzeug.exceptions import abort

from daos.request_dao_impl import RequestDAOImpl
from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_unavailable import ResourceUnavailable
from models.request import Request
from services.employee_service import EmployeeService
from logger import log
from services.request_service_impl import RequestServiceImpl


def route(app):
    @app.route("/employees/<employee_id>/requests", methods=['POST'])
    def create_employee_request(employee_id):
        try:
            amount = request.json["amount"]
            if employee_id.isdigit() and amount == int or float:
                employee = EmployeeService.get_employee_by_id(employee_id=int(employee_id))
                if employee == "Not a valid ID":
                    return "No such employee exist", 404
                log(f"Creating request for employee id={employee_id}")
                return jsonify(RequestServiceImpl.create_request(employee_id=employee_id, amount=amount)), 201
            else:
                raise ValueError

        except ValueError:
            return "No such employee exist", 404

    @app.route("/employees/<employee_id>/requests/", methods=['GET'])
    def get_employee_requests(employee_id):
        try:
            if employee_id.isdigit():
                log(
                    f"Indexing requests for a employee")
                return jsonify(
                    RequestServiceImpl.get_all_requests_for_employee(employee_id))
            else:
                raise ValueError
            if ret == []:
                raise ValueError
            else:
                return jsonify(ret)
        except ValueError:
            return "no employee exists", 404

    @app.route("/employees/<employee_id>/requests/<request_id>", methods=['GET'])
    def get_employee_request_with_id(employee_id, request_id):
        try:
            if employee_id.isdigit() and request_id.isdigit():
                employee = EmployeeService.get_employee_by_id(employee_id=employee_id)
                ret = [request.json() for request in
                       RequestDAOImpl.get_request_with_id(int(employee_id), int(request_id))]
                if not ret:
                    log(f"Could not find request for employee id={employee_id}")
                    return "Not a valid request", 404
            log(f"Viewing request for employee id={employee_id} with request id={request_id}")
            return jsonify(RequestServiceImpl.get_request_with_id(int(employee_id), int(request_id)))
        except ValueError:
            return "no employee exists", 404

    @app.route("/employees/<employee_id>/requests/<request_id>", methods=['PUT'])
    def update_request_with_id(employee_id, request_id):
        try:
            amount = request.json["amount"]
            if employee_id.isdigit() and request_id.isdigit() and amount:
                ret = [request.json() for request in
                       RequestDAOImpl.get_request_with_id(int(employee_id), int(request_id))]
                if not ret:
                    log(f"Failed to update request for employee id={employee_id}")
                    return "Not a valid request", 404
                log(f"Updating request for employee id={employee_id} with request id={request_id}")
                return RequestServiceImpl.update_request_with_id(employee_id, request_id, amount)
            else:
                raise ValueError
        except ValueError:
            return "Not a valid ID", 404

    @app.route("/employees/<employee_id>/requests/<request_id>", methods=['DELETE'])
    def delete_employee_request_with_id(employee_id, request_id):
        try:
            if employee_id.isdigit() and request_id.isdigit():
                log(f"Deleted request for employee id={employee_id}")
                return RequestServiceImpl.delete_request_with_id(employee_id, request_id)
            else:
                raise ValueError
        except ValueError:
            return "Not a valid ID", 404