from abc import abstractmethod, ABC


class RequestService(ABC):

    @abstractmethod
    def create_request(self, employee_id, amount):
        pass

    @abstractmethod
    def get_all_requests_for_employee(self, employee_id):
        pass

    @abstractmethod
    def get_request_with_id(self, employee_id, request_id):
        pass

    @abstractmethod
    def update_request_with_id(self, employee_id, request_id, req_funds, added_info, is_denied, denied_reason,
                               is_approved):
        pass

    @abstractmethod
    def delete_request_with_id(self, employee_id, request_id):
        pass
