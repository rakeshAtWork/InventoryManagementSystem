from django.http import HttpResponse
from django.views import View

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *


class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello, Django!")


# just returning the Json Response
@api_view()
def hello_world(request):
    return Response({"status": 200, "message": "Hello, world!"})


# in a decorator we have all the methods [GET, POST, PUT, DELETE]
@api_view(["GET"])
def all_data(request):
    student_obj = Student.objects.all()  # fetched all the students data using query
    serializer = StudentSerializer(student_obj, many=True)
    return Response({"status": 200, "payload": serializer.data})


@api_view(["POST"])
def CreateStudent(request):
    data = request.data
    serializer = StudentSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({"status": 200, "message": "Student Created Successfully"})

    return Response({"status": 403, "error": serializer.errors,"message": "Bad Request, Something went Wrong!"})
