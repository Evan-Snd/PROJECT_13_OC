from django.shortcuts import render
from .models import Profile


def profiles_index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)


def profile(request, username):
    """
    Récupère et affiche le profil d'un utilisateur donné.

    Arguments :
        request (HttpRequest) : L'objet HttpRequest de la requête HTTP.
        username (str) : Le nom d'utilisateur pour lequel le profil doit être récupéré.

    Retourne :
        HttpResponse : Un objet HttpResponse avec la page de profil rendue.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profile.html', context)
