from django.urls import path
from . import views
urlpatterns = [
    path('',views.listar_producto, name= 'listar_productos'),
    path('crear/', views.crear_producto, name= 'crear_producto'),
    path('editar/<int:producto_id>/', views.editar_producto, name= 'editar_producto'),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name= 'eliminar_producto'),
]
