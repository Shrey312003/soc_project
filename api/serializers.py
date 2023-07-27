from rest_framework.serializers import ModelSerializer
from .models import Admin_info, Ta_info, Student_info, Courses, Announcements, Announcement_follow, Course_post, Assignments, post_Comments

class Admin_infoSerializer(ModelSerializer):
    class Meta:
        model =  Admin_info
        fields = '__all__'

class Ta_infoSerializer(ModelSerializer):
    class Meta:
        model =  Ta_info
        fields = '__all__'

class Student_infoSerializer(ModelSerializer):
    class Meta:
        model =  Student_info
        fields = '__all__'

class CoursesSerializer(ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class AnnouncementsSerializer(ModelSerializer):
    class Meta:
        model = Announcements
        fields = '__all__'


class Announcement_followSerializer(ModelSerializer):
    class Meta:
        model = Announcement_follow
        fields = '__all__'



class AssignmentsSerializer(ModelSerializer):
    class Meta:
        model = Assignments
        fields = '__all__'

class Course_postSerializer(ModelSerializer):
    class Meta:
        model = Course_post
        fields = '__all__'


class post_CommentsSerializer(ModelSerializer):
    class Meta:
        model = post_Comments
        fields = '__all__'

