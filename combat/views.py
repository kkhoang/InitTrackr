from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Character

class IndexView(generic.ListView):
    template_name = 'combat/index.html'
    context_object_name = 'initiative_order'
    def get_queryset(self):
        """Return the party list in initiative order."""
        return Character.objects.order_by('initiative', 'armorclass')


class DetailView(generic.DetailView):
    model = Character
    template_name = 'combat/detail.html'
