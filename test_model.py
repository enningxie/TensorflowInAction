class VGGModel(BaseModel):
    def __init__(self, config):
        # in python3 just use super().__init__(config) instead
        super(VGGModel, self).__init__(config)
        # call the build_model and init_saver function
        self.build_model()
        self.init_saver()

class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print('Total Employee %d' % Employee.empCount)

    def displayEmployee(self):
        print('Name: ', self.name, ', Salary: ', self.salary)