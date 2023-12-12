"""
3. กําหนดให้ List x เป็น List ของจํานวนเต็ม
ให้เขียนโปรแกรมเพื่อลบจํานวนเต็มทุกตัวใน x ที่มีค่าเป็นลบ โดยใช้ List comprehension
– เช่น x = [ [1, -3, 2], [-8, 5], [-1, -4, -3] ]
– ได้คําตอบเป็น [ [1, 2], [5], [] ]

ให้สร้างเป็น delete_minus(x) แล้ว return เป็น List คําตอบ

"""
def delete_minus(x):
    non_minus_list = []
    for item in x:
        non_minus_list.append([i for i in item if i >= 0])
    return non_minus_list

x = [ [1, -3, 2], [-8, 5], [-1, -4, -3] ]

print(delete_minus(x))