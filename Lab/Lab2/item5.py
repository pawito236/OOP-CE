"""
5. ให้เขียนโปรแกรมเพื่อรับ string 1 ตัว
ให้ส่งคืนเฉพาะตัวอักษรที่เป็นภาษาอังกฤษ โดยใช้ List comprehension
ให้เขียนในฟังก์ชัน only_english(string1) แล้ว return เป็นคําตอบเป็น string
"""

def only_english(string1):
    return "".join([s for s in string1 if (s >= 'a' and s<= 'z') or (s>= 'A' and s <= 'Z')])

print(only_english(input("String input : ")))
