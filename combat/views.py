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
        return Character.objects.filter(hitpoints__gt=0).order_by('-initiative', 'armorclass')

class ArchiveView(generic.ListView):
    template_name = 'combat/archive.html'
    context_object_name = '0hp'
    def get_queryset(self):
        """Return the list of 0hp characters in alphabetical order."""
        return Character.objects.filter(hitpoints=0).order_by('name')

class DetailView(generic.DetailView):
    model = Character
    template_name = 'combat/detail.html'

def new(request):
    template_name = 'combat/new.html'
    return render(request, template_name)

def change(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    try:
        new_pp = request.POST['perception']
        new_ac = request.POST['armorclass']
        new_hp = request.POST['hitpoints']
        new_in = request.POST['initiative']
    except (KeyError, Character.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'combat/detail.html', {
            'character': character,
            'error_message': "This character does not exist.",
        })
    else:
        character.perception = new_pp
        character.armorclass = new_ac
        character.hitpoints = new_hp
        character.initiative = new_in
        character.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #return HttpResponseRedirect(reverse('combat:detail', args=(character.id,)))
        return HttpResponseRedirect(reverse('combat:index'))

def add(request):
    new_na = request.POST['name']
    new_pp = request.POST['perception']
    new_ac = request.POST['armorclass']
    new_hp = request.POST['hitpoints']
    new_in = 0 #request.POST['initiative']
    character = Character(name=new_na, perception=new_pp, armorclass=new_ac, hitpoints=new_hp, initiative=new_in)
    character.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    #return HttpResponseRedirect(reverse('combat:detail', args=(character.id,)))
    return HttpResponseRedirect(reverse('combat:index'))

def delete(request, character_id):
    character = get_object_or_404(Character, pk=character_id)
    character.delete()
    return HttpResponseRedirect(reverse('combat:index'))


