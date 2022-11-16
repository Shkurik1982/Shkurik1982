import random
a='new'

while True:
    txt=''
    try: 
        if int(a)>=1 and int(a)<=10:
            #b=random.randint(1,10)
            if int(a)==b:
                txt='Вы выиграли.\nНачинаем новый раунд\n'
                b=random.randint(1,10)
            elif  int(a) > b:
                txt="Много.\n"
            else:
                txt="Мало.\n"
    except:
        if a=="exit":
            break
        if a=="new":
            b=random.randint(1,10)
            txt="Начинаем новый раунд\n"
    a=input(txt+'Введите число от 1 до 10\nexit для выхода, или new для нового раунда\n')
