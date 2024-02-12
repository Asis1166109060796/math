def plus():
            a = float(input(": "))
            b = float(input(": "))
            ผลลัพธ์ = a + b
            print(ผลลัพธ์)

print("บวก กด 1")
print("ลบ กด 2")
print("คูณ กด 3")

choose=int(input("กรอกวิธีคำนวณ"))
if (choose==1):
        plus()
else:
        print("error")