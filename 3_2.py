a = [0,0]
cod = ''
print ('Движение персонажа, начальная позиция (0,0) по оси x и y. Для выхода введите "exit"')
while cod != 'exit':
    cod = str(input('Куда идем? (up,down,left,right):'))
    if cod == 'exit':
        continue
    i = int(input('Сколько шагов? (целые значения):'))
    if cod == 'up':    
        a[1] += i
    elif cod == 'down':
       a[1] -= i
    elif cod == 'left':
        a[0] -= i
    elif cod == 'right':
        a[0] += i
    elif cod == 'exit':
        print('Пришли')
    else:
        print('Команда введена неверно')
    print('Координаты персонажа x =',a[0],'y =',a[1])
print('Координаты персонажа x =',a[0],'y =',a[1])