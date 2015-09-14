from django.contrib import admin
from .models import *

class UsersAdmin(admin.ModelAdmin):
    list_display=('email','referral_code','referrer','created_at','repeat_ip','ip_address','referrals')

class IPAdmin(admin.ModelAdmin):
	list_display=('address','count','created_at')

admin.site.register(User, UsersAdmin)
admin.site.register(IP_Address, IPAdmin)
admin.site.register(Referrer)