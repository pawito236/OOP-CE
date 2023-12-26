"""
8. จากโปรแกรมในข้อ 7 ให้เขียนฟังก์ชัน เพิ่มเติมเป็น date_diff
– รับข้อมูลในรูปแบบ “dd-mm-yyyy” เช่น
date_diff(“1-1-2018”, “1-1-2020”) จะได้ 731 วัน
date_diff(“25-12-1999”, “9-3-2000”) จะได้ 76 วัน
– ให้เขียนฟังก์ชัน day_in_year โดยจะส่งค่าจํานวนวันของปี (365 หรือ 366) โดยรับข้อมูลเป็น ปี
– ส่งคืนข้อมูลเป็นจํานวนวันตั้งแต่วันที่แรก จนถึงวันที่สอง โดยรวมทั้ง 2 วันนั้นเข้าไปด้วย
– ให้สมมติว่าวันแรก จะต้องมาก่อนวันที่สองเสมอ ดังนั้นไม่ต้องตรวจสอบ
"""

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def day_of_year(day, month, year):
    day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
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

def day_in_year(year):
    return day_of_year(31, 12, year)

def date_diff(dmy1, dmy2):
    dd1, mm1, yy1 = [int(i) for i in dmy1.split("-")]
    dd2, mm2, yy2 = [int(i) for i in dmy2.split("-")]
    return day_of_year(dd2, mm2, yy2) - day_of_year(dd1, mm1, yy1) + sum([day_in_year(y) for y in range(yy1, yy2)]) + 1

dmy1, dmy2 = input("DD-MM-YY DD-MM-YY: ").split()
print(date_diff(dmy1, dmy2))