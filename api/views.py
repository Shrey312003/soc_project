from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import Admin_infoSerializer,Ta_infoSerializer,Student_infoSerializer
from .models import Admin_info,Ta_info,Student_info,Courses,Attendance_Records,Attendance_sessions
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.

@api_view(['GET','POST'])
def Admin_login(request):
    if(request.method =='POST'):
        admins = Admin_info.objects.all()


@csrf_exempt
@api_view(['GET', 'POST'])
def Ta_login(request):
    if request.method == 'POST':
        ta_data = JSONParser().parse(request)

        roll = ta_data['Roll']
        password = ta_data['Password']

        ta = Ta_info.objects.filter(Roll=roll, Password=password)

        if ta.exists():
            for instance in ta:
                instance.is_logged = True
                instance.save()
                request.session['roll'] = instance.Roll
                request.session['name'] = instance.Name
                request.session['user'] = 'TA'
            return Response("nice")

        return Response("user doesnt exist")
    return Response('Waiting')


@csrf_exempt
@api_view(['GET', 'POST'])
def Student_login(request):

    student_data = JSONParser().parse(request)

    roll = student_data['Roll']
    password = student_data['Password']

    student = Student_info.objects.filter(Roll=roll, Password=password)

    if student.exists():
        for instance in student:
            instance.is_logged = True
            instance.save()
            request.session['roll'] = instance.Roll
            request.session['name'] = instance.Name
            request.session['user'] = 'student'
        return Response("nice")

    return Response("user doesnt exist")



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

@api_view(['GET','POST'])
def Attendance_Sessions(request):
    if request.method == "POST":
        data = JSONParser().parse(request)

        course = data['courseId']
        date = data["date"]
        start = data["start_time"]

        instance = Attendance_sessions.objects.create(
            CourseId= course,
            Date = date,
            Start = start
        )
        instance.save()

        return Response("Attendance session created")
       

@api_view(['GET','POST'])
def Attendance (request,courseId,date):
    if request.method == "GET":
        attendance = Attendance_sessions.objects.filter(CourseId = courseId, Date = date)

        if(attendance.exists()):
            response_data = {
                'id' : attendance.first().id,
                'start': attendance.first().Start
            }
            return Response(response_data)
        else:
            return Response("date is incorrect")
        
@api_view(['GET','POST'])
def MakeAttend(request):
    if request.method == "POST":
        data = JSONParser().parse(request)

        roll = data["roll"]
        courseId = data["courseId"]
        sessionId = data["sessionId"]
        time = data["time"]

        session = Attendance_sessions.objects.filter(id = sessionId)

        if(session.exists()):
            instance = Attendance_Records.objects.create(
                Session = session.first(),
                CourseId = courseId,
                Roll = roll,
                Attend_time = time
            )

            instance.save()

            return Response("Attendance recorded")
        return Response("Session doesnt exist")
    return Response("invalid type")

@api_view(['GET'])
@csrf_exempt
def Course_home(request, id):
    if request.method == 'GET':
        course = Courses.objects.filter(courseId=id)
        if course.exists():
            course_serializer = CoursesSerializer(course.first(), many=False)
            return Response(course_serializer.data)
        else:
            return Response('Course not found')


@api_view(['GET'])
@csrf_exempt
def Course_class(request, id):
    if request.method == 'GET':
        course = Courses.objects.filter(courseId=id)
        if course.exists():
            students = Student_info.objects.filter(course=course[0])
            tas = Ta_info.objects.filter(course=course[0])
            if students.exists() and tas.exists():
                students_serializer = Student_infoSerializer(
                    students, many=True)
                tas_serializer = Ta_infoSerializer(tas, many=True)
                return Response({"students": students_serializer.data, "tas": tas_serializer.data})
            elif students.exists():
                students_serializer = Student_infoSerializer(
                    students, many=True)
                return Response({"students": students_serializer.data, "tas": 'No TAs Found'})
            elif tas.exists():
                tas_serializer = Ta_infoSerializer(tas, many=True)
                return Response({"students": 'No Students Found', "tas": tas_serializer.data})
            else:
                return Response({"students": 'No Students Found', "tas": 'No TAs Found'})
        else:
            return Response('Course not found')


@api_view(['GET'])
@csrf_exempt
def Course_announcements(request, id):
    course = Courses.objects.filter(courseId=id)
    if not course.exists():
        return Response('Course Not Found')
    try:
        roll = request.session['roll']
        user = request.session['user']
        if (user == 'TA' and course[0] in Ta_info.objects.filter(Roll=roll)[0].course.all()) or (user == 'student' and course[0] in Student_info.objects.filter(Roll=roll)[0].course.all()):
            if request.method == 'GET':
                announcements = Announcements.objects.filter(course=course[0])
                if announcements.exists():
                    announcement_serializer = AnnouncementsSerializer(
                        announcements, many=True)
                    return Response({"response": announcement_serializer.data, "user": request.session['user']})
                return Response({"response": 'No Announcements found', "user": request.session['user']})
        else:
            return Response('You are not registered for this course')
    except:
        return Response('Please login')


