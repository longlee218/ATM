from django.db import models
from ATM_LH.Hoang.models import TinhThanh
# Create your models here.


class NganHang(models.Model):
    ma_ngan_hang = models.CharField(primary_key=True, max_length=8)
    ten_ngan_hang = models.TextField()
    tru_so = models.TextField()
    tong_dai = models.CharField(max_length=10)
    chi_nhanh = models.ManyToManyField(TinhThanh, through="ChiNhanh")


class ChiNhanh(models.Model):
    ma_tinh_thanh = models.ForeignKey(TinhThanh, on_delete=models.CASCADE)
    ma_ngan_hang = models.ForeignKey(NganHang, on_delete=models.CASCADE)
    ma_chi_nhanh = models.CharField(max_length=5, primary_key=True)
    ten_chi_nhanh = models.TextField()
    dia_chi = models.TextField()


class NhanVien(models.Model):
    ma_chi_nhanh = models.ForeignKey(ChiNhanh, on_delete=models.CASCADE)
    ma_nhan_vien = models.CharField(max_length=3, primary_key=True)
    ho_ten_nv = models.CharField(max_length=32)
    ten_dang_nhap = models.CharField(max_length=18)
    mat_khau = models.TextField()


class CayATM(models.Model):
    TRANG_THAI = (
        ('1', 'Hoat dong'),
        ('2', 'Bao tri'),
        ('3', 'Hong'),
    )
    ma_nhan_vien = models.OneToOneField(NhanVien, on_delete=models.CASCADE)
    ma_cay = models.CharField(max_length=5, primary_key=True)
    dia_diem = models.TextField()
    so_du = models.BigIntegerField()
    trang_thai = models.CharField(max_length=1, choices=TRANG_THAI)


class LichSuDoTien(models.Model):
    ma_do_tien = models.CharField(max_length=3, primary_key=True)
    ma_cay = models.ForeignKey(CayATM, on_delete=models.CASCADE)
    thoi_gian = models.DateTimeField()
    so_tien_do = models.BigIntegerField()