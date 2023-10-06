from tkinter import*
from tkinter.ttk import Combobox
import tkinter.messagebox as mbox
import re

root = Tk()
root.title("Dang ky hoc phan")
root.geometry("550x300+500+300")
root.configure(background="light pink")

root.rowconfigure(0, pad=10)

mssv = StringVar()
hoten = StringVar()
email = StringVar()
sdt = StringVar()
hocky = StringVar()
ngaysinh = StringVar()

def CheckMSSV():
    ms = mssv.get()
    if not(len(ms)==7 and ms.isdigit()):
        mbox.showerror("Error", "MSSV chi duoc nhap 7 so")
        mssv.set("")

def CheckEmail():
    em = email.get()
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not(re.match(pattern, em)):
        mbox.showerror("Error", "Email khong hop le")
        email.set("")

def CheckSDT():
    ms = sdt.get()
    if not(len(ms)==10 and ms.isdigit()):
        mbox.showerror("Error", "SDT chi duoc nhap 10 so")
        sdt.set("")

def CheckHocKy():
    hk = hocky.get()
    var = int(hk)
    if var < 1 or var > 3:
        mbox.showerror("Error", "Hoc ki chi duoc nhap 1, 2, 3")
        hocky.set("")

def CheckNgaySinh():
    ns = ngaysinh.get()
    pattern = r'^\d{2}/\d{2}/\d{4}$'
    if not(re.match(pattern, ns)):
        mbox.showerror("Error", "Ngay sinh khong hop le")
        ngaysinh.set("")

def CheckEmty():
    if not mssv.get() or not hoten.get() or not ngaysinh.get() or not email.get() or not sdt.get() or not hocky.get():
        mbox.showwarning("Warning", "Vui long dien du thong tin")
    if not var1.get() or not var2.get() or not var3.get() or not var4.get():
        mbox.showwarning("Warning", "Vui long chon mot mon hoc")

def RegisterForm():
    CheckEmty()
    CheckMSSV()
    CheckEmail()
    CheckNgaySinh()
    CheckSDT()
    CheckHocKy()

Label(root, text="THONG TIN DANG KY HOC PHAN", fg="red", bg="light pink", font=15).grid(row=0, column=1)
Label(root, text="Ma so sinh vien", bg="light pink").grid(row=1, column=0, sticky=W, padx=30)
Label(root, text="Ho ten", bg="light pink").grid(row=2, column=0, sticky=W, padx=30)
Label(root, text="Ngay sinh", bg="light pink").grid(row=3, column=0, sticky=W, padx=30)
Label(root, text="Email", bg="light pink").grid(row=4, column=0, sticky=W, padx=30)
Label(root, text="So dien thoai", bg="light pink").grid(row=5, column=0, sticky=W, padx=30)
Label(root, text="Hoc ky", bg="light pink").grid(row=6, column=0, sticky=W, padx=30)
Label(root, text="Nam hoc", bg="light pink").grid(row=7, column=0, sticky=W, padx=30)
Label(root, text="Chon mon hoc", bg="light pink").grid(row=8, column=0, sticky=W, padx=30)

Entry(root, width=55, textvariable=mssv).grid(row=1, column=1)
Entry(root, width=55, textvariable=hoten).grid(row=2, column=1)
Entry(root, width=55, textvariable=ngaysinh).grid(row=3, column=1)
Entry(root, width=55, textvariable=email).grid(row=4, column=1)
Entry(root, width=55, textvariable=sdt).grid(row=5, column=1)
Entry(root, width=55, textvariable=hocky).grid(row=6, column=1)

cbbNamHoc = Combobox(root, width=52, textvariable=StringVar())
cbbNamHoc["values"] = ("2022-2023", "2023-2024", "2024-2025")
cbbNamHoc.grid(row=7, column=1)
cbbNamHoc.current(0)

var1 = BooleanVar()
var2 = BooleanVar()
var3 = BooleanVar()
var4 = BooleanVar()

chkLTP = Checkbutton(root, text="Lap trinh Python", bg="light pink", variable=var1).grid(row=8, column=1, sticky=W)
chkLTj = Checkbutton(root, text="Lap trinh Java", bg="light pink", variable=var2).grid(row=8, column=1, sticky=E, padx=59)
chkCNPM = Checkbutton(root, text="Cong nghe phan mem", bg="light pink", variable=var3).grid(row=9, column=1, sticky=W, pady=5)
chkPTUDW = Checkbutton(root, text="Phat trien ung dung web", bg="light pink", variable=var4).grid(row=9, column=1, sticky=E)

Button(root, text="Dang ky", bg="light blue", command=RegisterForm).grid(row=10, column=1, sticky=W, padx=60, pady=10)
Button(root, text="Thoat", bg="light blue", command=quit).grid(row=10, column=1, sticky=E, padx=60)

root.mainloop()