class Request:
    def __init__(self, request_id=0, employee_id=0, employee_name="", request_for="", req_funds=0, req_type="", info="",
                 added_info="", pass_grade=0, event_date=None, submit_date=None, is_denied=False, denied_reason="",
                 is_approved=False, phase=0):
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
        self.phase = phase

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
            'is_approved': self.is_approved,
            'phase': self.phase
        }

    @staticmethod
    def json_parse(json, employee_id):
        request = Request()
        request.requestId = json["requestId"] if "requestId" in json else 0
        request.employee_id = json["employeeId"] if "employeeId" in json else 0
        request.employee_name = json["employee_name"]
        request.request_for = json["request_for"]
        request.req_funds = json["req_funds"]
        request.req_type = json["req_type"]
        request.info = json["info"]
        request.added_info = json["added_info"]
        request.pass_grade = json["pass_grade"]
        request.event_date = json["event_date"]
        request.submit_date = json["submit_date"]
        request.is_denied = json["is_denied"]
        request.denied_reason = json["denied_reason"]
        request.is_approved = json["is_approved"]
        request.phase = json["phase"]
        return request
