"""

    ให้ตรวจสอบว่า String ที่รับเข้ามาผ่านคีย์บอร์ด เป็นตัวอักษรพิมพ์เล็ก หรือตัวอักษรพิมพ์ใหญ่ อย่างละกี่ตัว
ให้ตอบ 2 บรรทัด จํานวนตัวพิมพ์เล็ก 1 บรรทัด จํานวนตัวพิมพ์ใหญ่ 1 บรรทัด

"""

sentence = str(input())
c_lower = 0
c_upper = 0

for s in sentence:
    if(s.isalpha()):
      if(s.lower() == s):
          c_lower += 1
      else:
          c_upper +=1

print(c_lower)
print(c_upper)