from exceptions.resource_not_found import ResourceNotFound
from models.employee import Employee
from util.db_connection import connection
from daos.employee_doa import EmployeeDAO
from logger import log


class EmployeeDAOImpl(EmployeeDAO):

    def create_employee(self, employee):
        # empID, depID, SupervisorID, 'NAME',  isDepHead, isBenCo, requests
        sql = "INSERT INTO employees VALUES (DEFAULT, 1, %s, %s, DEFAULT, DEFAULT, DEFAULT) RETURNING *"
        # EX: DEFAULT, 1, 2, 'Jotaro Joestar', 0, false, false, DEFAULT
        cursor = connection.cursor()
        cursor.execute(sql, (employee.supervisor_id, employee.name))
        log(f"Creating an employee")
        connection.commit()
        record = cursor.fetchone()

        new_employee = Employee(record[0], record[1], record[2], record[3], record[4], record[5], record[6])
        return new_employee

    def get_employee(self, employee_id):
        sql = "SELECT * FROM employees WHERE employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        log(f"Viewing an employee")
        record = cursor.fetchone()

        if record:
            return Employee(record[0], record[1], record[2], record[3], record[4], record[5], record[6])
        else:
            return record
            # raise ResourceNotFound(f"Employee with employee_id: {employee_id} - Not Found")

    def all_employees(self):
        sql = "SELECT * FROM employees"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        log(f"Viewing employees")
        employee_list = []

        for record in records:
            employee = Employee(record[0], record[1], record[2], record[3], record[4], record[5], record[6])

            employee_list.append(employee.json())

        return employee_list

    def update_employee(self, change):
        sql = "UPDATE employees SET name=%s WHERE employee_id=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (change.name, change.employee_id))
        connection.commit()
        log(f"Updating an employee")
        record = cursor.fetchone()
        new_employee = Employee(record[0], record[1], record[2], record[3], record[4], record[5], record[6])
        return new_employee

    def delete_employee(self, employee_id):
        sql = "DELETE FROM employees WHERE employee_id = %s"
        log(f"Deleting an employee")
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        connection.commit()
        return 'deleted'


def _test():
    m_dao = EmployeeDAOImpl()
    employees = m_dao.all_employees()
    print(employees)

    print(m_dao.get_employee(1))


if __name__ == '__main__':
    _test()
