from django.db import models
from ATM_LH.Long.models import ChiNhanh, CayATM, NganHang
# Create your models here.


class TinhThanh(models.Model):
    ma_tinh_thanh = models.CharField(primary_key=True, max_length=2)
    ten_tinh_thanh = models.TextField()


class KhanhHang(models.Model):
    GIOI_TINH = (
        ('M', 'Man'),
        ('W', 'Woman'),
    )
    LOAI_GIAY_TO = (
        ('CMND', 'Chung minh nhan dan'),
        ('TCC', 'The can cuoc'),
        ('HC', 'Ho chieu'),
    )
    ma_chi_nhanh = models.ForeignKey(ChiNhanh, on_delete=models.CASCADE)
    ma_khach_hang = models.CharField(max_length=3, primary_key=True)
    ho_ten_kh = models.CharField(max_length=32)
    ngay_sinh = models.DateField()
    gioi_tinh = models.CharField(max_length=1, choices=GIOI_TINH)
    que_quan = models.TextField()
    so_dien_thoai = models.CharField(max_length=12, unique=True)
    email = models.TextField(unique=True)
    loai_giay_to = models.CharField(max_length=4, choices=LOAI_GIAY_TO)
    so_giay_to = models.CharField(max_length=12, unique=True)


class TaiKhoan(models.Model):
    TRANG_THAI = (
        ('Act', 'Active'),
        ('Dor', 'Dormant'),
        ('Inact', 'Inactive'),
    )
    ma_khach_hang = models.ForeignKey(KhanhHang, on_delete=models.CASCADE)
    so_tai_khoan = models.CharField(max_length=13, primary_key=True)
    ma_pin = models.TextField()
    han_muc = models.BigIntegerField()
    so_du = models.BigIntegerField()
    ngay_tao = models.DateField()
    trang_thai = models.CharField(max_length=5, choices=TRANG_THAI)


class The(models.Model):
    LOAI_THE = (
        ('1', 'The tin dung'),
        ('2', 'The tin dung'),
        ('3', 'The ATM'),
        ('4', 'The ghi no'),
        ('5', 'The dam bao'),
        ('6', 'The Visa'),
    )
    TRANG_THAI = (
        ('1', 'Mo'),
        ('2', 'Dong'),
    )
    so_tai_khoan = models.ForeignKey(TaiKhoan, on_delete=models.CASCADE)
    so_the = models.CharField(primary_key=True, max_length=13)
    ma_pin = models.TextField()
    ngay_tao = models.DateField()
    ngay_het_han = models.DateField()
    loai_the = models.CharField(max_length=1, choices=LOAI_THE)
    trang_thai = models.CharField(max_length=1, choices=TRANG_THAI)


class GiaoDich(models.Model):
    LOAI_GIAO_DICH = (
        ('RT', 'Rut tien'),
        ('CT', 'Chuyen tien'),
    )
    TRANG_THAI = (
        ('1', 'Thanh cong'),
        ('2', 'That bai'),
    )
    so_the = models.ForeignKey(The, on_delete=models.CASCADE)
    ma_cay = models.ForeignKey(CayATM, on_delete=models.CASCADE)
    ma_ngan_hang = models.ForeignKey(NganHang, on_delete=models.CASCADE)
    ma_giao_dich = models.CharField(max_length=3, primary_key=True)
    loai_giao_dich = models.CharField(max_length=2, choices=LOAI_GIAO_DICH)
    thoi_gian = models.DateTimeField()
    so_tien = models.BigIntegerField()
    phi_giao_dich = models.SmallIntegerField()
    trang_thai = models.CharField(max_length=1, choices=TRANG_THAI)