database = [] 
polzovatel = None
class Student:
    idcounter = 0
    def __init__(self, firstname, lastname, username, phonenumber, password, address, age, edit=False, delete=False):
        Student.idcounter += 1
        self.id = Student.idcounter
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.phonenumber = phonenumber
        self.password = password
        self.address = address
        self.age = age
        self.edit = edit
        self.delete = delete
    def registration(self):
        global database
        database.append(self)
        print(f"Student {self.username} registered successfully.")
    def login(self, username, password):
        global polzovatel
        for user in database:
            if user.username == username:
                if user.password == password:
                    polzovatel = user
                    print("You are logged in successfully.")
                    return True
                else:
                    print("Incorrect password.")
                    return False
        print(f"User with username {username} not found.")
        return False
    def show(self):
        print(f"Name: {self.firstname} {self.lastname}, Username: {self.username}, Phone: {self.phonenumber}, Age: {self.age}, Address: {self.address}")
    def edit_student(self, new_firstname=None, new_lastname=None, new_phonenumber=None, new_address=None, new_age=None):
        if self.edit:
            if new_firstname:
                self.firstname = new_firstname
            if new_lastname:
                self.lastname = new_lastname
            if new_phonenumber:
                self.phonenumber = new_phonenumber
            if new_address:
                self.address = new_address
            if new_age:
                self.age = new_age
            print(f"Student {self.username} updated successfully.")
        else:
            print(f"Edit permission denied for {self.username}.")
    def delete_student(self):
        global database
        if self.delete:
            database = [user for user in database if user.username != self.username]
            print(f"Student {self.username} deleted successfully.")
        else:
            print(f"Delete permission denied for {self.username}.")
    def logout(self):
        global polzovatel
        polzovatel = None
        print("You have logged out successfully.")
    def __str__(self):
        return f"{self.firstname} {self.lastname}, Username: {self.username}, Phone: {self.phonenumber}, Address: {self.address}, Age: {self.age}"
class Course:
    def __init__(self):
        self.courses = []
    def add_course(self, course_name, course_description):
        course = {'name': course_name, 'description': course_description}
        self.courses.append(course)
        print(f"Course '{course_name}' added successfully.")
    def edit_course(self, course_name, new_name=None, new_description=None):
        for course in self.courses:
            if course['name'] == course_name:
                if new_name:
                    course['name'] = new_name
                if new_description:
                    course['description'] = new_description
                print(f"Course '{course_name}' updated successfully.")
                return
        print(f"Course '{course_name}' not found.")
    def view_course(self, course_name):
        for course in self.courses:
            if course['name'] == course_name:
                print(f"Course: {course['name']}, Description: {course['description']}")
                return
        print(f"Course '{course_name}' not found.")
    def delete_course(self, course_name):
        self.courses = [course for course in self.courses if course['name'] != course_name]
        print(f"Course '{course_name}' deleted successfully.")
course_manager = Course()
while True:
    print("Menu:")
    print("1. Register a new student")
    print("2. Show student information")
    print("3. Edit student information")
    print("4. Delete student")
    print("5. Add a new course")
    print("6. View a course")
    print("7. Edit a course")
    print("8. Delete a course")
    print("9. Exit")
    a = input("Select an option: ")
    if a == "1":
        firstname = input("First name: ")
        lastname = input("Last name: ")
        username = input("Username: ")
        phonenumber = input("Phone number: ")
        password = input("Password: ")
        address = input("Address: ")
        age = input("Age: ")
        edit = input("Allow editing this student? (yes or no): ").lower() == "yes"
        delete = input("Allow deleting this student? (yes or no): ").lower() == "yes"
        student = Student(firstname, lastname, username, phonenumber, password, address, age, edit, delete)
        student.registration()
    elif a == "2":
        for student in database:
            student.show()
    elif a == "3":
        username = input("Enter the username of the student to edit: ")
        for student in database:
            if student.username == username:
                new_firstname = input("New first name (press Enter to skip): ")
                new_lastname = input("New last name (press Enter to skip): ")
                new_phonenumber = input("New phone number (press Enter to skip): ")
                new_address = input("New address (press Enter to skip): ")
                new_age = input("New age (press Enter to skip): ")
                student.edit_student(new_firstname, new_lastname, new_phonenumber, new_address, new_age)
                break
        else:
            print(f"No student found with username {username}.")
    elif a == "4":
        username = input("Enter the username of the student to delete: ")
        for student in database:
            if student.username == username:
                student.delete_student()
                break
        else:
            print(f"No student found with username {username}.")
    elif a == "5":
        course_name = input("Course name: ")
        course_description = input("Course description: ")
        course_manager.add_course(course_name, course_description)
    elif a == "6":
        course_name = input("Enter course name to view: ")
        course_manager.view_course(course_name)
    elif a == "7":
        course_name = input("Enter course name to edit: ")
        new_name = input("New course name (press Enter to skip): ")
        new_description = input("New course description (press Enter to skip): ")
        course_manager.edit_course(course_name, new_name, new_description)
    elif a == "8":
        course_name = input("Enter course name to delete: ")
        course_manager.delete_course(course_name)
    elif a == "9":
        print("The programm has ended!")
        break
    else:
        print("Invalid choice, please try again.")
