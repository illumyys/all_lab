import math

def tong_can_bac_hai(n):
    tong = 0
    for i in range(1, n+1):
        tong += math.sqrt(i)
    return tong

n = int(input("Nhập số nguyên dương n: "))
print("Tổng căn bậc hai của", n, "số nguyên đầu tiên là:",tong_can_bac_hai(n))