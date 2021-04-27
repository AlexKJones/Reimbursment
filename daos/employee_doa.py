from abc import abstractmethod, ABC


class EmployeeDAO(ABC):

    @staticmethod
    def create_employee(self, employee):
        pass

    @staticmethod
    def get_employee(self, employee_id):
        pass

    @staticmethod
    def all_employees(self):
        pass

    @staticmethod
    def update_employee(self, change):
        pass

    @staticmethod
    def delete_employee(self, employee_id):
        pass
