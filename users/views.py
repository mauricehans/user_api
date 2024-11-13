from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from .models import CustomUser
from .serializers import CustomUserSerializer
# pour toutes les methodes de l'app users
@method_decorator(csrf_exempt, name='dispatch')
class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
