from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """
    Renders the index page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object with the rendered template.
    """
    return render(request, 'index.html')


def custom_404(request, exception):
    """
    Renders the custom 404 error page.

    Args:
        request (HttpRequest): The request object.
        exception (Exception): The exception that triggered the 404 error.

    Returns:
        HttpResponse: The response object with the rendered template.
    """
    return render(request, '404.html', status=404)


def custom_500(request):
    """
    Renders the custom 500 error page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object with the rendered template.
    """
    return render(request, '500.html', status=500)
