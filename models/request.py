class Request:
    def __init__(self, request_id=0, employee_id=0, employee_name="", request_for="", req_funds=0, req_type="", info="",
                 added_info="", pass_grade=0, event_date=None, submit_date=None, is_denied=False, denied_reason="",
                 is_approved=False):
        self.request_id = request_id
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.request_for = request_for
        self.req_funds = req_funds
        self.req_type = req_type
        self.info = info
        self.added_info = added_info
        self.pass_grade = pass_grade
        self.event_date = event_date
        self.submit_date = submit_date
        self.is_denied = is_denied
        self.denied_reason = denied_reason
        self.is_approved = is_approved

    def get_request_id(self):
        return self.request_id

    def get_employee_id(self):
        return self.employee_id

    def json(self):
        return {
            'requestId': self.request_id,
            'employeeId': self.employee_id,
            'employee_name': self.employee_name,
            'request_for': self.request_for,
            'req_funds': self.req_funds,
            'req_type': self.req_type,
            'info': self.info,
            'added_info': self.added_info,
            'pass_grade': self.pass_grade,
            'event_date': self.event_date,
            'submit_date': self.submit_date,
            'is_denied': self.is_denied,
            'denied_reason': self.denied_reason,
            'is_approved': self.is_approved
        }

    @staticmethod
    def json_parse(json, employee_id):
        request = Request()
        request.employee_id = json["employeeId"]
        request.amount = json["amount"]
        return request
