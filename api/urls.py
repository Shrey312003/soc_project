
from django.urls import path
from . import views

urlpatterns = [
    path("admin-login/",views.Admin_login,name="admin_login" ),
    path("ta-login/",views.Ta_login,name="ta_login"),
    path("student-login/",views.Student_login,name="student_login"),
    path("ta/<str:roll>/",views.Ta_data,name="ta"),
    path("ta/<str:roll>/delete-course/",views.Ta_courseRemove,name="ta_course_delete"),
    path("student/<str:roll>/",views.Student_data,name="student"),
    path("student-signup/",views.Student_signup,name="student_signup"),
    path("attendance/",views.Attendance_Sessions,name="attendance_sessions"),
    path("student-attendance/<str:courseId>/<str:date>/",views.Attendance,name="attendance"),
    path("student-attendance/", views.MakeAttend,name= "make_attend"),
    path("course/<str:id>/", views.Course_home, name="course_home"),
    path("course/<str:id>/discussions/",
         views.Discussion_tab, name="course_discussions"),
    path("course/<str:id>/class/", views.Course_class, name="course_class"),
    path("course/<str:id>/announcements/",
         views.Course_announcements, name="course_announcements"),
    path("announcements/<str:id>/", views.Announcement_followup,
         name="announcement_followup"),
    path("course/<str:id>/create-announcement/",
         views.Create_Announcement, name="create_announcements"),
    path("course/<str:id>/assignments/",
         views.assignment_tab, name="course_assignments"),
]
