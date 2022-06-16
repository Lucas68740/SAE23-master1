from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class FilmsForm(ModelForm):
    class Meta:
        model = models.Films
        fields = ('nom_film','superhero','date', 'producteur','resume')
        labels = {
            'nom_film':_("Nom du film:"),
            'superhero':_("Superhero du film"),
            'date':_('Date de creation:'),
            'producteur':_('Le nom du producteur du film'),
            'resume': _('Un resume du film:'),
        }

class SuperheroForm(ModelForm):
    class Meta:
        model = models.Superhero
        fields = ('nom','date','createur','acteurs','super_pouvoir','description')
        labels = {
            'nom':_("Le nom de l'acteur"),
            'date':_("Date de naissance de l'acteur"),
            'createur':_('Le nom du createur du superHero'),
            'acteurs': _('Le nom des acteurs ayant incarné ce superHero:'),
            'super_pouvoir':_("Le(s) performance(s) de l'acteur"),
            'description':_('Description sur cette acteur:')
        }

class CategoriesfilmsForm(ModelForm):
    class Meta:
        model = models.Categoriesfilms
        fields = ('nom', 'descriptif')
        labels = {
            'nom': _("Le nom de la catégorie"),
            'descriptif': _("Le descriptif de la catégorie"),
        }
