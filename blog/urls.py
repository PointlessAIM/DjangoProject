from django.urls import path

from .views import BlogListView, BlogCreateView, BlogDetailView
# 
app_name= "blog"

urlpatterns= [
    # Dejamos vacío el path porque es la página principal
    # name="home" es el nombre de la url, se usa para referenciar a la url en otros
    # archivos
    # el path queda vacío porque es la página principal, es la raiz del sitio
    path("", BlogListView.as_view(), name="home"),
    path("create/", BlogCreateView.as_view(), name="create"),
    # <int:pk> es un parámetro que se le pasa a la url, en este caso es el id del post
    # int: significa que es un número entero
    path("<int:pk>/", BlogDetailView.as_view(), name="detail"),

]