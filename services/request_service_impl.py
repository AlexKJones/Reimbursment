from flask import jsonify

from services.request_service import RequestService
from daos.request_dao_impl import RequestDAOImpl
from models.request import Request


class RequestServiceImpl(RequestService):

    @classmethod
    def create_request(cls, employee_id, employee_name, request_for, req_funds, req_type, info, pass_grade, event_date,
                       submit_date):
        return RequestDAOImpl.create_request(int(employee_id), str(employee_name), str(request_for), int(req_funds),
                                             str(req_type), str(info), int(pass_grade), int(event_date),
                                             int(submit_date)), 201

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
        ret = RequestDAOImpl.update_request_with_id(int(employee_id), int(request_id), int(req_funds), added_info,
                                                    is_denied, denied_reason, is_approved)
        if not ret:
            return "Not a valid request"
        return ret

    @classmethod
    def delete_request_with_id(cls, employee_id, request_id):

        return RequestDAOImpl.delete_request_with_id(int(employee_id), int(request_id))
