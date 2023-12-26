class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def get_student_name(self):
        return self.student_name
        

class Subject:
    def __init__(self, subject_id, subject_name, section, credit):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.section = section
        self.credit = credit
        self.student_list = []
        self.teacher_list = []
    
    def get_subject_id(self):
        return self.subject_id

    def update_student_list(self, stu):
        self.student_list.append(stu)

    def update_teacher_list(self, teacher):
        self.teacher_list.append(teacher)

    def get_teacher_list(self):
        return self.teacher_list

    def get_student_list(self):
        return self.student_list

class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name
    
    def get_teacher_id(self):
        return self.teacher_id
    
def check_student_by_subject_id(db_subject, teacher_id):
    """ ให้เขียนฟังก์ชัน #1 โดยเมื่อใส่ รหัสผู้สอน แล้วสามารถบอกได้ว่ามี นศ. คนไหนบ้างที่เรียนกับผู้สอนนี้ โดยให้บอกเป็นชื่อนักศึกษา """
    for sub in db_subject:
        if(teacher_id in [t.get_teacher_id() for t in sub.get_teacher_list()]):
            for stu in sub.get_student_list():
                print(stu.get_student_name())

def check_student_registration(db_subject, student_id):
    """ ให้เขียนฟังก์ชัน #2 โดยเมื่อใส่ รหัส นศ. แล้วบอกว่าเรียนวิชาอะไรบ้าง โดยให้บอกเป็นชื่อวิชา """
    for sub in db_subject:
        if(student_id in [s.student_id for s in sub.get_student_list()]):
            print(sub.subject_name)

stu1 = Student(student_id="u01", student_name="NANA")
stu2 = Student(student_id="u02", student_name="YOK")
stu3 = Student(student_id="u03", student_name="EY")
stu4 = Student(student_id="u04", student_name="CHE")
stu5 = Student(student_id="u05", student_name="COPPER")

teacher1 = Teacher(teacher_id="t01", teacher_name="WIT")
teacher2 = Teacher(teacher_id="t02", teacher_name="GAN")

subject1 = Subject(subject_id="s01", subject_name="OOP-SEC1", section=1, credit=3)
subject2 = Subject(subject_id="s02", subject_name="OOP-SEC2", section=2, credit=3)

subject1.update_student_list(stu1)
subject1.update_student_list(stu2)
subject1.update_student_list(stu3)
subject1.update_student_list(stu4)
subject1.update_teacher_list(teacher1)

subject2.update_student_list(stu1)
subject2.update_student_list(stu4)
subject2.update_student_list(stu5)
subject2.update_teacher_list(teacher2)

db_stu = [stu1, stu2, stu3, stu4, stu5]
db_teacher = [teacher1, teacher2]
db_subject = [subject1, subject2]

# check_student_by_subject_id(db_subject=db_subject, teacher_id="t01")
check_student_registration(db_subject, "u02")