from django.urls import path
from .views import ShoeList, ShoeDetail,index

urlpatterns = [
    path('',index),
    path('shoes/', ShoeList.as_view()),
    path('shoes/<int:pk>/', ShoeDetail.as_view()),
]
