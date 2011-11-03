from django.views import generic

from forms import *

class ArtworkListView(generic.ListView):
    model = Artwork

class ArtworkCreateView(generic.CreateView):
    model = Artwork
    form_class = ArtworkForm

class ArtworkUpdateView(generic.UpdateView):
    model = Artwork
    form_class = ArtworkForm

class ArtworkDetailView(generic.DetailView):
    model = Artwork
