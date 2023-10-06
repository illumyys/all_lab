def Tong(a:float,b:float):
    return a+b
a = float(input("a = "))
b = float(input("b = "))
print(a,"+",b," = ",Tong(a,b))

def Tich(a:float,b:float):
    return a/b
a=float(input("a = "))
b=float(input("b = "))
print(a,'/',b,'=',Tich(a,b))

def LuyThua(a:float,b:float):
    return pow(a,b)
a=float(input("a = "))
b=float(input("b = "))
print(a,'^',b,'=',LuyThua(a,b))
