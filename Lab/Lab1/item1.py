"""
    จงเขียนโปรแกรมที่จะหาตัวเลขระหว่าง 2000-3200 ที่หารด้วย 7 ลงตัว แต่หารด้วย 5 ไม่ลงตัว
    การแสดงผลให้แสดงตัวเลขและคั่นด้วยเครื่องหมาย , ในบรรทัดเดียว
"""

for i in range(2000, 3200):
    if(i % 7 == 0 and i % 5 != 0):
        print(i, end=",")