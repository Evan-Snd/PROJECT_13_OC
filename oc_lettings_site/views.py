import logging
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

logger = logging.getLogger(__name__)


def index(request: HttpRequest) -> HttpResponse:
    """
    Renders the index page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object with the rendered template.
    """
    try:
        return render(request, 'index.html')
    except Exception as e:
        logger.error("Error rendering index page: %s", e)
        raise


def custom_404(request: HttpRequest, exception: Exception) -> HttpResponse:
    """
    Renders the custom 404 error page.

    Args:
        request (HttpRequest): The request object.
        exception (Exception): The exception that triggered the 404 error.

    Returns:
        HttpResponse: The response object with the rendered template.
    """
    try:
        return render(request, '404.html', status=404)
    except Exception as e:
        logger.error("Error rendering custom 404 page: %s", e)
        raise


def custom_500(request: HttpRequest) -> HttpResponse:
    """
    Renders the custom 500 error page.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object with the rendered template.
    """
    try:
        return render(request, 'errors/500.html', status=500)
    except Exception as e:
        logger.error("Error rendering custom 500 page: %s", e)
        raise