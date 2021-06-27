from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.template import loader
from django.shortcuts import render, redirect
from django.utils import timezone
from urllib.parse import urlparse
from django.contrib.auth.decorators import login_required
from os.path import normpath
from .models import Bookmarks

# Create your views here.

@login_required
def index(request: HttpRequest):
    print('calling index with', request.path)
    bookmarks = Bookmarks.objects.filter(is_deleted=False)
    #template = loader.get_template('bookmarks/list.html')
    context = {
        'bookmarks': bookmarks,
    }
    #return HttpResponse(template.render(context, request))
    return render(request, 'bookmarks/list.html', context)

@login_required
def resolve(request: HttpRequest):
    alias = normalize_path(request.path)
    print("serving request for", request.path, " original request:", alias)
    
    try:
        ## try to resolve
        bookmark = Bookmarks.objects.get(is_deleted=False, alias=alias)
        print("redirecting to", bookmark.destination)
        return redirect(bookmark.destination)
    except Bookmarks.DoesNotExist:
        ## try to find reference path
        print('bookmark not found. cannot redirect')
        sep_alias = alias+"/"   ## adding / to add heirarchy separation, we are not doing just substring matching
        bookmarks = Bookmarks.objects.filter(is_deleted=False, alias__startswith=sep_alias)
        if bookmarks:
            print('sending bunch of bookmarks...')
            return render(request, "bookmarks/list.html", {'bookmarks': bookmarks})
        
    # bookmark is none - need to add
    print('no bookmark with given prefix, adding...')
    return render(request, 'bookmarks/add.html', { 'alias_inp' : alias})

@login_required
def add_alias(request: HttpRequest, alias_inp: str):
    destination_url = request.POST['destination_url']
    bookmark = Bookmarks(alias = alias_inp,
                         destination = destination_url,
                         mod_date = timezone.now())
    bookmark.save()
    return redirect('bookmarks:bookmark_list')

def normalize_path(request_path):
    start = 1 if request_path.startswith('/') else 0
    return normpath(request_path)[start:]
