from django.urls import path, include
from rest_framework import routers
from cadastro import views

router = routers.DefaultRouter()


router.register('alunos', views.AlunoViewSet, basename='alunos')

urlpatterns = [
    path('', include(router.urls))
]