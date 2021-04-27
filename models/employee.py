class Employee:

    def __init__(self, employee_id=0, supervisor_id=0, name="", funds=0):
        self.employee_id = employee_id
        self.supervisor_id = supervisor_id
        self.name = name
        self.funds = funds

    def json(self):
        return {
            'employeeId': self.employee_id,
            'supervisorId': self.supervisor_id,
            'name': self.name,
            'funds': self.funds
        }

    @staticmethod
    def json_parse(json):
        employee = Employee()
        employee.employee_id = json["employeeId"] if "employeeId" in json else 0
        employee.supervisor_id = json["supervisor_id"] if "employeeId" in json else 0
        employee.name = json["name"]
        employee.funds = json["funds"]

        return employee

    def __repr__(self):
        return str(self.json())
