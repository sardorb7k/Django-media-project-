from django.shortcuts import render, redirect
from blog.models import Photos

def HomePage(request):
    photos = Photos.objects.all()
    context = {
        'photos': photos,
    }
    return render(request, 'index.html', context)

def UploadPage(request):
    if request.method == 'POST':
        data = Photos()
        data.title = request.POST.get('title')
        if 'photo' in request.FILES:
            data.photo = request.FILES['photo']
        data.save()
        return redirect('home')
    return render(request, 'upload.html')

