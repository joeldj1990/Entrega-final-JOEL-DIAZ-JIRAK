from django.urls import path
from .views import buscar, inicio, horario, armazones, preguntas, anteojos_sol, lentes, armazones_formulario, sol_formulario, lentes_formulario, busqueda_codigo

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('horario/', horario, name="Horarios"),
    path('armazones/', armazones, name="Armazones"),
    path('preguntas-frecuentes/', preguntas, name="Preguntas"),
    path('anteojos-de-sol/', anteojos_sol, name="Anteojos_Sol"),
    path('lentes/', lentes, name="Lentes"),
    path('armazones-formulario/', armazones_formulario, name="Armazones_Formulario"),
    path('sol-formulario/', sol_formulario, name="Sol_Formulario"),
    path('lentes-formulario/', lentes_formulario, name="Lentes_Formulario"),
    path('busqueda/', busqueda_codigo, name="Busqueda"),
    path('buscar/', buscar, name="Buscar"),
]