import pyodbc
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


connectionString = '''DRIVER={ODBC Driver 17 for SQL Server};
                        SERVER=DESKTOP-VRKH844;DATABASE=QLMonAn;UID=sa;PWD=1;Encrpt=no'''
my_list=[]
def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn

def close_connection(conn):
    if conn:
        conn.close()
def get_all_nhom():
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """select * from NhomMonAn"""
        cursor.execute(select_query)
        records = cursor.fetchall()
        results_for_combobox = [result[1] for result in records]
        return results_for_combobox

        
def get_all_monan():
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """SELECT MonAn.MaMonAn,MonAn.TenMonAn,DonViTinh,DonGia, NhomMonAn.TenNhom
                            FROM MonAn, NhomMonAn
                            WHERE MonAn.Nhom=NhomMonAn.MaNhom
                            ORDER BY MonAn.MaMonAn,MonAn.TenMonAn,DonViTinh,DonGia, NhomMonAn.TenNhom"""
        cursor.execute(select_query)
        records = cursor.fetchall()
        return records

        
def get_monan_byIDnhom(nhom_id):
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """SELECT MonAn.MaMonAn,MonAn.TenMonAn,DonViTinh,DonGia, NhomMonAn.TenNhom
                            FROM MonAn, NhomMonAn
                            WHERE MonAn.Nhom=NhomMonAn.MaNhom and NhomMonAn.MaNhom= ?
                            ORDER BY NhomMonAn.TenNhom;"""
        cursor.execute(select_query, (nhom_id,))
        records = cursor.fetchall()
        return records

def get_Nhom_byID(nhom_id):
    connection = get_connection()
    cursor =connection.cursor()
    
    select_query = """select TenNhom
                        from NhomMonAn
                        where MaNhom = ?"""
    cursor.execute(select_query,(nhom_id))
    record = cursor.fetchall()
    return record

def on_combobox_select(event):
    selected_index = listmonan.current()
    data = get_monan_byIDnhom(selected_index+1) 
    treeView(data)
   
def treeView( data ):
    tree.delete(*tree.get_children()) 
    for row in data:
        row = tuple(row)
        tree.insert("", "end", values=row)

def on_get_index_clicked():
    # Get the selected index
    selected_iid = tree.focus()   
    item_value = tree.item(selected_iid, "values")[0]
    delete_mon_an(item_value) 

def delete_mon_an(ma_mon_an):
    connection = pyodbc.connect(connectionString)
    cursor = connection.cursor()

    delete_query = "DELETE FROM MonAn WHERE MaMonAn = ?"

    try:
        cursor.execute(delete_query, (ma_mon_an,))
        connection.commit()
        messagebox.showinfo("Thông báo", "Món ăn đã xóa thành công")
    except Exception as e:
        messagebox.showinfo(f"Error occurred: {e}")
        connection.rollback()
    finally:
        close_connection(connection)

def add_food(ma,ten,dvt,dongia,nhom):
    connection = pyodbc.connect(connectionString)
    cursor = connection.cursor()
   
    try:
        cursor.execute("{CALL ThemMonAn (?, ?, ?, ?, ?)}",(ma,ten,dvt,dongia,nhom))
        connection.commit()
        messagebox.showinfo("Thông báo", "Món ăn đã thêm thành công")
        print("them")
    except Exception as e:
        messagebox.showinfo(f"Lỗi","Error occurred:")
        connection.rollback()
    finally:
        close_connection(connection)

def table2():
    root1 =Tk()
    root1.configure(background="light grey")
    root1.title("Thêm xóa sửa món ăn")
    root1.geometry("500x300")
    ma = Label(root1, text="Mã món ăn", background="light grey",fg="black",font=('calibre',10, ))
    ma.grid(row =0,pady=5,)
    entry_ma = Entry(root1,  fg="black",background="white",)
    entry_ma.grid(row =0,column=2,padx=60,pady=5,ipadx= 20, ipady=4)
    ten = Label(root1, text="Tên món ăn", fg="black",background="light grey",font=('calibre',10, ))
    ten.grid(row =1,pady=5)
    entry_ten = Entry(root1,  fg="black",background="white",)
    entry_ten.grid(row =1,column=2,padx=60,pady=5,ipadx= 20, ipady=4)
    dvt = Label(root1, text="Đơn vị tính", fg="black",background="light grey",font=('calibre',10, ))
    dvt.grid(row =2,pady=5)
    entry_dvt = Entry(root1,  fg="black",background="white",)
    entry_dvt.grid(row =2,column=2,padx=60,pady=5,ipadx= 20, ipady=4)
    dongia = Label(root1, text="Đơn giá", fg="black",background="light grey",font=('calibre',10, ))
    dongia.grid(row =3,column=0,pady=5,padx=0)
    entry_dongia = Entry(root1,  fg="black",background="white",)
    entry_dongia.grid(row =3,column=2,padx=60,pady=5,ipadx= 20, ipady=4)
    nhom = Label(root1, text="Nhóm", fg="black",background="light grey",font=('calibre',10, ))
    nhom.grid(row =4,column=0,pady=5,padx=0)
    entry_nhom = Entry(root1,  fg="black",background="white",)
    entry_nhom.grid(row =4,column=2,padx=60,pady=5,ipadx= 20, ipady=4)
    
    getma=entry_ma.get()
    getten=entry_ten.get()
    getdvt= entry_dvt.get()
    getdongia =entry_dvt.get()
    getnhom =entry_nhom.get()
    btnThem = Button(root1, text="Enter", command=lambda: add_food(getma, getten, getdvt, getdongia, getnhom))
    btnThem.grid(row=5)
    
if __name__ == "__main__":
    root =Tk()
    root.configure(background="light grey")
    root.title("Quản lý món ăn")
    root.geometry("700x500")

    tree = ttk.Treeview(root)
    tree['columns']=( 'ma','name', 'dvt','dongia', 'nhom')
    tree.column('#0', width=0, stretch=NO)
    tree.column('ma',anchor=CENTER, width=100)
    tree.column('name', anchor=CENTER, width=100)
    tree.column('dvt', anchor=CENTER, width=100)
    tree.column('dongia', anchor=CENTER, width=80)
    tree.column('nhom', anchor=CENTER, width=100)
    
    tree.heading('ma', text='Mã món ăn', anchor=CENTER)
    tree.heading('name', text='Tên món ăn', anchor=CENTER)
    tree.heading('dvt', text='Đơn vị tính', anchor=CENTER)
    tree.heading('dongia', text='Đơn giá', anchor=CENTER)
    tree.heading('nhom', text='Nhóm', anchor=CENTER)
    tree.grid(row=3, columnspan=5, padx= 40, pady=20)
    data = get_all_monan()
    treeView(data)
    
    nhom = Label(root, text="Nhóm món ăn", fg="black",background="light grey",font=('calibre',10, 'bold'))
    nhom.grid(row =0,padx= 40, pady=20)
    selected_nam = StringVar()  
    listmonan = ttk.Combobox(root, values=get_all_nhom())
    listmonan.grid(row=0,column=1, padx= 2, pady=0)
    listmonan.bind("<<ComboboxSelected>>", on_combobox_select)
    
    them = Button(root, text ="Thêm", fg="black",background="white",font=('calibre',10, 'bold'), command=table2)
    them.grid(row = 4, columnspan=1,ipadx= 10, ipady=10)
    xoa = Button (root, text="Xóa",fg="black",background="white", font=('calibre',10, 'bold'),command=on_get_index_clicked)
    xoa.grid(row=4,columnspan=2,ipadx= 16, ipady=10)

    root.mainloop()  