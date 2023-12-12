"""
9. จากโปรแกรมในข้อ 8 ให้เขียนฟังก์ชัน date_diff เพิ่มเติม โดยให้มีการตรวจสอบ
– วันที่ต้องเป็นวันที่ถูกต้องของเดือนนั้นๆ
– เดือนต้องอยู่ระหว่าง 1-12
– เดือนกุมภาพันธ์ของปีที่มี Leap Year เท่านั้นที่จะมี 29 วันได้
– หากข้อมูล Input ผิดพลาด ให้ Return -1
"""
day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
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

def date_diff(dmy1, dmy2):
    dd1, mm1, yy1 = [int(i) for i in dmy1.split("-")]
    dd2, mm2, yy2 = [int(i) for i in dmy2.split("-")]

    if (day_of_year(dd2, mm2, yy2) != -1 and day_of_year(dd1, mm1, yy1) != -1) \
        or (mm1 >= 1 and mm1 <= 12 and mm2 >= 1 and mm2 <= 12) \
        or (mm1 <= day_in_month[mm1] and mm2 <= day_in_month[mm2]):
        return -1
    
    return day_of_year(dd2, mm2, yy2) - day_of_year(dd1, mm1, yy1) + sum([day_of_year(31, 12, y) for y in range(yy1, yy2)]) + 1

dmy1, dmy2 = input("DD-MM-YY DD-MM-YY: ").split()
print(date_diff(dmy1, dmy2))