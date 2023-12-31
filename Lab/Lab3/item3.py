"""
3. ให้เขียนฟังก์ชัน is_plusone_dictionary(d) โดยรับพารามิเตอร์ 1 ตัว เป็นข้อมูลชนิด dictionary และให้
ทดสอบว่า dictionary ที่รับเข้ามาเป็น plusone dictionary หรือไม่ ผลลัพธ์ให้return เป็น True หรือ
False โดย plusone dictionary คือ dictionary ที่ key และ value จะบวก 1 ต่อกันไปเรื่อยๆ

    Input : {1:2, 3:4, 5:6, 7:8}
    return : True
    อธิบาย : เพราะ key : value ต่างกันเป็น +1 ต่อกันไป
    Input : {1:2, 3:10, 5:6, 7:8}
    return : False
อธิบาย : เพราะ key, value ไม่เป็นไปตามลําดับ
"""

def is_plusone_dictionary(d:dict):
    last_n = None
    for k, v in d.items():
        if(k != v-1): return False
        if(last_n != None):
            if(last_n != k-1): return False
        last_n = v
    return True

print(is_plusone_dictionary({1:2, 3:10, 5:6, 7:8}))