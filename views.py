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
    order = ''
    order_type = ''
    
    if request.GET.has_key('o'):
        order = request.GET['o']
        if request.GET.has_key('ot'):
            order_type = request.GET['ot']
            if order_type == 'asc':
                if order == 'mod':
                    query = Server.objects.all().order_by('last_modified')
                elif order == 'name':
                    query = Server.objects.all().order_by('hostname')
                elif order == 'domain':
                    query = Server.objects.all().order_by('domain')
                elif order == 'type':
                    query = Server.objects.all().order_by('-is_physical')
                elif order == 'ishost':
                    query = Server.objects.all().order_by('guest_set')
                elif order == 'host':
                    query = Server.objects.all().order_by('host')
                else:
                    query = Server.objects.all()
            else:
                order_type = 'dsc'
                if order == 'mod':
                    query = Server.objects.all().order_by('-last_modified')
                elif order == 'name':
                    query = Server.objects.all().order_by('-hostname')
                elif order == 'domain':
                    query = Server.objects.all().order_by('-domain')
                elif order == 'type':
                    query = Server.objects.all().order_by('is_physical')
                elif order == 'ishost':
                    query = Server.objects.all().order_by('-guest_set')
                elif order == 'host':
                    query = Server.objects.all().order_by('-host')
                else:
                    query = Server.objects.all()

    else:
        query = Server.objects.all()
            
    return list_detail.object_list(
        request,
        queryset=query,
        template_name='techventory/server_list.html',
        paginate_by=20,
        page=page,
        extra_context={'ot': order_type, 'o': order}
    )

def server_detail(request, object_id):
    return list_detail.object_detail(
        request,
        queryset=Server.objects.all(),
        template_name='techventory/server_detail.html',
        object_id=object_id,
    )