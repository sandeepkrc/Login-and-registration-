from .serializer import RegisterSerializer,  AuthenticationSerializer,UserSerializer
from rest_framework.decorators import APIView, api_view
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response


class Login(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = AuthenticationSerializer

class userGetViewSet(APIView):
    serializer_class = UserSerializer#extra
    def get(self, request):
        try:
            print(self.request.user)
            user = User.objects.get(id=self.request.user.id)
        except User.DoesNotExist:
            return Response({'error': " Invalid user ID"})
        ser = userGetSerializer(user, many=False)
        return Response(ser.data)

@api_view(['GET', 'POST'])
def Registerapi(request):
    user_serializer = RegisterSerializer(data=request.data)
    if user_serializer.is_valid():
        user_serializer.save()
        return Response(user_serializer.data, status=status.HTTP_201_CREATED)
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
