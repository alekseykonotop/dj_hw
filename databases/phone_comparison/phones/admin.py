from django.contrib import admin
from .models import Phone, IPhone, Samsung, Xiaomi


class PhoneAdmin(admin.ModelAdmin):
    pass


class IPhoneAdmin(admin.ModelAdmin):
    pass


class SamsungAdmin(admin.ModelAdmin):
    pass


class XiaomiAdmin(admin.ModelAdmin):
    pass


admin.site.register(Phone, PhoneAdmin)
admin.site.register(IPhone, IPhoneAdmin)
admin.site.register(Samsung, SamsungAdmin)
admin.site.register(Xiaomi, XiaomiAdmin)