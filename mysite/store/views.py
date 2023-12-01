from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.shortcuts import render
from .models import Painting, Review
from .forms import PaintingForm



def main_menu(request):
    paintings = Painting.objects.all()
    return render(request, 'store/main.html', {'paintings': paintings})

def about(request):
    return render(request,'store/about.html')
def painting_list(request):
    paintings = Painting.objects.all()
    return render(request, 'store/painting_list.html', {'paintings': paintings})

def add_painting(request):
    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('painting_list')  # Или куда вы хотите перенаправить пользователя после добавления
    else:

        form = PaintingForm()
    return render(request, 'store/add_painting.html', {'form': form})
def delete_painting(request, id):
    painting = get_object_or_404(Painting, id=id)
    painting.delete()
    return redirect('painting_list')  # Верните пользователя обратно к списку картин


def edit_painting(request, id):
    painting = get_object_or_404(Painting, id=id)
    image_url = painting.image.url if painting.image else None

    if request.method == 'POST':
        form = PaintingForm(request.POST, request.FILES, instance=painting)
        if form.is_valid():
            form.save()
            return redirect('painting_list')
    else:
        form = PaintingForm(instance=painting)

    context = {
        'form': form,
        'painting': painting,
        'image_url': image_url,
    }

    return render(request, 'store/edit_painting.html', context)