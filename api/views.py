from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Admin_infoSerializer,Ta_infoSerializer
from .models import Admin_info,Ta_info,Student_info
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

@api_view(['GET'])
def Ta_data(request,roll):
    ta = Ta_info.objects.filter(Roll=roll)
    print(roll)
    if ta.exists():
        ta_serializer = Ta_infoSerializer(ta.first(), many=False)
        return Response(ta_serializer.data)
    else:
        return Response( 'Ta_info object not found.')