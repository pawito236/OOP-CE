"""
5. ตัวเลข palindrome คือตัวเลขที่อ่านได้ทั้ง 2 ทาง แล้วมีค่าเท่ากัน เช่น 9009 โดย 9009 คือ palindrome
ที่เกิดจากการคูณของตัวเลข 2 หลักที่มากที่สุด คือ 91x99 จงหา palindrome ที่มากที่สุดของตัวเลข 3
หลัก

"""
max = 0
palindrome = ""
# for i in range(999*999, 0, -1):
#     if(str(i) == str(i)[::-1]):
#         palindrome = i

for i in range(999, 1, -1):
    for j in range(999, 1, -1):
        sum = i*j
        if(str(sum) == str(sum)[::-1]):
            if(i*j > max):
                palindrome = f"{i}x{j}"
                max = i*j
            # break
    # if(palindrome != ""): 
    #     print(palindrome)
    #     break
print(max)