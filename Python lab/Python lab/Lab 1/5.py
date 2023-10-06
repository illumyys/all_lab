def tinh_thu_fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
      return tinh_thu_fibonacci(n-1) + tinh_thu_fibonacci(n-2)
try:
  n = int(input("n = "))
  print("Số Fibonacci thứ ",n," là: ",tinh_thu_fibonacci(n))
except:
  print("Vui lòng nhập đúng!!!")
#########################################################
def tinh_thu_fibonacci_dequy(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
      a = 0
      b = 1
      for i in range(2,n+1):
        c = a + b
        a = b
        b = c
        c += b
      return b
try:
  n = int(input("n = "))
  print("Số Fibonacci thứ ",n," là: ",tinh_thu_fibonacci_dequy(n))
except:
  print("Vui lòng nhập đúng!!!")
