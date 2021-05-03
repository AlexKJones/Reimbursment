class Employee:

    def __init__(self, employee_id=0, dep_id=0, supervisor_id=0, name="", is_dep_head=False, is_benco=False, requests=None):
        self.employee_id = employee_id
        self.dep_id = dep_id
        self.supervisor_id = supervisor_id
        self.name = name
        self.is_dep_head = is_dep_head
        self.is_benco = is_benco
        self.requests = requests

    def json(self):
        return {
            'employeeId': self.employee_id,
            'dep_id': self.dep_id,
            'supervisorId': self.supervisor_id,
            'name': self.name,
            'is_dep_head': self.is_dep_head,
            'is_benco': self.is_benco,
            'requests': self.requests
        }

    @staticmethod
    def json_parse(json):
        employee = Employee()
        employee.employee_id = json["employeeId"] if "employeeId" in json else 0
        employee.dep_id = json["dep_Id"] if "depId" in json else 0
        employee.supervisor_id = json["supervisorId"] if "supervisorId" in json else 0
        employee.name = json["name"]
        employee.is_dep_head = json["is_dep_head"]
        employee.is_benco = json["is_benco"]
        employee.requests = json["requests"]

        return employee

    def __repr__(self):
        return str(self.json())
