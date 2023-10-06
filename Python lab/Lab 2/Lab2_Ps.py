class PhanSo:
    def __init__(self, tu: int = 0, mau: int = 1) -> None:
        if mau == 0:
            raise ArithmeticError('Phan so khong the co mau bang 0')
        self.tu = tu
        self.mau = mau
        self.rutGon()

    def tinhGiaTriCuaPhanSo(self) -> float:
        return self.tu / self.mau

    def ktPhanSoAm(self):
        return self.tu * self.mau < 0

    @staticmethod
    def my_gcd_1(num1: int, num2: int):
        ucln = 1
        if num1 < num2:
            num = num1
        else:
            num = num2
        for i in range(2, num + 1):
            if num1 % i == 0 and num2 % i == 0:
                ucln = i
        return ucln

    @staticmethod
    def my_gcd_2(num1: int, num2: int):
        while num1 != num2:
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
        return num1

    @staticmethod
    def my_gcd3(num1: int, num2: int):
        while num2:
            num1, num2 = num2, num1 % num2
        return num1

    def my_gcd_4(self, num1: int, num2: int):
        if num2 == 0:
            return num1
        else:
            return self.my_gcd_4(num2, num1 % num2)

    def my_gcd_5(self, num1: int, num2: int):
        if num1 == 0 or num2 == 0:
            return num1 + num2

        if num1 == num2:
            return num1

        if num1 > num2:
            return self.my_gcd_5(num1 - num2, num2)

        else:
            return self.my_gcd_5(num1, num2 - num1)

    def rutGon(self):
        gcd = self.my_gcd_4(self.tu, self.mau)
        if gcd != 1:
            self.tu = self.tu // gcd
            self.mau = self.mau // gcd

    def __add__(self, other):
        result = PhanSo(self.tu * other.mau + self.mau * other.tu, self.mau *
                        other.mau)
        result.rutGon()
        return result

    def bcnn(self, a, b):
        return int(a * b) / self.my_gcd_4(a, b)

    # def __lt__(self, other):
    #     if not isinstance(other, PhanSo):
    #         other = PhanSo(other, 1)
    #     mau_chung = self.bcnn(self.mau, other.mau)
    #     print(f"UCLN cua {self.mau} va {other.mau} la: {mau_chung}")
    #     if other.mau == mau_chung:
    #         return self.tu * mau_chung < other.tu
    #     elif self.mau == mau_chung:
    #         return self.tu < other.tu * mau_chung
    #     return self.tu * mau_chung < other.tu * mau_chung

    # def __gt__(self, other):
    #     if not isinstance(other, PhanSo):
    #         other = PhanSo(other, 1)
    #     mau_chung = self.bcnn(self.mau, other.mau)
    #     print(f"UCLN cua {self.mau} va {other.mau} la: {mau_chung}")
    #     if other.mau == mau_chung:
    #         return self.tu * mau_chung > other.tu
    #     elif self.mau == mau_chung:
    #         return self.tu > other.tu * mau_chung
    #     return self.tu * mau_chung > other.tu * mau_chung

    def __sub__(self, other):
        result = PhanSo(self.tu * other.mau - self.mau * other.tu,
                        self.mau * other.mau)
        result.rutGon()
        return result

    def __mul__(self, other):
        result = PhanSo(self.tu * other.tu, self.mau * other.mau)
        result.rutGon()
        return result

    def __truediv__(self, other):
        result = PhanSo(self.tu * other.mau, self.mau * other.tu)
        result.rutGon()
        return result

    def __str__(self):
        if self.mau == 1:
            return f'{self.tu}'
        return f'{self.tu}/{self.mau}'

