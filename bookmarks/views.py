from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import loader
from django.shortcuts import render, redirect
from django.utils import timezone
from urllib.parse import urlparse
from os.path import normpath
from .models import Bookmarks

# Create your views here.

def index(request: HttpRequest):
    print('calling index with', request.path)
    bookmarks = Bookmarks.objects.filter(is_deleted=False)
    #template = loader.get_template('bookmarks/list.html')
    context = {
        'bookmarks': bookmarks,
    }
    print(bookmarks)
    #return HttpResponse(template.render(context, request))
    return render(request, 'bookmarks/list.html', context)

def resolve(request: HttpRequest):
    alias = normalize_path(request.path)
    print("serving request for", request.path, " original request:", alias)
    
    try:
        bookmark = Bookmarks.objects.get(is_deleted=False, alias=alias)
    except Bookmarks.DoesNotExist:
        bookmark = None
    print(bookmark)
    if bookmark != None:
        print("redirecting to", bookmark.destination)
        return redirect(bookmark.destination)

    # bookmark is none - need to add
    #return redirect('add_alias', alias)
    return render(request, 'bookmarks/add.html', { 'alias_inp' : alias})

def add_alias(request: HttpRequest, alias_inp: str):
    destination_url = request.POST['destination_url']
    bookmark = Bookmarks(alias = alias_inp,
                         destination = destination_url,
                         mod_date = timezone.now())
    bookmark.save()
    return redirect('bookmarks:index')
    
    #expects alias and url (from form)
    #print('alias received: ', alias)
    #return HttpResponse("ok")

def normalize_path(request_path):
    start = 1 if request_path.startswith('/') else 0
    return normpath(request_path)[start:]
