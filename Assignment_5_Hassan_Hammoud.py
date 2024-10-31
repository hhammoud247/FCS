import json

class Course:
    def __init__(self,code,name,credit_hours, core=True):
        self.code = code
        self.name = name
        self.credit_hours = credit_hours
        self.core = core

    def printout(self):
        return f"{self.code}: {self.name} - {self.credit_hours} credits - {'Core' if self.core else 'Elective'}"

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = {}

    def enrollCourse(self,course):
        if course.code in self.courses:
            print(f"{self.name} is enrolled already")
            return
        self.courses[course.code] = course

    def dropCourse(self, course_code):
        if course_code not in self.courses:
            print(f"{course_code} not found in {self.name} courses")
            return
        else:
            del self.courses[course_code]
            print(f"{course_code} dropped for {self.name}")

    def courseList(self):
        if not self.courses:
            return "No courses enrolled!"
        return '\n'.join(str(cs) for cs in self.courses.values())

class EnrollmentSystem:
    def __init__(self):
        self.courses = {}
        self.students = {}
#Add Course: Add a new course to the catalog.
    def addCourse(self, code,name, credit_hours, core = True):
        if code in self.courses:
            print(f"Course with code {code} already exist ")
            return
        self.courses[code] = Course(code, name, credit_hours,core)
#Enroll Student in Course: Enroll a student in a specified course.

    def studentEnroll(self,student_id, course_code):
        if student_id not in self.courses:
            print(f"Student with ID {student_id} not found")
            return
        if course_code not in self.courses:
            print(f"Course with code {course_code} not found")
            return
        self.students[student_id].enrollCourse(self.courses[course_code])

    def droppinG(self,student_id,course_code):
        if student_id not in self.students:
            print(f"Student with ID {student_id} not found")
            return
        self.students[student_id].dropCourse(course_code)

    def listStudentcourses(self,student_id):
        if student_id not in self.students:
            print(f"Student with ID {student_id} not found.")
            return ""
        return self.students[student_id].courseList()

    def SaveCourse(self,filename):
        # with open(filename,'w') as files:
        #     files.write('{\n}')
        #     for i, (key, value) in enumerate(self.courses.items()):
        #         key_str = f'"{key}"'
        #         value_str = f'"{value}"' if isinstance(value, str) else str(value)
        #         comma = ','if i < len(self.courses) -1 else ''
        #         files.write(f' {key_str}: {value_str}{comma}\n')
        #     files.write('}\n')
        try:
            with open(filename, "w") as file:
                catalog_data = {code: vars(course) for code, course in self.courses.items()}
                json.dump(catalog_data, file)
                print(f"Course catalog saved to {filename}")
        except IOError as e:
            print(f"Error saving catalog: {e}")

    def loadCourse(self, filename):
        try:
            with open(filename, 'r') as files:
                courses_data = json.load(files)
                for course_data in courses_data.values():
                    self.addCourse(
                        course_data['code'],
                        course_data['name'],
                        course_data['credit_hours'],
                        course_data['core']
                    )
                print(f"Courses loaded from {filename}")
        except (IOError, KeyError) as e:
            print(f"Error loading catalog: {e}")

    def addStudent(self,student_id, name):
        if student_id in self.students:
            print(f"Student with ID {student_id} already exists")
            return
        self.students[student_id] = Student(student_id, name)
        print(f"Student {name} added with ID {student_id}")


def main():
    sys = EnrollmentSystem()
    while True:
        print("\nUniversity Course Enrollment System")
        print("1. Add Course")
        print("2. Enroll Student in Course")
        print("3. Drop Course for Student")
        print("4. List Student Courses")
        print("5. Save Course Catalog")
        print("6. Load Course Catalog")
        print("7. Add Student")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            code = input("Enter course code: ")
            name = input("Enter course name: ")
            credit_hours = int(input("Enter credit hours: "))
            core = input("Is this course a core course?(Yes/No): ").strip().lower() == 'yes'
            try:
                sys.addCourse(code, name,credit_hours,core)
                print("Course added successfully.")
            except Exception as e:
                print(e)

        elif choice == '2':
            student_id = input("Enter student ID: ")
            course_code = input("Enter course code to enroll in: ")
            try:
                sys.studentEnroll(student_id, course_code)
                print("student enrolled successfully")
            except Exception as e :
                print(e)
        elif choice == '3':
            student_id = input("Enter student ID: ")
            course_code = input("Enter course code to drop: ")
            try:
                sys.droppinG(student_id,course_code)
                print("Course dropped successfully")
            except Exception as e:
                print(e)
        elif choice == '4':
                student_id = input("Enter student ID: ")
                try:
                    courses = sys.listStudentcourses(student_id)
                    print("Enrolled courses:\n",courses)
                except Exception as e:
                    print(e)
        elif choice  == '5':
            filename = input("Enter filename to save courses' list: ")
            sys.SaveCourse(filename)
            print("Course list saved successfully")

        elif choice == '6':
            filename = input("Enter filename to load course list: ")
            try:
                sys.loadCourse(filename)
                print("course list loaded successfully")
            except Exception as e:
                print(e)

        elif choice  == '7':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            try:
                sys.addStudent(student_id, name)
                print("student added successfully")
            except Exception as e:
                print(e)

        elif choice == '8':
            print("Exiting the program")
            break
        else:
            print("Invalid choice. Please try again.")
main()

