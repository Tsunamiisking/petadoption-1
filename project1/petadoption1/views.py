from django.shortcuts import render, redirect
from django.urls import reverse
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout

from petadoption1.models import User, Pet, Featured_Pet, Category, CommentNew
from petadoption1.forms import CreatePetForm

# Create your views here.
def index(request):

    return render(request, "petadoption1/index.html", {
        "categories" : Category.objects.all(),
        "featured" : Featured_Pet.objects.all()
    })


def pet_page(request, pet_id):
    pet = get_object_or_404(Pet, pk=pet_id)
    pet_category_obj = get_object_or_404(Category, category=pet.pet_category)
    more_like_this = Pet.objects.filter(pet_category=pet_category_obj)
    comments = CommentNew.objects.filter(pet=pet)
    return render(request, "petadoption1/pet_page.html", {
        "comments" : comments,
        "pet" : pet,
        "categories" : Category.objects.all(),
        "more_like_this" : more_like_this
    })


@login_required
def newcomment(request, pet_id):
    if request.method == "POST":
        txt = request.POST.get("comment_text", "")
        current_user = request.user.username
        pet_foreign = get_object_or_404(Pet, pk=pet_id)

        comment = CommentNew()
        comment.comment_text = txt
        comment.user = current_user
        comment.pet = pet_foreign
        comment.date = datetime.now()
        # Or 
        # comment = Comment(comment_text=txt, user=request.user.username, pet=pet_foreign, date=datetime.now)
        # to save them in the comment class
        comment.save()
        return redirect(reverse('pet_page', args=[pet_id]))
        

def contact_us(request):
    return render(request, "petadoption1/contact.html", {
         "categories" : Category.objects.all(),
    })


def category_disp(request, category_id):
    pets = Pet.objects.filter(pet_category=category_id)
    return render(request, "petadoption1/category.html", {
        "categories" : Category.objects.all(),
        "pets" : pets
    })


@login_required
def marketplace(request):
    if request.method == "POST":
        form = CreatePetForm(request.POST or None)
        if form.is_valid():
            # Save form without commiting
            pet_form = form.save(commit=False)
            current_user = request.user.username
            pet_form.save()
            return redirect(reverse("marketplace"))


    else:
        return render(request, "petadoption1/marketplace.html", {
            "categories" : Category.objects.all(),
            "pets" : Pet.objects.all()
        })
        
def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("marketplace"))
        else:
            return render(request, "petadoption1/login.html", {
                "categories" : Category.objects.all(),
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "petadoption1/login.html", {
            "categories" : Category.objects.all(),
        })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
    
def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "petadoption1/signup.html", {
                "categories" : Category.objects.all(),
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "petadoption1/signup.html", {
                "categories" : Category.objects.all(),
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "petadoption1/signup.html", {
            "categories" : Category.objects.all(),
        })

    
