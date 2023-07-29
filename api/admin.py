from django.contrib import admin
from .models import Admin_info, Ta_info, Student_info, Courses, Attendance_Records, Attendance_sessions, Announcements, Announcement_follow, Assignments, Course_post, post_Comments
# Register your models here.


admin.site.register(Admin_info)
admin.site.register(Ta_info)
admin.site.register(Student_info)
admin.site.register(Courses)
admin.site.register(Attendance_sessions)
admin.site.register(Attendance_Records)
admin.site.register(Announcements)
admin.site.register(Announcement_follow)
admin.site.register(Course_post)
admin.site.register(post_Comments)
admin.site.register(Assignments)
