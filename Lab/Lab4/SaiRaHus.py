class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_mentor = None

    def get_student_name(self):
        return self.student_name

stu1 = Student(student_id="66010473", student_name="Pawit")
stu2 = Student(student_id="65010888", student_name="YOK")
stu3 = Student(student_id="64010023", student_name="NANA")
stu4 = Student(student_id="64010403", student_name="MN")

stu5 = Student(student_id="65010000", student_name="Non")

stu1.student_mentor = stu2
stu2.student_mentor = stu3
stu3.student_mentor = stu4

db_stu = [stu1, stu2, stu3, stu4, stu5]

def check_mentor(student_id):
    """ให้เขียนฟังก์ชัน #3 โดยเมื่อป้อนรหัสนักศึกษา x แล้วตอบว่ามีพี่รหัส เป็นใครบ้าง โดยให้
ตอบให้ครบ เช่น ถ้าป้อน a ให้ตอบ b, c, d ถ้าป้อน b ให้ตอบ c, d โดยให้แสดงทั้งรหัส
นักศึกษาและชื่อ ในการแสดงให้แสดงกรณีไม่มีพี่รหัสด้วย """
    for stu in db_stu:
        if(stu.student_id == student_id):
            if(stu.student_mentor == None):
                return ""
            elif(stu.student_mentor.student_id != ""):
                return stu.student_mentor.student_name + " " + check_mentor(stu.student_mentor.student_id)

def check_mentor_id(student_id):
    """ให้เขียนฟังก์ชัน #3 โดยเมื่อป้อนรหัสนักศึกษา x แล้วตอบว่ามีพี่รหัส เป็นใครบ้าง โดยให้
ตอบให้ครบ เช่น ถ้าป้อน a ให้ตอบ b, c, d ถ้าป้อน b ให้ตอบ c, d โดยให้แสดงทั้งรหัส
นักศึกษาและชื่อ ในการแสดงให้แสดงกรณีไม่มีพี่รหัสด้วย """
    for stu in db_stu:
        if(stu.student_id == student_id):
            if(stu.student_mentor == None):
                return ""
            elif(stu.student_mentor.student_id != ""):
                return stu.student_mentor.student_id + " " + check_mentor_id(stu.student_mentor.student_id)

    return ""

def check_bond_mentor(student_id1, student_id2):
    """ให้เขียนฟังก์ชัน #4 โดยเมื่อป้อนรหัสนักศึกษา Student x และ student y ให้ตรวจสอบว่าเป็น
สายรหัสกันหรือไม่ ให้ตอบเป็น True และ False"""
    if(int(student_id1) < int(student_id2)):
        temp = student_id1
        student_id1 = student_id2
        student_id2 = temp

    bond = check_mentor_id(student_id1) if check_mentor_id(student_id1) != None else ""
    print(bond)
    if(student_id2 in bond): return True
    else: return False

# print("No mentor" if check_mentor("66010473").strip() == "" else check_mentor("66010473"))
print(check_bond_mentor("64010403", "66010473"))
