from django.shortcuts import render, get_object_or_404, redirect
from .models import Cars, CarsImage, AddCar, AddCarImage, CarParts, Accessories, Problem, Craftsman, CarsYear, About
from .forms import UserForm, CarPartsAddForm, AccessoriesAddForm, ProblemAddForm, ContactsForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    posts = CarsYear.objects.all()
    return render(request, 'main/index.html', {'posts': posts})


def model(request, year_id):
    year = get_object_or_404(CarsYear, pk=year_id)
    return render(request, 'main/model.html', {'year': year})


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


@login_required(login_url='login_user')
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


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = UserForm()
    return render(request, 'main/register.html', {'form': form})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'main/login_user.html')


def logout_user(request):
    logout(request)
    return redirect('index')


@login_required(login_url='login_user')
def home(request):
    return render(request, 'main/home.html')


def car_parts(request):
    posts = CarParts.objects.all()
    return render(request, 'main/car_parts.html', {'posts': posts})


@login_required(login_url='login_user')
def add_car_parts(request):
    if request.method == 'POST':
        form = CarPartsAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('car_parts')
    form = CarPartsAddForm()
    return render(request, 'main/add_car_parts.html', {'form': form})


def accessories(request):
    posts = Accessories.objects.all()
    return render(request, 'main/accessories.html', {'posts': posts})


@login_required(login_url='login_user')
def add_accessories(request):
    if request.method == 'POST':
        form = AccessoriesAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accessories')
    form = AccessoriesAddForm()
    return render(request, 'main/add_accessories.html', {'form': form})


def problem(request):
    posts = Problem.objects.all()
    return render(request, 'main/problem.html', {'posts': posts})


@login_required(login_url='login_user')
def add_problem(request):
    if request.method == 'POST':
        form = ProblemAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('problem')
    form = ProblemAddForm()
    return render(request, 'main/add_problem.html', {'form': form})


def craftsman(request):
    posts = Craftsman.objects.all()
    return render(request, 'main/craftsman.html', {'posts': posts})


def youtube(request):
    return render(request, 'main/youtube.html')


def about(request):
    posts = About.objects.all()
    return render(request, 'main/about.html', {'posts': posts})


def contact(request):
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = ContactsForm()
    return render(request, 'main/contact.html', {'form': form})