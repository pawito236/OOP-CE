"""
4. เขียนฟังก์ชัน char_count(str) โดยรับพารามิเตอร์ 1 ตัว เป็นข้อมูลชนิด string และให้ส่งคืนเป็น
dictionary ที่มี key เป็นตัวอักษรแต่ละตัวของ string นั้น และ value คือ จํานวนครั้งที่ตัวอักษรนั้นปรากฏ
ใน string เช่น
Input : 'language'
return : {'l': 1, 'a': 2, 'n': 1, 'g': 2, 'e': 1}
"""

def char_count(sentnce:str):
    return {c:sentnce.count(c) for c in set(sentnce)}


print((char_count("language")))