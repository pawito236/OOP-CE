"""
6. กําหนดให้ list x และ y เป็น list ของจํานวนเต็ม โดยมีขนาดเท่ากัน
ให้ return list ที่เป็นผลบวกของ list x และ y โดยใช้ list comprehension
ให้เขียนในฟังก์ชัน function ชื่อ add2list(lst1,lst2)
"""

def add2list(lst1, lst2):
    return [int(n1)+int(n2) for n1, n2 in zip(lst1, lst2)]

lst1 = [1, 2, 3]
lst2 = [1, 1, 2]

print(add2list(lst1, lst2))