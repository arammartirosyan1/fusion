from django.shortcuts import render, get_object_or_404
from .models import Cars, CarsImage, AddCar, AddCarImage


# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def cars(request):
    posts = Cars.objects.all()
    return render(request, 'main/cars.html', {'posts': posts})


def detail(request, id):
    post = get_object_or_404(Cars, id=id)
    photos = CarsImage.objects.filter(post=post)
    return render(request, 'main/detail.html', {
        'post': post,
        'photos': photos
    })


def add_car(request):
    if request.method == 'POST':
        length = request.POST.get('length')
        title = request.POST.get('title')
        description = request.POST.get('description')

        post = AddCar.objects.create(
            title=title,
            description=description
        )

        for file_num in range(0, int(length)):
            AddCarImage.objects.create(
                post=post,
                images=request.FILES.get(f'images{file_num}')
            )

    return render(request, 'main/add_car.html')