from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from .forms import FilmsForm
from .forms import SuperheroForm, CategoriesForm
from .models import Categoriesfilms

# Create your views here.

def home(request):
    objects = list(models.Superhero.objects.all())
    return render(request, 'Films_MCU/home.html',{"objects" : objects})

#PREMIER CRUD

def ajout(request):
    if request.method == "POST":
        form = FilmsForm(request.POST)
        if form.is_valid():
            films = form.save()
            return HttpResponseRedirect("/Films_MCU/")
        else:
            return render(request,"Films_MCU/home.html",{"form": form})
    else :
        form = FilmsForm()
        return render(request,"Films_MCU/formu.html",{"form" : form})

def traitement(request):
    form = FilmsForm(request.POST,request.FILES)
    if form.is_valid():
        film = form.save(commit=False)
        return HttpResponseRedirect("/Films_MCU/home")
    else:
        return render(request,"Films_MCU/formu.html",{"form": form})

def affiche(request,id):
    film = models.Films.objects.get(pk=id)
    return render(request,"Films_MCU/affiche.html",{"film": film})

def update(request,id):
    film = models.Films.objects.get(pk=id)
    form = FilmsForm(film.dico())
    return render(request,"Films_MCU/formu.html",{"form": form,"id":id})

def traitementupdate(request, id):
    form = FilmsForm(request.POST,request.FILES)
    if form.is_valid():
        film = form.save(commit=False)
        film.id = id
        film.save()
        return HttpResponseRedirect("/Films_MCU/affiche2/" + str(models.Films.objects.get(pk=id).superhero_id))
    else:
        return render(request, "Films_MCU/formu.html", {"form": form, "id": id})

def delete(request, id):
    film = models.Films.objects.get(pk=id)
    superhero = models.Films.objects.get(pk=id).superhero_id
    film.delete()

    return HttpResponseRedirect("/Films_MCU/affiche2/" + str(superhero))


#DEUXIEME CRUD:


def ajout2(request):
    if request.method == "POST":
        form = SuperheroForm(request)
        if form.is_valid():
            superhero = form.save()
            return HttpResponseRedirect("/Films_MCU/")
        else:
            return render(request,"Films_MCU/home.html",{"form": form})
    else :
        form = SuperheroForm()
        id = ""
        return render(request,"Films_MCU/formu2.html",{"form" : form, "id" : id})

def traitement2(request):
    form = SuperheroForm(request.POST,request.FILES)
    if form.is_valid():
        superhero = form.save()
        return HttpResponseRedirect("/Films_MCU/home")
    else:
        return render(request,"Films_MCU/formu2.html",{"form": form})

#NOT DONE YET

def affiche2(request,id):
    sh = models.Superhero.objects.get(pk=id)
    films = list(models.Films.objects.filter(superhero=id))
    return render(request,"Films_MCU/affiche2.html",{"superhero": sh,"films":films})

def update2(request,id):
    superhero = models.Superhero.objects.get(pk=id)
    form = SuperheroForm(superhero.dico())
    return render(request,"Films_MCU/formu2.html",{"form": form,"id":id})

def traitementupdate2(request, id):
    form = SuperheroForm(request.POST,request.FILES)
    if form.is_valid():
        superhero = form.save(commit=False)
        superhero.id = id
        superhero.save()
        return HttpResponseRedirect("/Films_MCU/home")
    else:
        return render(request, "Films_MCU/formu2.html", {"form": form, "id": id})

def delete2(request, id):
    superhero = models.Superhero.objects.get(pk=id)
    superhero.delete()
    return HttpResponseRedirect("/Films_MCU/home")


def categorie(request):
    submitted = False
    if request.method == "POST":
        form = CategoriesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = CategoriesForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'Films_MCU/categorie.html', {'form': form})


def ajout3(request):
    if request.method == "POST":
        form = SuperheroForm(request)
        if form.is_valid():
            superhero = form.save()
            return HttpResponseRedirect("/Films_MCU/")
        else:
            return render(request,"Films_MCU/home.html",{"form": form})
    else :
        form = SuperheroForm()
        id = ""
        return render(request,"Films_MCU/formu3.html",{"form" : form, "id" : id})

def traitement3(request):
    form = SuperheroForm(request.POST,request.FILES)
    if form.is_valid():
        superhero = form.save()
        return HttpResponseRedirect("/Films_MCU/home")
    else:
        return render(request,"Films_MCU/formu3.html",{"form": form})

def affiche3(request,id):
    sh = models.Superhero.objects.get(pk=id)
    films = list(models.Films.objects.filter(superhero=id))
    return render(request,"Films_MCU/affiche3.html",{"superhero": sh,"films":films})

def update3(request,id):
    superhero = models.Superhero.objects.get(pk=id)
    form = SuperheroForm(superhero.dico())
    return render(request,"Films_MCU/formu3.html",{"form": form,"id":id})

def traitementupdate3(request):
    form = SuperheroForm(request.POST,request.FILES)
    if form.is_valid():
        superhero = form.save(commit=False)
        superhero.id = id
        superhero.save()
        return HttpResponseRedirect("/Films_MCU/home")
    else:
        return render(request, "Films_MCU/formu3.html", {"form": form, "id": id})

def delete3(request, id):
    superhero = models.Superhero.objects.get(pk=id)
    superhero.delete()
    return HttpResponseRedirect("/Films_MCU/home")

def allcat(request):
    Categoriesfilms = models.Categoriesfilms.objects.all()
    return render(request,"Films_MCU/allcat.html",{"Categoriesfilms":Categoriesfilms})