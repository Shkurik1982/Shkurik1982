import random
txt=txt1=''
a=1
b=random.randint(1,10)
print(b)
while True:
    if ( (a>=1 and a<=10) and (str(a)!="exit") and (str(a)!="new")) :
        a=input(txt+'Введите число от 1 до 10 or exit\n'+txt1+"или exit для выхода, или new для нового раунда\n")
        if a=="exit":continue
        print("a=",a)
        print("b=",b)
        if int(a)==b:
            txt='Вы выиграли. '
        elif  int(a) > b:
            txt="Много. "
        else:
            txt="Мало. "
    elif (a=="exit"):
        break
    elif a=="new":
        b=random.randint(1,10)
        print(b)
        a=b+1
    else: continue
