from daos.request_dao import RequestDAO
from models.employee import Employee
from models.request import Request
from util.db_connection import connection
import logging


class RequestDAOImpl(RequestDAO):
    @classmethod
    def create_request(cls, employee_id, amount):
        sql = f"insert into requests values ( default, {employee_id}, {amount} );"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        return "Request created", 201

    @classmethod
    def get_all_requests_for_employee(cls, employee_id):
        sql = f"select * from requests  where employee_id ={employee_id};"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        requests = [Request(elem[0], elem[1], float(elem[2])) for elem in records]
        return requests

    @classmethod
    def get_request_with_id(cls, employee_id, request_id):
        sql = f"SELECT * FROM(SELECT * FROM requests  where employee_id = {employee_id}) m WHERE request_id ={request_id};"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        requests = [Request(elem[0], elem[1], float(elem[2])) for elem in records]
        return requests

    @classmethod
    def update_request_with_id(cls, employee_id, request_id, req_funds, added_info, is_denied, denied_reason,
                               is_approved):
        sql = f"UPDATE requests SET req_funds ={req_funds}, added_info ={added_info}, is_denied ={is_denied}," \
              f" denied_reason ={denied_reason}, is_approved ={is_approved} WHERE request_id = {request_id}" \
              f" AND employee_id={employee_id};"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        return "Request updated", 200

    @classmethod
    def delete_request_with_id(cls, employee_id, request_id):
        request = cls.get_request_with_id(employee_id, request_id)
        if not request:
            return "no request or employee exists", 404
        sql = f"DELETE FROM requests WHERE request_id = {request_id} AND employee_id={employee_id};"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        return "Deleted request"