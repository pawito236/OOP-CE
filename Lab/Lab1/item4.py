"""
4. จงเขียนโปรแกรมที่คํานวณค่าของ a+aa+aaa+aaaa เมื่อรับข้อมูลเป็นตัวเลข 1 หลัก

Input : 9
Output : 11106 (=9+99+999+9999)

"""

n = str(input())
print(sum([int(n*i) for i in range(1,5)]))