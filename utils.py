import random

user_list = [
    {
        "ID": "6JPX34-D05NzT-yr7w3h-2EJ6aE",
        "Type": "Teacher",
        "Name": "Johan",
        "Username": "johsta",
        "Password": "password",
        "StudentList": ["fRWL81-AqYyzm-A1B6vq-w2WM8n"]
    },
    {
        "ID": "fRWL81-AqYyzm-A1B6vq-w2WM8n",
        "Type": "Student",
        "Name": "Daniel",
        "Attendances": {}
    }
]

def save_data(data):
    return

def load_data():
    data = []
    return data

def pack_data(teachers, students, managers, superTeachers):
    data = []
    return data

def unpack_data(data):
    teachers = []
    students = []
    managers = []
    superTeachers = []
    for user in data:
        user_type = user["Type"]
        del user["Type"]
        if user_type == "Teacher":
            teachers.append(user)
        elif user_type == "Student":
            students.append(user)
        elif user_type == "Manager":
            managers.append(user)
        elif user_type == "Super Teacher":
            superTeachers.append(user)
        
    return [teachers, students, managers, superTeachers]

print(unpack_data(user_list))

class User:
    def __init__(self, Name, id = "") -> None:
        self.Name = Name
        self._id = id
        if self._id == "":
            self._id = self._generateID()

    def _generateID(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        id = "-".join(''.join(random.choice('0123456789'*2 + letters + letters.lower()) for _ in range(6)) for _ in range(4))
        return id

class Teacher(User):
    def __init__(self, Name, username, password, id = "", studentList = []) -> None:
        self.username = username
        self._password = password
        self.studentList = studentList
        super().__init__(Name, id=id)
    
    def changePassword(self, oldPassword, confPassword, newPassword):
        if oldPassword == confPassword == self._password:
            self._password = newPassword
        else:
            return "Incorrect Password"

    def createStudent(self):
        pass

class SuperTeacher(Teacher):
    def __init__(self, Name, username, password, id = "", studentList = []) -> None:
        super().__init__(Name, username, password, id = id, studentList = studentList)


class Student(User):
    def __init__(self, Name, userID, id = "", attendance = {}) -> None:
        self.userID = userID
        self.attendance = attendance
        super().__init__(Name, id=id)

class Manager(Student):
    def __init__(self, Name, userID, id = "") -> None:
        super().__init__(Name, userID, id=id, attendance= {})