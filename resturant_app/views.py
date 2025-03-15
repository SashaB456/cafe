from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from resturant_app.models import Review
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("get-reviews")
    else:
        form = UserCreationForm()
    return render(request, context={"form": form}, template_name='register.html')
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('get-reviews')
            else:
                messages.error(request,'Неправильний логін та пароль.')
def get_posts(request):
    context = Review.objects.all()
    return render(request, context={"reviews": context}, template_name='get_reviews.html')
def create_post(request):
    if request.method == "POST":
        title = request.POST.get("title", default="Ого! Я полетів на Мальдіви!О")
        text = request.POST.get("text", default="Ого! Я полетів на Мальдіви!")
        author = request.POST.get("author", default="Саша")
        pub_date = request.POST.get("pub_date", default="2025-03-28 16:37")
        try:
            review = Review.objects.create(
            title=title,
            text=text,
            author=author,
            pub_date=pub_date,)
        except ValueError:
            return HttpResponse("Error", status=400)
        review = Review.objects.create(
            title=title,
            text=text,
            author=author,
            pub_date=pub_date,)
        return redirect("get-reviews")
    else:
        return render(request, template_name="create_review.html")  