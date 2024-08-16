from django.shortcuts import render
from .models import Letting


def index(request):
    return render(request, 'index.html')


def lettings_index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings_index.html', context)


def letting(request, letting_id):
    """
    Récupère et affiche les détails d'un bien spécifique par son ID.

    Cette vue récupère les informations d'un bien à partir de son identifiant unique,
    puis rend un template HTML avec ces informations.

    Arguments:
    request -- L'objet HttpRequest.
    letting_id -- L'identifiant unique du bien à afficher.

    Retourne:
    HttpResponse -- Une réponse HTTP avec le rendu du template letting.html.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting.html', context)
