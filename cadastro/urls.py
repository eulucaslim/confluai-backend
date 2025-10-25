from django.urls import path, include
from rest_framework import routers
from cadastro import views

router = routers.DefaultRouter()


router.register('alunos', views.AlunoViewSet, basename='alunos')
router.register('cursos', views.CursoViewSet, basename='cursos')
router.register('empresas', views.EmpresaViewSet, basename='empresas')

urlpatterns = [
    path('', include(router.urls))
]