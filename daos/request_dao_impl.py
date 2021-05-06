from daos.request_dao import RequestDAO
from models.employee import Employee
from models.request import Request
from util.db_connection import connection
import logging


class RequestDAOImpl(RequestDAO):
    @classmethod
    def create_request(cls, employee_id, employee_name, request_for, req_funds, req_type, info, pass_grade, event_date,
                       submit_date):
        sql = f"insert into requests values ( default, {employee_id}, {employee_name}, {request_for}, {req_funds}," \
              f" {req_type}, {info}, default, {pass_grade}, {event_date}, {submit_date}, default, default, default );"
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
        requests = [Request(elem[0], elem[1], (elem[2])) for elem in records]
        return requests

    @classmethod
    def get_request_with_id(cls, employee_id, request_id):
        sql = f"SELECT * FROM(SELECT * FROM requests  where employee_id = {employee_id}) m WHERE request_id ={request_id};"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        requests = [Request(elem[0], elem[1], (elem[2]), (elem[3]), "", (elem[5]), (elem[6]), (elem[7]), "", (elem[9]), (elem[10])) for elem in records]
        return requests

    @classmethod
    def update_request_with_id(cls, employee_id, request_id, req_funds, added_info, is_denied, denied_reason,
                             is_approved):
        print(f"'req_funds is:' {req_funds}")
        # added_info = "null"
        print(f"'added_info is:' {added_info}")
        print(f"'is_denied is:' {is_denied}")
        sql = f"UPDATE requests SET req_funds ={req_funds}, added_info ={added_info}, is_denied ={is_denied}," \
              f" denied_reason ={denied_reason}, is_approved ={is_approved} WHERE request_id = {request_id}" \
              f" AND employee_id={employee_id};"
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        return "Request updated"

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
