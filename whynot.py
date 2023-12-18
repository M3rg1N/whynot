a = int(input("Введи a:"))
b = int(input("Введи b:"))
c = int(input("Введи c:"))

D = b**2-4*a*c

if a == 0:
	x = -c/b
	print("Ответ: x= ", x)
if b == 0:
    d = -c/a
    if d >= 0:
        x1 = d**0.5
        x2 = -x1
        print("Ответ: x1= ", x1, "x2= ", x2)
elif c == 0:
	x1 = 0
	x2 = -b
	print("Ответ: x1= ", x1, "x2= ", x2)
elif D > 0:
	x1 = (-b+D**0.5)/(2*a)
	x2 = (-b-D**0.5)/(2*a)
	print("Ответ: x1= ", x1, "x2= ", x2)
elif D == 0:
	x = -b/(2*a)
	print(x)
elif D < 0:
	print("Корней нет")
