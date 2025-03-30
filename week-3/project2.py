print("IZIFIN TECHNOLOGY")
x = int(input("enter years of expirience: "))
y = int(input("enter age: "))
if x > 25 and y >= 55:
    print("your annual tax return is N5,600,000")
elif x > 20 and y >= 45:
    print("your annual tax return is N4,480,000")
elif x > 10 and y >= 35:
    print("your annual tax return is N1,500,000")
else:
    print("your annual tax return is N550,000")