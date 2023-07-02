
from django.urls import path
from . import views

urlpatterns = [
    path("admin-login/",views.Admin_login,name="admin_login" ),
    path("ta-login/",views.Ta_login,name="ta_login"),
    path("student-login/",views.Student_login,name="student_login"),
    path("ta/<str:roll>/",views.Ta_data,name="ta"),
    path("ta/<str:roll>/delete-course/",views.Ta_courseRemove,name="ta_course_delete"),
    path("student/<str:roll>/",views.Student_data,name="student"),
    path("student-signup/",views.Student_signup,name="student_signup")
]