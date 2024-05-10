from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *
from rest_framework import status
# JWT implementation

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken





# User Register
class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            refresh = RefreshToken.for_user(user)
            return Response(
                {"status": 200, "message": "User Created Successfully", "access": str(refresh.access_token)})
        return Response({"status": 403, "error": serializer.errors, "message": "Bad Request, Something went Wrong!"})

# user login.
class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Login successful",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response({"message": "Invalid username or password"}, status=status.HTTP_400_BAD_REQUEST)



# here in this case we did not require diffrent route for different api call.
class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

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

        return Response(
            {"status": 403, "error": serializer.errors, "message": "Bad Request, Something went Wrong!"})

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
