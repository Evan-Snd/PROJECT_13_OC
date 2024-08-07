import logging
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Profile

logger = logging.getLogger(__name__)


def profiles_index(request: HttpRequest) -> HttpResponse:
    """
    Renders the profiles index page with a list of all profiles.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object with the rendered template.
    """
    try:
        profiles_list = Profile.objects.all()
        context = {'profiles_list': profiles_list}
        return render(request, 'profiles_index.html', context)
    except Exception as e:
        logger.error("Error rendering profiles index: %s", e)
        raise


def profile(request: HttpRequest, username: str) -> HttpResponse:
    """
    Renders the profile detail page for a specific user profile.

    Args:
        request (HttpRequest): The request object.
        username (str): The username of the profile to be displayed.

    Returns:
        HttpResponse: The response object with the rendered template.
    """
    try:
        profile = Profile.objects.get(user__username=username)
        context = {'profile': profile}
        return render(request, 'profile.html', context)
    except Profile.DoesNotExist:
        logger.warning("Profile not found for username: %s", username)
        return HttpResponse("Profile not found", status=404)
    except Exception as e:
        logger.error("Error rendering profile for username %s: %s", username, e)
        raise
