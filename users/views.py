from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from .serializers import CustomUserSerializer, UserLoginSerializer
from .models import CustomUser
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth import authenticate

class UserLoginView(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        print(f"Attempting to authenticate user: {email}")

        user = authenticate(email=email, password=password)
        
        if user is not None:
            print(f"Authentication successful for user: {email}")
            print(f"Authentication successful for user: {password}")
            access_token = AccessToken.for_user(user)
            return Response({
                'access_token': str(access_token),
                'is_admin': user.is_admin
            }, status=status.HTTP_200_OK)
        else:
            print(f"Authentication failed for user: {email}")
            print(f"Authentication failed for password: {password}")
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)



class UserRegistrationView(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to register
