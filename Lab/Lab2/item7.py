"""
7. ให้เขียน function ชื่อ day_of_year(day, month ,year)
โดยมีการคืนค่า คือ day_of_years เป็นวันที่ลําดับที่เท่าใดของปีคริสตศักราช year
– ปีที่เป็น Leap Year เดือนกุมภาพันธ์จะมี 29 วัน
– ให้สร้างฟังก์ชัน is_leap เพื่อตรวจสอบ leap year แยกออกมา และให้ฟังก์ชัน day_of_year
    เรียกใช้ is_leap อีกที
"""

day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_of_year(day, month, year):
    day_of_years = 0
    if(is_leap(year)):
        day_in_month[2] += 1
    else:
        if(month == 2 and day == 29):
            return -1
    for i in range(1, month):
        # print(day_in_month[i])
        day_of_years += day_in_month[i]
    day_of_years += day

    return day_of_years

dd, mm, yy = [int(i) for i in input("DD MM YY: ").split()]
print(day_of_year(dd, mm, yy))