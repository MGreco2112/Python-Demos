class Employee:
    #python constructor, self indicates this class similar to 'this'. Fields come after
    def __init__(self, name, worked, pay):
        self.name = name
        self.hoursWorked = worked
        self.payRate = pay
    
    #custom method, self is used to assign value to field within class
    def setGross(self, gross):
        self.grossPay = gross
