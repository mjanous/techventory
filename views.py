from django.shortcuts import render_to_response
from django.views.generic import list_detail
from techventory.models import *
from django.conf import settings

media_url = settings.MEDIA_URL

def index(request):
    return render_to_response(
        'techventory/index.html',
        {
            'media_url': media_url,
            'request': request,
        }
    )

def server_list(request, page):
    return list_detail.object_list(
        request,
        queryset=Server.objects.all(),
        template_name='techventory/server_list.html',
        paginate_by=25,
        page=page,
        extra_context={'media_url': media_url},
    )

def server_detail(request, object_id):
    return list_detail.object_detail(
        request,
        queryset=Server.objects.all(),
        template_name='techventory/server_detail.html',
        object_id=object_id,
        extra_context={'media_url': media_url},
    )