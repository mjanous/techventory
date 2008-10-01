from django.shortcuts import render_to_response
from django.views.generic import list_detail
from techventory.models import *
from django.conf import settings

def index(request):
    return render_to_response(
        'techventory/index.html',
        {
            'request': request,
            'MEDIA_URL': settings.MEDIA_URL,
        }
    )

def server_list(request, page):
    if request.GET.has_key('order_by'):
        order_by = request.GET['order_by']
        if order_by == 'mod':
            query = Server.objects.all().order_by('-last_modified')
        elif order_by == '-mod':
            query = Server.objects.all().order_by('last_modified')
        elif order_by == 'name':
            query = Server.objects.all().order_by('hostname')
        elif order_by == '-name':
            query = Server.objects.all().order_by('-hostname')
        elif order_by == 'domain':
            query = Server.objects.all().order_by('domain')
        elif order_by == '-domain':
            query = Server.objects.all().order_by('-domain')
        elif order_by == 'type':
            query = Server.objects.all().order_by('is_physical')
        elif order_by == '-type':
            query = Server.objects.all().order_by('-is_physical')
        elif order_by == 'ishost':
            query = Server.objects.all().order_by('guest_set')
        elif order_by == '-ishost':
            query = Server.objects.all().order_by('-guest_set')
        elif order_by == 'host':
            query = Server.objects.all().order_by('host')
        elif order_by == '-host':
            query = Server.objects.all().order_by('-host')
        else:
            query = Server.objects.all()
    else:
        query = Server.objects.all()
        order_by = ''
            
    return list_detail.object_list(
        request,
        queryset=query,
        template_name='techventory/server_list.html',
        paginate_by=20,
        page=page,
        extra_context={'order_by': order_by}
    )

def server_detail(request, object_id):
    return list_detail.object_detail(
        request,
        queryset=Server.objects.all(),
        template_name='techventory/server_detail.html',
        object_id=object_id,
    )