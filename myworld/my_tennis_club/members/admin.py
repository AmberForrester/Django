from django.contrib import admin

# Register your models here:
from .models import Member

# Control the fields to display by specifying them in a list_display property. 
# 1st - create a MemberAdmin() class:
class MemberAdmin(admin.ModelAdmin):
# 2nd - specify the list_display tuple:
    list_display = ('firstname', 'lastname', 'joined_date',)

# Add MemberAdmin as an argument. 
admin.site.register(Member, MemberAdmin)