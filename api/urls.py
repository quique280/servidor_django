from django.urls import path

from .views import PruebaAPIView, PruebaAPIDetail, PruebaAPIAllView
from .views import DeduccionAPIView, DeduccionAPIDetail, DeduccionAPIAllView
from .views import InferenciaAPIView, InferenciaAPIDetail, InferenciaAPIAllView

urlpatterns = [
    path('pruebas', PruebaAPIView.as_view()),
    path('pruebas/<int:pk>/', PruebaAPIDetail.as_view()),
    path('pruebas/all', PruebaAPIAllView.as_view()),
    path('deducciones', DeduccionAPIView.as_view()),
    path('deducciones/<int:pk>/', DeduccionAPIDetail.as_view()),
    path('deducciones/all', DeduccionAPIAllView.as_view()),
    path('inferencias', InferenciaAPIView.as_view()),
    path('inferencias/<int:pk>/', InferenciaAPIDetail.as_view()),
    path('inferencias/all', InferenciaAPIAllView.as_view()),
]