from django.urls import path, include

from taxi.views import CreateDriverSerialiser, DriverList, DriverDetail

urlpatterns = [
    path('driver/create', CreateDriverSerialiser.as_view()),
    path('all', DriverList.as_view()),
    path('driver/detail/<int:pk>/', DriverDetail.as_view()),
]