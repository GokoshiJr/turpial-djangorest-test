from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse, HttpResponse
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.views import APIView

class UserLogin(APIView):
    def post(self, request, format=None):

        username = request.data["username"]
        password = request.data["password"]

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        pwd_valid = check_password(password, user.password)

        if not pwd_valid:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

        token, _ = Token.objects.get_or_create(user=user)

        return JsonResponse({"token": token.key}, status=status.HTTP_200_OK)
