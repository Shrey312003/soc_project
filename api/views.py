from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Admin_infoSerializer,Ta_infoSerializer,Student_infoSerializer
from .models import Admin_info,Ta_info,Student_info,Courses
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.

@api_view(['GET','POST'])
def Admin_login(request):
    if(request.method =='POST'):
        admins = Admin_info.objects.all()


@csrf_exempt
@api_view(['GET','POST'])

def Ta_login(request):
 
    ta_data = JSONParser().parse(request)

    roll = ta_data['Roll']
    password = ta_data['Password']
    

    ta = Ta_info.objects.filter(Roll = roll, Password = password)
    
    if ta.exists():
        for instance in ta:
            instance.is_logged = True
            instance.save()
        return Response("nice")
    
    return Response("user doesnt exist");

@csrf_exempt
@api_view(['GET','POST'])

def Student_login(request):
 
    student_data = JSONParser().parse(request)

    roll = student_data['Roll']
    password = student_data['Password']
    

    student = Student_info.objects.filter(Roll = roll, Password = password)
    
    if student.exists():
        for instance in student:
            instance.is_logged = True
            instance.save()
        return Response("nice")
    
    return Response("user doesnt exist");



@api_view(['GET','POST'])
@csrf_exempt
def Ta_data(request,roll):
    if request.method =="GET":
        ta = Ta_info.objects.filter(Roll=roll)
        if ta.exists():
            ta_serializer = Ta_infoSerializer(ta.first(), many=False)
            return Response(ta_serializer.data)
        else:
            return Response( 'Ta_info object not found.')
        
    if request.method =="POST":
        ta = Ta_info.objects.filter(Roll = roll)

        if ta.exists():
            course_data = JSONParser().parse(request)

            course_id = course_data['courseId']
            course_code = course_data['courseCode']

            course = Courses.objects.filter(courseId =course_id, courseCode = course_code)

            if(course.exists()):
                ta.first().course.add(*course) 
                ta.first().save()
                ta_serializer = Ta_infoSerializer(ta.first(), many=False)
                return Response(ta_serializer.data)
            return Response("Course code invalid")
        return Response("Ta doenst exist")
    
@api_view(['POST'])
@csrf_exempt
def Ta_courseRemove(request,roll):
    ta = Ta_info.objects.filter(Roll = roll)

    if ta.exists():
        course_data = JSONParser().parse(request)

        course_id = course_data['courseId']
        
        course = Courses.objects.filter(courseId =course_id)

        if(course.exists()):
            ta.first().course.remove(course.first()) 
            ta.first().save()
            ta_serializer = Ta_infoSerializer(ta.first(), many=False)
            return Response(ta_serializer.data)
        return Response("Course code invalid")
    return Response("Ta doenst exist")

@api_view(['GET'])
@csrf_exempt
def Student_data(request,roll):
    if request.method =="GET":
        student = Student_info.objects.filter(Roll=roll)
        if student.exists():
            student_serializer = Student_infoSerializer(student.first(), many=False)
            return Response(student_serializer.data)
        else:
            return Response( 'Student_info object not found.')

@api_view(['POST'])
@csrf_exempt
def Student_signup(request):
    if request.method == "POST":
        student_data = JSONParser().parse(request)

        student_name = student_data["name"]
        student_roll = student_data["roll"]
        student_pass = student_data["password"]

        student = Student_info.objects.create(
            Name=student_name,
            Roll=student_roll,
            Password=student_pass
        )

        student.save()

        return Response("Student added success")
    return Response("wrong method")
