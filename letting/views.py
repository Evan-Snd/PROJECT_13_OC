from django.shortcuts import render
from .models import Letting


def lettings_index(request):
    """
    Renders the lettings index page with a list of all lettings.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object with the rendered template.
    """
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings_index.html', context)


def letting(request, letting_id):
    """
    Renders the letting detail page for a specific letting.

    Args:
        request (HttpRequest): The request object.
        letting_id (int): The ID of the letting to be displayed.

    Returns:
        HttpResponse: The response object with the rendered template.
    """
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting.html', context)
