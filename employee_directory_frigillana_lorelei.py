# Review Programming Assignment
# Program Description: Employee Directory
# Your Name: Lorelei Frigillana
# Date: 10/01/2025

# Employee Class
class Employee:
    """ Employee class to keep track of employee info """
    def __init__(self, ID=-999, name='', department='', pay=0.0):
        """ initializer for new employee object """
        self.set_ID(ID)
        self.set_name(name)
        self.set_department(department)
        self.set_pay(pay)

    # Getters and setters
    def get_ID(self):
        return self.ID
    def set_ID(self, ID):
        self.ID = ID
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_department(self):
        return self.department
    def set_department(self, department):
        self.department = department
    def get_pay(self):
        return self.pay
    def set_pay(self, pay):
        self.pay = pay

    def __str__(self):
        return f'{self.get_ID()}\t{self.get_name()}\t{self.get_department()}\t{self.get_pay()}'

# Employee Directory Class
class EmployeeDirectory:
    """ Track employee info in the directory """
    def __init__(self):
        self.employee_list = []
        self.employee_dict = {}

    def add_employee(self, employee):
        """ Append employee object to the employee_list """
        self.employee_list.append(employee)

    def del_employee(self, employee):
        """ Delete employee object from the employee_list """
        try:
            self.employee_list.remove(employee)
        except ValueError:
            print(f"ID:{employee.get_ID()} does not exist, deletion is aborted")

    def read_file(self, file_name):
        """ Read employees.txt file and return a list of employee objects """
        employees = []
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 4:
                        ID = int(parts[0])
                        name = parts[1]
                        department = parts[2]
                        pay = float(parts[3])
                        emp = Employee(ID, name, department, pay)
                        employees.append(emp)
        except FileNotFoundError:
            print(f"File {file_name} not found.")
        return employees

    def update_employee_dir(self, file_name):
        """ Update the employee_list attribute with file data """
        self.employee_list = self.read_file(file_name)

    def write_to_file(self, file_name):
        """ Write the updated employee_list to file """
        with open(file_name, 'w') as file:
            for emp in self.employee_list:
                file.write(f"{emp.get_ID()},{emp.get_name()},{emp.get_department()},{emp.get_pay()}\n")

    def write_to_dict(self):
        """ Write employee_list data to a dictionary of lists """
        dummy_emp = Employee()
        for attribute_name in dummy_emp.__dict__.keys():
            self.employee_dict[attribute_name] = []

        for emp in self.employee_list:
            for attribute_name, attribute_value in emp.__dict__.items():
                self.employee_dict[attribute_name].append(attribute_value)

    def display_dict(self):
        """ Display employee dictionary in key/value pairs """
        for key, value in self.employee_dict.items():
            print(f"{key} : {value}")
        print()  


if __name__ == '__main__':
    try:
        directory = EmployeeDirectory()

        directory.update_employee_dir('employees.txt')

        emp1 = Employee(106, 'Emp1', 'Accounting', 56000.0)
        emp2 = Employee(107, 'Emp2', 'Sales', 80000.0)
        emp3 = Employee(108, 'Emp3', 'IT', 90000.0)

        directory.add_employee(emp1)
        directory.add_employee(emp2)
        directory.del_employee(emp3)

    except KeyError as ke:
        print(ke)
    except Exception as ex:
        print(ex)
    finally:
        directory.write_to_file('employees.txt')
        directory.write_to_dict()
        directory.display_dict()
