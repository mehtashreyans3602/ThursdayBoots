from django.urls import path
from .views import ShoeList, ShoeDetail,index,dummy_data

urlpatterns = [
    path('dummy',dummy_data),
    path('',index),
    path('shoes/', ShoeList.as_view()),
    path('shoes/<int:pk>/', ShoeDetail.as_view()),
]
