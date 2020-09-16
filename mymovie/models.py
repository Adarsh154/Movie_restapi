from django.db import models


class Movie(models.Model):
    movietheatre = models.CharField(max_length=100,primary_key=True)
    movietitle = models.CharField(max_length=100)
    seats = models.IntegerField()
    address = models.TextField()

    def __str__(self):
       return self.movietheatre



class Customer(models.Model):
    name = models.CharField(max_length=100)
    tickets = models.IntegerField(default=0)
    theatre = models.ForeignKey(Movie,default=None, on_delete=models.CASCADE)
    #theatre = models.CharField(max_length=100)

    def __str__(self):
       return self.name