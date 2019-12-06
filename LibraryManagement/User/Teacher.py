
class Person:

    def __init__(self,name,address,phoneNo,email,gender):
        self.__name = name
        self.__address =address
        self.__phoneNo = phoneNo
        self.__email = email
        self.__gender = gender

    def getName(self):
        return self.__name

    def getGender(self):
        return self.__gender

    def getPhoneNo(self):
        return self.__phoneNo

    def getEmail(self):
        return self.__email

    def getAddress(self):
        return self.__address

    def setName(self,name):
        self.__name = name

    def setGender(self,gender):
        self.__gender = gender

    def setPhoneNo(self,phoneNo):
        self.__phoneNo = phoneNo

    def setEmail(self,email):
        self.__email = email

    def setAddress(self,address):
        self.__address = address

    def display(self):
        print("Name",self.__name)
        print("Address",self.__address)
        print("Email",self.__gender)
        print("PhoneNumber",self.__phoneNo)
        print("Gender",self.__gender)



class Teacher(Person):

    def __init__(self,name,address,email,gender,phoneNo,employeeId,department,salary,role):
        super().__init__(name,address,phoneNo,email,gender)
        self.__employeeId = employeeId
        self.__department = department
        self.__researchAreas = []
        self.__salary = salary
        self.__role = role
        self.__subjects =  []

    def subscriptionFees(self,fees):
        self.__salary-= fees

    def updateResearchAreas(self,research):
        self.__researchAreas.append(research)
        return self.__researchAreas

    def getResearchAreas(self):
        return self.__researchAreas

    def getDepartment(self):
        return self.__department

    def updateDepartment(self,department):
        self.__department = department

    def getEmployeeId(self):
        return self.__employeeId

    def getRole(self):
        return self.__role

    def updateRole(self,role):
        self.__role = role

    def getSubjects(self):
        return self.__subjects

    def addSubjects(self,subject):
        self.__subjects.append(subject)

    def display(self):
        super().display()
        print("subjects thought",self.getSubjects())
        print("Role of the prof",self.getRole())
        print("Department of the Prof",self.getDepartment())
        print("employee Id of the Prof",self.getEmployeeId())
        print("Get Research Areas",self.getResearchAreas())



