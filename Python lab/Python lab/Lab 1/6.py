def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Nhập số Fibonacci đầu tiên cần tính tổng: "))
sum = 0
for i in range(0, n):
    sum += fibonacci(i)
print("Tổng của", n, "số Fibonacci đầu tiên là:", sum)
