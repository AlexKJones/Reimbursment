from flask import jsonify, request
from werkzeug.exceptions import abort

from daos import employee_dao_impl
from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_unavailable import ResourceUnavailable
from models.employee import Employee
from services import employee_service
from services.employee_service import EmployeeService
from logger import log


def route(app):
    @app.route("/employees", methods=['GET'])
    def get_all_employees():
        log(f"Indexing all employees")
        return jsonify(EmployeeService.all_employees()), 200

    @app.route("/employees/<employee_id>", methods=['GET'])
    def get_employee(employee_id):
        try:
            employee = EmployeeService.get_employee_by_id(int(employee_id))
            if employee is None:
                log(f"get error for employee id={employee_id}")
                return 'No employee found', 404
            log(f"Used get request for employee id={employee_id}")
            return jsonify(employee.json()), 200
        except ValueError as e:
            return "Not a valid ID", 400  # Bad Request
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/employees", methods=["POST"])
    def post_employee():
        try:
            log(f"Creating new employee")
            employee = Employee.json_parse(request.json)
            employee = EmployeeService.create_employee(employee)
            return jsonify(employee.json()), 201
        except ValueError:
            return 'Invalid input', 400

    @app.route("/employees/<employee_id>", methods=["PUT"])
    def put_employee(employee_id):
        try:
            log(f"Updating employee info for employee id={employee_id}")
            employee = Employee.json_parse(request.json)
            employee.employee_id = int(employee_id)
            employee = EmployeeService.update_employee(employee)
            return jsonify(employee.json()), 200
        except ResourceNotFound:
            return 'employee id not found', 404
        except ValueError:
            return 'Invalid Input', 201

    @app.route("/employees/<employee_id>", methods=["DELETE"])
    def del_employee(employee_id):
        try:
            ret = EmployeeService.get_employee_by_id(int(employee_id))
            if ret is None:
                log(f"Failed to find and delete employee")
                return 'Employee not found', 404
            log(f"Deleted employee with employee id={employee_id}")
            EmployeeService.delete_employee(int(employee_id))
            return 'Employee Deleted', 205
        except ResourceNotFound:
            return 'employee id not found', 404
        except ValueError:
            return 'Invalid Input', 201
