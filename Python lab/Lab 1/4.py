def kiem_tra_so_fibonacci(n):
    a = 0
    b = 1
    while b < n:
        c = a + b
        a = b
        b = c
    if b == n:
        return True
    else:
        return False
try:
  n = int(input("Nhập số cần kiểm tra: "))
  if n<0:
    print('Vui lòng nhập số nguyên dương')
  else:
    if kiem_tra_so_fibonacci(n):
        print(n, "là số Fibonacci.")
    else:
        print(n, "không phải là số Fibonacci.")
except:
  print("Vui long nhap dung!!!")