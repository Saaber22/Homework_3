import math

print("Введите коэффициенты для уравнения")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a == 0 and b == 0 and c == 0:
    print("X любое число")
else:
    if a == 0 and b == 0:
        print("решений нет")
    else:
        if a == 0:
            x = (-c / b)
            print("x=", x)
        else:
            dis = b ** 2 - 4 * a * c
            print("Дискриминант D = ",dis)
            if dis > 0:
                x1 = (-b + math.sqrt(dis)) / (2 * a)
                x2 = (-b - math.sqrt(dis)) / (2 * a)
                if x1 == x2:
                    print('x=',x1)
                else:    
                    print('x1=',x1,'x2=',x2)