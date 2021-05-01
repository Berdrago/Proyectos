from api.Libro.LibroSRL import libroserializado
from api.models import libro
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class LibroAPI(APIView):
    permission_classes= [IsAuthenticated]
    def get(self, request, id):
        try :
            Libro = libro.objects.all()
            serializado = libroserializado(Libro , many=True )
            return Response( serializado.data, status=200)
        except:
            return Response(status=400)
    def post (self, request):
        serializado = libroserializado(data=request.data)
        if serializado.is_valid():
            serializado.save()
            return Response(serializado.data, status=200)
        else:
            return Response(serializado.errors, status=400)
    def put(self,request, id):  
        data = request.data         
        Libro = libro.objects.get(id = id)
        
        serializado = libroserializado (Libro, data=data)
        if serializado.is_valid():
            serializado.save()
            return Response(serializado.data, status=200)
        else:
            return Response(serializado.errors, status=400)
    
    def delete(self,request, id):
        Libro = libro.objects.get(id = id )
        Libro.delete()
        return Response(status=200)

    
