
class Student:
    def __init__(self, name, crr_cls, id):
        self.name = name
        self.crr_cls = crr_cls
        self.id = id

    def __repr__(self) -> str:
        return f'Student --> Name: {self.name}, Class:{self.crr_cls}, ID: {self.id}'


class Teacher:
    def __init__(self, name, subj, id):
        self.name = name
        self.subj = subj
        self.id = id

    def __repr__(self) -> str:
        return f'Teacher --> Name: {self.name}, Class:{self.subj}, ID: {self.id}'


class School:
    def __init__(self, name, ) -> None:
        self.name = name
        self.teachers = []
        self.students = []

    def add_teacher(self, name, subj):
        id = len(self.teachers) + 100
        teacher = Teacher(name, subj, id)
        self.teachers.append(teacher)

    def enroll(self, name, fee):
        if fee < 6500:
            return 'Not enough fee'
        else:
            id = len(self.students) + 1
            student = Student(name, 'C', id)
            self.students.append(student)
            return f'{name} is enroll with ID: {id}, em: {fee- 6500}'

    def __repr__(self) -> str:
        print('Welcome to', self.name)
        print('--------OUR TEACHERS--------')
        for teachers in self.teachers:
            print(teachers)
        print('--------OUR STUDENTS--------')
        for students in self.students:
            print(students)

        return 'Thanks For Visiting'

abu = Student('Abu Hasan', 13, 1)
abuT = Teacher('Hasan Master', 'Math', 1)

print(abu)
print(abuT)


dhsc = School('Dharmokam High School')
dhsc.enroll('Nazmul Hossen', 7200)
dhsc.enroll('Hossen', 8000)
dhsc.enroll('Nurul Islam', 9000)

dhsc.add_teacher('Mehedi Master', 'Bangla 2')
dhsc.add_teacher('Johurul Master', 'Bangla')
dhsc.add_teacher('Sagor Master', 'English')

print(dhsc)
