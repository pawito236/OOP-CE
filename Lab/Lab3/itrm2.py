"""
2. ให้นําโปรแกรมตามข้อ 1 มาขยายความสามารถให้รองรับนักศึกษาหลายคน โดยให้ refactor ฟังก์ชัน
add_score ให้รับพารามิเตอร์เป็น add_score(subject_score, student, subject, score) โดย student
เป็นข้อมูลของนักศึกษาเป็น string (ในที่นี้เป็น id) และ return เป็น dictionary
    Input : subject_score = { }, student = '65010001', subject = 'python', score = 50
    return : { '65010001' : { 'python' : 50 } }
    input : subject_score = { '65010001' : { 'python' : 50 } },
    student = '65010001', subject = ‘calculus’, score = 60
    return : {'65010001': {'python’: 50, 'calculus', 60} }
โดยหากชื่อมีข้อมูล key ใดที่มีใน dictionary อยู่แล้ว ให้ถือเป็นการ update ข้อมูลนั้น

ให้ refactor ฟังก์ชัน calc_average_score โดยให้ส่งคืนเป็น dictionary ของนักศึกษาและคะแนนเฉลี่ย
ของนักศึกษาคนนั้น เช่น {'65010001': '55.00' }
"""

def add_score(subject_score, student, subject, score):
    if(student in subject_score.keys()):
        subject_score[student].update({subject : score})
    else:
        subject_score.update({student : {subject : score}})
    return calc_average_score(subject_score)

def calc_average_score(subject_score:dict):
    return {id: "{}".format(sum([v for k,v in subject_score[id].items()])/ len(subject_score[id])) for id in subject_score.keys() }

print(add_score(subject_score = { '65010001' : { 'python' : 50 } }, student = '65010001', subject = 'calculus', score = 60))