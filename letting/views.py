import logging
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Letting

logger = logging.getLogger(__name__)


def lettings_index(request: HttpRequest) -> HttpResponse:
    """
    Renders the lettings index page with a list of all lettings.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object with the rendered template.
    """
    try:
        lettings_list = Letting.objects.all()
        context = {'lettings_list': lettings_list}
        return render(request, 'lettings_index.html', context)
    except Exception as e:
        logger.error("Error rendering lettings index: %s", e)
        raise


def letting(request: HttpRequest, letting_id: int) -> HttpResponse:
    """
    Renders the letting detail page for a specific letting.

    Args:
        request (HttpRequest): The request object.
        letting_id (int): The ID of the letting to be displayed.

    Returns:
        HttpResponse: The response object with the rendered template.
    """
    try:
        letting = Letting.objects.get(id=letting_id)
        context = {
            'title': letting.title,
            'address': letting.address,
        }
        return render(request, 'letting.html', context)
    except Letting.DoesNotExist:
        logger.warning("Letting not found for id: %d", letting_id)
        return HttpResponse("Letting not found", status=404)
    except Exception as e:
        logger.error("Error rendering letting for id %d: %s", letting_id, e)
        raise
