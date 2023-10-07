import datetime
from encodings import utf_8
import math

class SinhVien:
    truong = "Đại học Đà Lạt"

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.__maSo = maSo
        self.__hoTen = hoTen
        self.__ngaySinh = ngaySinh

    @property
    def maSo(self):
        return self.__maSo
    
    @property
    def hoTen(self):
        return self.__hoTen
    
    @property
    def ngaySinh(self):
        return self.ngaySinh
    
    @maSo.setter
    def maSo(self, maSo):
        if self.laMaSoHopLe(maSo):
            self.__maSo = maSo

    @staticmethod
    def laMaSoHopLe(maSo: int):
        return len(str(maSo)) == 7

    @classmethod
    def doiTenTruong(self, tenMoi):
        self.truong = tenMoi

    def __str__(self) -> str:
        return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
    
    def xuat(self):
        print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")

 #---------------------------------------------------------------------------------------------------
 
class DanhSachSV:
    def __init__(self) -> None:
        self.dssv = []
    
    def themSinhVien(self, sv: SinhVien):
        self.dssv.append(sv)

    def xuat(self):
        for sv in self.dssv:
            print(sv)

    def timSvTheoMssv(self, mssv: int):
        for sv in self.dssv:
            if sv.maSo == mssv:
                return sv
    
    def timVTSvTheoMssv(self, mssv: int):
        for i in range(len(self.dssv)):
            if self.dssv[i].mssv == mssv:
                return i
        return -1
    
    def xoaSvTheoMssv(self, maSo: int) -> bool:
        vt = self.timVTSvTheoMssv(maSo)
        if vt != -1:
            del self.dssv[vt]
            return True
        else:
            return False
    
    def timSvTheoTen(self, ten:str):
        for sv in self.dssv:
            l = sv.hoTen.split()
            n = len(l)
            if l[n - 1] == ten:
                return sv

    def timSvSinhTruocNgay(self, ngay: datetime):
        ds = []
        for sv in self.dssv:
            if sv.ngaySinh < ngay:
                ds.append(sv)
        return ds
    def sapXepDSTang_HoTen(self):
        ds = sorted(self.dssv, key=lambda item: item.hoTen)
        return ds
ds = DanhSachSV()
sv = SinhVien(0, "Zero", "0/0/0000")
ds.themSinhVien(SinhVien(1, "Thục Nguyên", "8/4/2004"))
ds.themSinhVien(SinhVien(2, "Thuyên", "4/4/2004"))
ds.xuat()
print(sv)

print(ds.timSvTheoTen("Nguyên"))
dskq = DanhSachSV()

f = open("D:\Works\Python lab\Lab 2\Lab2.txt", encoding= "utf8")
for x in f:
    l = x.split(",")
    ds.themSinhVien(SinhVien(l[0], l[1], l[2]))
f.close()
ds.xuat()
ds = ds.sapXepDSTang_HoTen()
