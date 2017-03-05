from django.shortcuts import render
from django.http import HttpResponse
# from django.shortcuts import loader
from .models import Album


# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
    'all_albums':all_albums,
    }
    return HttpResponse(template.render(context, request)
    #return HttpResponse(template.render(request, 'music/index.html', context))
    # return HttpResponse("<h2>this is music home page</h2>")

def detail(request, album_id):
    return HttpResponse("<h2>Detail of the album id:" + str(album_id) + "</h2>")
