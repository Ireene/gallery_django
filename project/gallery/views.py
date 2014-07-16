from django.shortcuts import render, render_to_response
from gallery.models import Album, Image, Comment
from django.http import HttpResponse
from forms import AlbumForm, ImageForm, CommentForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.utils import timezone
from django.conf import settings
from django.template import RequestContext
from django.contrib import messages


def albums(request):
    args = {}
    args.update(csrf(request))
    
    args['albums'] = Album.objects.all()
        
    return render(request,'albums.html', args)

    
def album(request, album_id=1):
    
    args = {}
    args.update(csrf(request))
    
    args['album'] = Album.objects.get(id=album_id)
  
    
    return render(request,'album.html', args)
    
def show_image(request, image_id=1):
    return render(request,'show_image.html',
                              {'image': Image.objects.get(id=image_id)})
                              
def create_image(request):
    if request.POST:
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/galleries/albums/')
    else:
        form = ImageForm()
        
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    
    return render(request,'create_image.html', args)
    
def create_album(request,album_id=1):
    if request.POST:
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/galleries/albums/')
    else:
        form = AlbumForm()
        
    args = {}
    args.update(csrf(request))
    

    args['form'] = form
    
    return render(request,'create_album.html', args)

def delete_image(request, image_id):
    c = Image.objects.get(id=image_id)
    
    c.delete()

    return HttpResponseRedirect("/galleries/albums/")



def add_comment(request, image_id):
    a = Image.objects.get(id=image_id)
    
    if request.method == "POST":
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.image = a
            c.save()
            
            return HttpResponseRedirect('/galleries/show_image/%s' % image_id)
        
    else:
        f = CommentForm()
        
    args = {}
    args.update(csrf(request))
    
    args['image'] = a
    args['form'] = f
    
    return render(request,'add_comment.html', args)