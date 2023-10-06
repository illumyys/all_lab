import math

def giaiPTBac2(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                return "Phương trình vô số nghiệm"
            else:
                return "Phương trình vô nghiệm"
        else:
            x = -c / b
            return "Phương trình có một nghiệm: x = {}".format(x)
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            return "Phương trình vô nghiệm"
        elif delta == 0:
            x = -b / (2*a)
            return "Phương trình có nghiệm kép: x1 = x2 = {}".format(x)
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            return "Phương trình có hai nghiệm phân biệt: x1 = {}, x2 = {}".format(x1, x2)

a = float(input("Nhập hệ số bậc 2, a = "))
b = float(input("Nhập hệ số bậc 1, b = "))
c = float(input("Nhập hằng số tự do, c = "))

print(giaiPTBac2(a, b, c))