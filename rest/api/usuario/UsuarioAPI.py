from api.usuario.UsuarioSRL import usuarioserializado
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView

class UsuarioAPI(APIView):
    def get(self, request):
        Usuarios = User.objects.all()
        serializado = usuarioserializado (Usuarios , many=True )
        return Response( serializado.data, status=200)

    def post (self, request):
        data = request.data 
        serializado = usuarioserializado (data=data)
        if serializado.is_valid():
            serializado.save()
            return Response(serializado.data, status=200)
        else:
            return Response(serializado.errors, status=400)
    def put(self,request):  
        data = request.data         
        Usuarios = User.objects.get(id = id)
        serializado = usuarioserializado (Usuarios, data=data)
        if serializado.is_valid():
            serializado.save()
            return Response(serializado.data, status=200)
        else:
            return Response(serializado.errors, status=400)
    
    def delete(self,request):
        Usuarios = User.objects.get(id = id )
        Usuarios.delete()
        return Response(status=200)



    
