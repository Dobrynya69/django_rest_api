from webbrowser import get
from rest_framework.views import *
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import *
from .models import *
from .permissions import *

class AllCountriesAPIView(APIView):
    def get(self, request, *args, **kwargs):
        serializer = CountrySerializer(Country.objects.all(), many=True)
        return Response(serializer.data, status=200)


    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=404)


class CountryAPIView(APIView):
    permission_classes = (IsAuthorOrReadOnly, permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            country = Country.objects.get(pk=pk)
        except(Country.DoesNotExist):
            return None

        return country


    def get(self, request, *args, **kwargs):
        country = self.get_object(kwargs['pk'])
        if country is None:
            return Response({'Error': 'Item does not exist'}, status = 404)

        serializer = CountrySerializer(country)
        return Response(serializer.data, status=200)


    def delete(self, request, *args, **kwargs):
        country = self.get_object(kwargs['pk'])
        if country is None:
            return Response({'Error': 'Item does not exist'}, status = 404)

        country.delete()
        return Response(status=204)


    def put(self, request, *args, **kwargs):
        country = self.get_object(kwargs['pk'])
        if country is None:
            return Response({'Error': 'Item does not exist'}, status = 404)

        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)
        else:
            return Response(serializer.errors, status = 404)


    def patch(self, request, *args, **kwargs):
        country = self.get_object(kwargs['pk'])
        if country is None:
            return Response({'Error': 'Item does not exist'}, status = 404)

        serializer = CountrySerializer(country, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 200)
        else:
            return Response(serializer.errors, status = 404)

    

