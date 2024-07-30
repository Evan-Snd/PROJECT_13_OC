from django.shortcuts import render
from .models import Profile


def profiles_index(request):
    """
    Renders the profiles index page with a list of all profiles.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object with the rendered template.
    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)


def profile(request, username):
    """
    Renders the profile detail page for a specific user profile.

    Args:
        request (HttpRequest): The request object.
        username (str): The username of the profile to be displayed.

    Returns:
        HttpResponse: The response object with the rendered template.
    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profile.html', context)
