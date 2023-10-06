import math

def ktSoNT(n):
	if (n<2):
		return False
	for i in range(2,int(math.sqrt(n))):
	 if n%i==0:
	   return False
	return True
try:
  a = int(input("Nhap so dau tien trong khoang: "))
  b = int(input("Nhap so cuoi cung trong khoang: "))
  if a<0 or b<0:
    print('Vui long nhap so nguyen duong')
  if a>b:
    print('Vui long nhap a nho hon b')
  else:
    print("Các số nguyên tố trong khoảng từ",a,"đến",b,"là:")
    for i in range(a,b+1):
    		if ktSoNT(i):
    		  print (i)
except:
  print('Vui long nhap dung')