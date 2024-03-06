from .models import Profissional, Consulta
from .serializer import ProfSerializer, CadSerializer
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.views import APIView
from django.urls import reverse


# Interface para links de listas de Profissionais e Consultas abaixo:

class ProfissionalApi(viewsets.ModelViewSet):

    queryset = Profissional.objects.all()

    serializer_class= ProfSerializer


class clinicaApi(viewsets.ModelViewSet):

    queryset = Consulta.objects.all()

    serializer_class = CadSerializer
    


# CRUD para as Consultas abaixo:
    

class ConsultDetail(APIView):
    
    def get_consulta_by_pk(self, pk):

        try:

            return Consulta.objects.get(pk=pk)
        
        except:

            return Response({'Erro': 'A consulta não existe.'})
        

    def delete(self, request, pk):

       consulta = self.get_consulta_by_pk(pk)

       consulta.delete()

       return Response(status=status.HTTP_204_NO_CONTENT)
    


    def get(self, request, pk):
       consulta = self.get_consulta_by_pk(pk)
       serializer = CadSerializer(consulta)
       return Response(serializer.data)


    def put(self, request, pk):

       consulta = self.get_consulta_by_pk(pk)

       serializer = CadSerializer(consulta, data=request.data)

       if serializer.is_valid():

           serializer.save()

       return Response(serializer.errors)
    

# CRUD para os Profissionais abaixo:


class ProfDetail(APIView):
    
    def get_profissional_by_pk(self, pk):
        try:
            return Profissional.objects.get(pk=pk)
        except:
            return Response({'Erro': 'O profissional não existe.'})
        

    def delete(self, request, pk):

       prof = self.get_profissional_by_pk(pk)

       prof.delete()

       return Response(status=status.HTTP_204_NO_CONTENT)
    


    def get(self, request, pk):
       
       prof = self.get_profissional_by_pk(pk)

       serializer = ProfSerializer(prof)

       return Response(serializer.data)


    def put(self, request, pk):

       prof = self.get_profissional_by_pk(pk)

       serializer = ProfSerializer(prof, data=request.data)

       if serializer.is_valid():

           serializer.save()

           return Response(serializer.data)

       return Response(serializer.errors)

    