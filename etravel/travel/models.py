from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
# Create your models here.


class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')


class ItemBase(models.Model):
    class Meta:
        abstract = True

    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    CMND = models.CharField(max_length=20, null=False, unique=True)
    male = 1
    female = 2
    none = 3
    choices = ((male, 'Nam'), (female, 'Nữ'), (none, 'Khác'))
    GioiTinh = models.IntegerField(choices=choices, default=none)
    DienThoai = models.CharField(max_length=11)
    NgaySinh = models.DateTimeField()

    def __str__(self):
        return self.first_name +' '+ self.last_name


class KhachHang(ItemBase):
    class Meta:
        ordering = ['-id']
    email = models.CharField(max_length=255)


class NoiKhoiHanh(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)

    def __str__(self):
        return self.name


class NoiDen(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)

    def __str__(self):
        return self.name


class LoaiHinhDuLich(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)

    def __str__(self):
        return self.name


class Tour(models.Model):
    name = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='travel/%Y/%m', default=None)
    NgayKhoiHanh = models.DateTimeField() #ngay bat dau
    SoNgay = models.IntegerField() #so ngay cua tour
    Gia = models.IntegerField() #gia tour
    status = models.BooleanField(default=True)
    content = RichTextField()

    departure = models.ForeignKey(NoiKhoiHanh, related_name="tours", on_delete=models.SET_NULL, null=True) #noi khoi hanh
    category = models.ManyToManyField(LoaiHinhDuLich, related_name='tours', blank=True, null=True)
    destination = models.ForeignKey(NoiDen, related_name='tours', on_delete=models.SET_NULL, null=True) #diem dem

    def __str__(self):
        return self.name


class KhachSan(models.Model):
    name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=11)
    status = models.BooleanField(default=True)

    destination = models.ForeignKey(NoiDen, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class PhuongTien(models.Model):
    name = models.CharField(max_length=255, null=False)
    seats = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Employee(ItemBase):

    status = models.BooleanField(default=True)


class HopDong(models.Model):
    name = models.CharField(max_length=255, null=False)
    GiaTriHopDong = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    SoLuongNguoiLon = models.IntegerField()
    SoLuongEmBe = models.IntegerField()
    PhongRieng = models.BooleanField(default=False)

    customer = models.ForeignKey(KhachHang, related_name='contracts', on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, related_name='contracts', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class HoaDon(models.Model):
    name = models.CharField(max_length=255, null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)  # thoa thuan hop dong
    contract = models.ForeignKey(HopDong, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
