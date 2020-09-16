from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Movie,Customer
from .serializers import Movieserializer,Customerserializer
from rest_framework.views import APIView

class MovieAPIList(APIView):
    """
    List all snippets, or create a new movies.
    """
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = Movieserializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Movieserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetail(APIView):
    """
    Retrieve, update or delete a movies instance.
    """
    def get_object(self, pk):
        try:
            return Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movies = self.get_object(pk)
        serializer = Movieserializer(movies)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        movies = self.get_object(pk)
        serializer = Movieserializer(movies, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movies = self.get_object(pk)
        movies.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerAPIList(APIView):
    """
    List all snippets, or create a new movies.
    """
    def get(self, request, format=None):
        customers = Customer.objects.all()
        serializer = Customerserializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        #tickets & movie name
        #call movie object whose name is theatre & update the ticket
        tik=request.data['tickets']
        th=request.data['theatre']
        movie_in = Movie.objects.get(movietheatre=th)
        movie_in.seats-=tik
        movie_in.save()
        serializer = Customerserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetail(APIView):
    """
    Retrieve, update or delete a movies instance.
    """
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customers = self.get_object(pk)
        serializer = Customerserializer(customers)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        customers = self.get_object(pk)
        tikold=customers.tickets
        serializer = Customerserializer(customers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            tik=request.data['tickets']
            th=request.data['theatre']
            movie_in = Movie.objects.get(movietheatre=th)
            movie_in.seats=movie_in.seats + tikold -tik
            movie_in.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        customers = self.get_object(pk)
        tik=customers.tickets
        th=customers.theatre
        movie_in = Movie.objects.get(movietheatre=th)
        movie_in.seats=movie_in.seats + tik
        movie_in.save()
        customers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

