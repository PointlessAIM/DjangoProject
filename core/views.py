from django.views.generic import View
from django.shortcuts import render

# Esta clase es la que se encarga de manejar las peticiones HTTP que llegan al servidor
# y devolver una respuesta HTTP
class HomeView(View):
    # Aquí hacemos nuestra petición GET al servidor, en otras palabras, la información
    # que se va a mostrar en la página web

    # self es una referencia a la instancia de la clase,
    # request es la petición que se hace al servidor
    # *args y **kwargs son argumentos que se pueden pasar a la función, cualquier parametro
    # que el objeto de la petición pueda tener
    def get(self, request, *args, **kwargs):
        # Aquí se crea el contexto, es decir, la información que se va a mostrar en la página
        # web, en este caso, no hay nada que mostrar
        context = {


        }

        return render(request, "index.html", context)