from django.contrib import admin
from django.urls import path
from .views import MovieAPIList,MovieDetail,CustomerAPIList,CustomerDetail

urlpatterns = [
   #path('article/', article_list),
    path('Movie/', MovieAPIList.as_view()),
    path('detail/<str:pk>/',MovieDetail.as_view() ),
    path('cust/', CustomerAPIList.as_view()),
    path('cdetail/<int:pk>/',CustomerDetail.as_view() )
]