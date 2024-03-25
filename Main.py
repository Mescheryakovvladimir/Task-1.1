import math


def provrka():
    string= input("Введите число: ")
    str = string.replace("-", "",)
    str = str.replace(".",'')
    if str.isdigit():
        number = float(string)
        print(number)
        return number
    else:print("Error")
x=provrka()
y=provrka()
z=provrka()
f=0
f=(2*math.cos(x-math.pi/6))/((1/2)+(math.sin(y))**2)
print(f)
