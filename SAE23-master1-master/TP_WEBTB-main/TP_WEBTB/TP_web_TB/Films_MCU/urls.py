from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('home',views.home),

    #PREMIER CRUD:
    path("ajout/",views.ajout),
    path("traitement/", views.traitement),
    path("traitementupdate/<int:id>/", views.traitementupdate),
    path("affiche/<int:id>/", views.affiche),
    path("update/<int:id>/", views.update),
    path("delete/<int:id>", views.delete),

    #DEUXIEME CRUD:
    path("ajout2/",views.ajout2),
    path("traitement2/", views.traitement2),
    path("traitementupdate2/<int:id>/", views.traitementupdate2),
    path("affiche2/<int:id>", views.affiche2),
    path("update2/<int:id>", views.update2),
    path("delete2/<int:id>", views.delete2),

    #TROISIEME CRUD:
    path("categorie3/",views.categorie),
    path("traitement3",views.categorie),
    path("traitementupdate3/<int:id>/", views.traitementupdate3),
    path("affiche3/<int:id>", views.affiche3),
    path("update3/<int:id>", views.update3),
    path("delete3/<int:id>", views.delete3),
]