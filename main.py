def plus():#สหัสชัย สิทธิมงคล
            a = float(input(": "))
            b = float(input(": "))
            ผลลัพธ์ = a + b
            print(ผลลัพธ์)

def minus():#สิทธิโชค ลิ้มไล้
            a = float(input(": "))
            b = float(input(": "))
            ผลลัพธ์ = a - b
            print(ผลลัพธ์)
def multi():#ปณิธาน ปัญญารัตนโยธิน
            a = float(input(": "))
            b = float(input(": "))
            ผลลัพธ์ = a * b
            print(ผลลัพธ์)
def divi():#ปณิธาน ปัญญารัตนโยธิน
            a = float(input(": "))
            b = float(input(": "))
            ผลลัพธ์ = 
            print(ผลลัพธ์)
while True:
    print("บวก กด 1")
    print("ลบ กด 2")
    print("คูณ กด 3")
    print("หาร กด 4")

    choose=int(input("กรอกวิธีคำนวณ"))
    if (choose==1):
        plus()
    elif(choose==2):
        minus()
    elif(choose==3):
        multi()
    elif(choose==4):
        
    else:
        print("error")