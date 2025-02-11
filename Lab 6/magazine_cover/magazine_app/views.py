from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import MagazineForm

def cover_view(request):
    if request.method == 'POST' and request.FILES['cover_image']:
        # Get form data
        background_color = request.POST.get('background_color', '#FFFFFF')
        font_color = request.POST.get('font_color', '#000000')
        font_size = request.POST.get('font_size', 30)
        font_family = request.POST.get('font_family', 'Arial')
        text_message = request.POST.get('text_message', 'Your Title Here')

        # Handle the uploaded image
        uploaded_image = request.FILES['cover_image']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_image.name, uploaded_image)
        image_url = fs.url(filename)

        # Prepare context for template
        result = {
            'background_color': background_color,
            'font_color': font_color,
            'font_size': font_size,
            'font_family': font_family,
            'text_message': text_message,
            'image_url': image_url,
        }

        return render(request, 'magazine_app/index.html', {'result': result})

    return render(request, 'magazine_app/index.html')
