import pyodbc

connectionString = '''DRIVER={ODBC Driver 17 for SQL Server};
                        SERVER=DESKTOP-VRKH844;DATABASE=QLSinhVien;UID=sa;PWD=1;Encrpt=no'''

def get_connection():
    conn = pyodbc.connect(connectionString)
    return conn

def close_connection(conn):
    if conn:
        conn.close()

def get_all_class():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """select * from Lop"""
        cursor.execute(select_query)
        records = cursor.fetchall()

        print(f"Danh sách các lớp là: ")
        for row in records:
            print("*"*50)
            print("Mã lớp: ", row[0])
            print("Tên lớp: ", row[1])

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi hự thi. Thông tin lỗi: ",error)
get_all_class()

def get_all_student():
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = """select * from SinhVien"""
        cursor.execute(select_query)
        records = cursor.fetchall()

        print(f"Danh sách tất cả các sinh viên là: ")
        print(f'ID \t Họ tên \t\t Mã lớp')
        for row in records:
            print (f'{row[0]} \t {row[1]} \t\t {row[2]}')

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi hự thi. Thông tin lỗi: ",error)
get_all_student()   
             
def get_all_class_student():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from Lop"""
        select_query = """select SinhVien.ID, HoTen, MaLop, Lop.TenLop
                            from SinhVien, Lop
                            where SinhVien.MaLop = Lop.ID"""                      
        cursor.execute(select_query)
        records = cursor.fetchall()

        print(f"Danh sách tất cả các sinh viên là: ")
        print(f'ID \t Họ tên \t\t Mã lớp: \t Tên lớp: ')
        for row in records:
            print (f'{row[0]} \t {row[1]} \t\t {row[2]}\t\t {row[3]}')

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi hự thi. Thông tin lỗi: ",error)
# get_all_class()

def get_class_by_id(class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()


        select_query = "select * from Lop where ID= ?"

        params = (class_id,)
        cursor.execute(select_query, params)

        record = cursor.fetchone()

        print(f"Thông tin lớp có id = {class_id} là: ")
        print("Mã lớp: ", record[0])
        print("Tên lớp: ", record[1])

        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xả ra khi hực thi. Thông tin lỗi: ", error)
# get_class_by_id(1)

def get_student_by_id(sinhvien_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()


        select_query = "select * from SinhVien where ID= ?"

        params = (sinhvien_id,)
        cursor.execute(select_query, params)

        record = cursor.fetchone()

        print(f"Thông tin sinhvien có id = {sinhvien_id} là: ")
        print("Mã số: ", record[0])
        print("Họ tên: ", record[1])
        print("Mã lớp: ", record[2])
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xả ra khi hực thi. Thông tin lỗi: ", error)
# get_student_by_id(1)

def get_student_by_idLop(tenLop):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = '''SELECT * FROM SinhVien JOIN Lop ON SinhVien.MaLop = Lop.ID WHERE Lop.TenLop = ?'''
        params = (tenLop,)
        cursor.execute(select_query, params)

        records = cursor.fetchall()
        print(f"Danh sách tất cả các sinh viên là: ")
        print(f'ID \t Họ tên \t\t Mã lớp: \t Tên lớp: ')
        
        for row in records:
            print (f'{row.ID} \t {row.HoTen} \t\t {row.MaLop}\t\t {row.TenLop}')
            
        close_connection(connection)
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xả ra khi thực thi. Thông tin lỗi: ", error)
# get_student_by_idLop('CTK43')


def search_students_by_name_and_class(tenSinhVien, maLop):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        select_query = "SELECT SinhVien.* FROM SinhVien JOIN Lop ON SinhVien.MaLop = Lop.ID WHERE SinhVien.HoTen LIKE ? AND Lop.ID = ?"
        params = (f'%{tenSinhVien}%', maLop)
        cursor.execute(select_query, params)

        records = cursor.fetchall()
        print(f"Kết quả tìm kiếm sinh viên có tên '{tenSinhVien}' học lớp có mã '{maLop}':")
        print(f'ID \t Họ tên \t\t Mã lớp')
        
        for row in records:
            print (f'{row.ID} \t {row.HoTen} \t\t {row.MaLop}')
            
    except Exception as error:
        print(f"Đã có lỗi xả ra khi thực thi. Thông tin lỗi: {error}")
    finally:
        connection.close()
# search_students_by_name_and_class('Trung', '3')


def insert_class(class_name):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        #Cách 1 - truyền trực tiếp tham số vào câu truy vấn
        #select_query = f"Insert into Lop(TenLop) values ('{class_name}')"
        #cursor.execute(select_query)
        
        #Cách 2 - Dùng tham số
        select_query = "Insert into Lop values ( 10, ?)"
        cursor.execute(select_query, (class_name,))

        connection.commit()

        print("Đã thêm thành công")

        close_connection(connection)
    
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)
# insert_class(class_name)


def delete_class_by_id(class_id):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        delete_query = "DELETE FROM Lop WHERE ID = ?"
        cursor.execute(delete_query, (class_id,))

        connection.commit()

        print(f"Lớp có ID {class_id} đã được xóa thành công")

        close_connection(connection)
    
    except (Exception, pyodbc.Error) as error:
        print("Đã có lỗi xảy ra khi thực thi. Thông tin lỗi: ", error)
# delete_class_by_id(9)