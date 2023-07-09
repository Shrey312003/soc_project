from django.contrib import admin
from .models import Admin_info,Ta_info,Student_info,Courses,Attendance_Records,Attendance_sessions
# Register your models here.

admin.site.register(Admin_info)
admin.site.register(Ta_info)
admin.site.register(Student_info)
admin.site.register(Courses)
admin.site.register(Attendance_sessions)
admin.site.register(Attendance_Records)