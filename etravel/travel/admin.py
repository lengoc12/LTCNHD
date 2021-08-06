from django.contrib import admin
from django.contrib.auth.models import Permission
from django.db.models import Count
from django.urls import path
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.template.response import TemplateResponse
from django.utils.html import mark_safe
from .models import *
# Register your models here.


class TourForm(forms.ModelForm):
    class Meta:
        model = Tour
        fields = '__all__'

    content = forms.CharField(widget=CKEditorUploadingWidget)


class TourInline(admin.StackedInline):
    model = Tour
    fk_name = 'destination'


class DestinationAdmin(admin.ModelAdmin):
    inlines = (TourInline,)


class TourCategoryInlineAdmin(admin.TabularInline):
    model = Tour.category.through


class CategoryAdmin(admin.ModelAdmin):
    inlines = [TourCategoryInlineAdmin, ]


class TourAdmin(admin.ModelAdmin):
    form = TourForm
    inlines = [TourCategoryInlineAdmin, ]
    list_display = ['id', 'name', 'NgayKhoiHanh', 'SoNgay', 'Gia', 'departure', 'destination']
    search_fields = ['name', 'NgayKhoiHanh', 'SoNgay', 'Gia', 'departure', 'destination']
    list_filter = ['NgayKhoiHanh', 'SoNgay', 'Gia']
    readonly_fields = ['avatar']

    def avatar(self, tour):
        return mark_safe('<img src="/static/{img_url}" alt="{alt}" width="200px" />'.format(img_url=tour.image.name, alt=tour.name))


class TourAppAdminSite(admin.AdminSite):
    def get_urls(self):
        return [
            path('tour_stats/', self.tour_stats)
        ] + super().get_urls()

    def tour_stats(self, request):
        tour_count = Tour.objects.count()
        category_count = LoaiHinhDuLich.objects.count()
        destination = NoiDen.objects.count()
        stats = NoiDen.objects.annotate(so_luong=Count('tours')).values('id', 'name', 'so_luong')

        return TemplateResponse(request, 'admin/tour-stats.html', {
            'tour_count': tour_count,
            'category_count': category_count,
            'destination': destination,
            'stats': stats,

        })

    site_header = 'HỆ THỐNG QUẢN LÝ TOUR DU LỊCH'


#admin_site = TourAppAdminSite('mytour')


#admin_site.register(NoiDen, DestinationAdmin)
#admin_site.register(NoiKhoiHanh)
#admin_site.register(KhachSan)
#admin_site.register(Employee)
#admin_site.register(KhachHang)
#admin_site.register(Tour, TourAdmin)
#admin_site.register(PhuongTien)
#admin_site.register(HopDong)
#admin_site.register(HoaDon)
#admin_site.register(LoaiHinhDuLich, CategoryAdmin)

admin.site.register(NoiDen, DestinationAdmin)
admin.site.register(NoiKhoiHanh)
admin.site.register(KhachSan)
admin.site.register(Employee)
admin.site.register(KhachHang)
admin.site.register(Tour, TourAdmin)
admin.site.register(PhuongTien)
admin.site.register(HopDong)
admin.site.register(HoaDon)
admin.site.register(LoaiHinhDuLich, CategoryAdmin)
admin.site.register(User)
admin.site.register(Permission)
