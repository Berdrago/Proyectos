from api.Cuenta.CuentaSRL import cuentaserializado
from django.contrib.auth.models import User
from api.models import Cuenta
from rest_framework.response import Response
from rest_framework.views import APIView

class CuentaAPI(APIView):
    def get(self, request, id):             
        usuario = User.objects.get(id=id)
        cuenta = Cuenta.objects.get(usuario=usuario)    
        serializado = cuentaserializado (cuenta)
        return Response( serializado.data, status=200)