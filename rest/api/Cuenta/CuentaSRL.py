from api.Libro.LibroSRL import libroserializado
from api.models import Cuenta
from rest_framework import serializers

class cuentaserializado (serializers.ModelSerializer):
    usuario = serializers.CharField(required = False)
    libro = libroserializado(required = False, many=True)
    class Meta :
        model = Cuenta
        fields = ['usuario','libro']
