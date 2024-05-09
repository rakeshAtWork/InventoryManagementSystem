from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *


# here in this case we did not require diffrent route for different api call.
class StudentAPI(APIView):
    def get(self, request):
        student_obj = Student.objects.all()  # fetched all the students data using query
        serializer = StudentSerializer(student_obj, many=True)
        return Response({"status": 200, "payload": serializer.data})

    def post(self, request):
        data = request.data
        serializer = StudentSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": 200, "message": "Student Created Successfully"})

        return Response({"status": 403, "error": serializer.errors, "message": "Bad Request, Something went Wrong!"})

    def put(self, request):
        try:
            studentobj = Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(studentobj, data=request.data,
                                           )  # here we have converted PUT to Patch Method.
            if serializer.is_valid():
                serializer.save()
                return Response({"status": 200, "message": "Student Updated Successfully"})

            return Response(
                {"status": 403, "error": serializer.errors, "message": "Bad Request, Something went Wrong!"})
        except Exception as e:
            return Response({"status": 403, "error": str(e), "message": "Invalid Id"})

    def patch(self, request):
        try:
            studentobj = Student.objects.get(id=request.data['id'])
            serializer = StudentSerializer(studentobj, data=request.data,
                                           partial=True)  # here we have converted PUT to Patch Method.
            if serializer.is_valid():
                serializer.save()
                return Response({"status": 200, "message": "Student Updated Successfully"})

            return Response(
                {"status": 403, "error": serializer.errors, "message": "Bad Request, Something went Wrong!"})
        except Exception as e:
            return Response({"status": 403, "error": str(e), "message": "Invalid Id"})

    def delete(self, request):
        try:
            studentobj = Student.objects.get(id=request.data['id'])
            studentobj.delete()
            return Response({"status": 200, "message": "Student Deleted Successfully"})
        except Exception as e:
            return Response({"status": 403, "error": str(e), "message": "Invalid Id"})
