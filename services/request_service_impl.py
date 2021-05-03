from flask import jsonify

from services.request_service import RequestService
from daos.request_dao_impl import RequestDAOImpl
from models.request import Request


class RequestServiceImpl(RequestService):

    @classmethod
    def create_request(cls, employee_id, amount):
        return RequestDAOImpl.create_request(int(employee_id), int(amount)), 201

    @classmethod
    def get_all_requests_for_employee(cls, employee_id):
        requests = [request.json() for request in RequestDAOImpl.get_all_requests_for_employee(int(employee_id))]
        return requests

    @classmethod
    def get_request_with_id(cls, employee_id, request_id):
        ret = [request.json() for request in RequestDAOImpl.get_request_with_id(int(employee_id), int(request_id))]
        if not ret:
            return "Not a valid request", 404
        return ret

    @classmethod
    def update_request_with_id(cls, employee_id, request_id, req_funds, added_info, is_denied, denied_reason,
                               is_approved):
        ret = RequestDAOImpl.update_request_with_id(int(employee_id), int(request_id), int(req_funds),
                                                    jsonify(added_info), bool(is_denied), jsonify(denied_reason),
                                                    bool(is_approved))
        if not ret:
            return "Not a valid request"
        return ret

    @classmethod
    def delete_request_with_id(cls, employee_id, request_id):

        return RequestDAOImpl.delete_request_with_id(int(employee_id), int(request_id))
