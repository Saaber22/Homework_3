a = [0,0];
cod = str(input('Куда идем:'));
i = int(input('Сколько шагов? (целые значения)'))
if cod == 'up':
    a[1] += i
elif cod == 'down':
    a[1] -= i
elif cod == 'left':
    a[0] -= i
elif cod == 'right':
    a[0] += i
else:
    print('Команда введена неверно')
print('Координаты персонажа x =',a[0],'y =',a[1])