@api_view(['GET', 'POST'])
@csrf_exempt
def Announcement_followup(request, id):
    announcements = Announcements.objects.filter(id=id)
    if not announcements.exists():
        return Response('Announcement Not Found')
    try:
        roll = request.session['roll']
        user = request.session['user']
        if (user == 'TA' and announcements[0].course in Ta_info.objects.filter(Roll=roll)[0].course.all()) or (user == 'student' and announcements[0].course in Student_info.objects.filter(Roll=roll)[0].course.all()):
            if request.method == 'GET':
                followups = Announcement_follow.objects.filter(
                    announcement=announcements[0])
                if followups.exists():
                    followups_serializer = Announcement_followSerializer(
                        followups, many=True)
                    return Response(followups_serializer.data)
                return Response('No follow-ups exist')
            if request.method == 'POST':
                followup_info = JSONParser().parse(request)
                followup_description = followup_info["description"]
                followup = Announcement_follow.objects.create(
                    description=followup_description, announcement=announcements[0], roll=request.session['roll'], name=request.session['name'], user=request.session['user'])
                followup.save()
                return Response('Follow-up added successfully')
        else:
            return Response('You are not registered for this course')
    except:
        return Response('Please login')


@api_view(['POST'])
@csrf_exempt
def Create_Announcement(request, id):
    course = Courses.objects.filter(courseId=id)
    if not course.exists():
        return Response('Course Not Found')
    try:
        if request.session['user'] == 'TA':
            roll = request.session['roll']
            ta = Ta_info.objects.filter(Roll=roll)
            if ta.exists():
                if course[0] in ta[0].course.all():
                    if request.method == 'POST':
                        announcement_info = JSONParser().parse(request)
                        announcement = Announcements.objects.create(
                            description=announcement_info["description"],
                            course=course[0]
                        )
                        announcement.save()
                        return Response('Announcement added successfully')
                return Response('You are not a TA for this course')
            return Response('TA not found')
        return Response('Only TAs can make announcements')
    except:
        return Response('Please login')


@api_view(['POST', 'GET'])
@csrf_exempt
def Discussion_tab(request, id):
    course = Courses.objects.filter(courseId=id)
    if not course.exists():
        return Response('Course Not Found')
    try:
        roll = request.session['roll']
        user = request.session['user']
        if (user == 'TA' and course[0] in Ta_info.objects.filter(Roll=roll)[0].course.all()) or (user == 'student' and course[0] in Student_info.objects.filter(Roll=roll)[0].course.all()):
            if request.method == 'GET':
                discussions = Discussions.objects.filter(course=course[0])
                if discussions.exists():
                    discussions_serializer = DiscussionsSerializer(
                        discussions, many=True)
                    return Response(discussions_serializer.data)
                return Response('No Discussions Found')
            if request.method == 'POST':
                discussion_info = JSONParser().parse(request)
                discussion = Discussions.objects.create(
                    description=discussion_info['description'],
                    course=course[0],
                    roll=request.session['roll'],
                    name=request.session['name'],
                    user=request.session['user']
                )
                discussion.save()
                return Response('Discussion posted successfully')
        else:
            return Response('You are not registered for this course')
    except:
        return Response('Please login')


@api_view(['POST', 'GET'])
@csrf_exempt
def assignment_tab(request, id):
    course = Courses.objects.filter(courseId=id)
    if not course.exists():
        return Response('Course Not Found')
    try:
        roll = request.session['roll']
        user = request.session['user']
        if (user == 'TA' and course[0] in Ta_info.objects.filter(Roll=roll)[0].course.all()) or (user == 'student' and course[0] in Student_info.objects.filter(Roll=roll)[0].course.all()):
            if request.method == 'GET':
                assignments = Assignments.objects.filter(course=course[0])
                if assignments.exists():
                    assignment_serializer = AssignmentsSerializer(
                        assignments, many=True)
                    return Response(assignment_serializer.data)
                return Response('No Assignments Found')
            if request.method == 'POST':
                if user == 'TA':
                    assignment_info = JSONParser().parse(request)
                    assignment = Assignments.objects.create(
                        description=assignment_info['description'],
                        course=course[0],
                        date_submission=assignment_info['date_submission'],
                        roll=request.session['roll'],
                        name=request.session['name']
                    )
                    assignment.save()
                    return Response('Assignment added successfully')
                return Response('Only TAs can add assignments')
        else:
            return Response('You are not registered for this course')
    except:
        return Response('Please login')
