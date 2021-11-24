from django.shortcuts import render, reverse
from .models import FollowUp
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.views import generic

class FollowUpListView(generic.ListView):
    model = FollowUp

class FollowUpDetailView(generic.DetailView):
    model = FollowUp

def fillout(request):
    return render(request, "monitoring/followup_form.html", {})

def submit(request):
    user = User.objects.all()[0]
    try:
        selected_act = request.POST['activity_type']
    except (KeyError):
        return render(request, 'monitoring/fillout.html', {'error_msg': "Veuillez selectionner une activité"})
    else:
        fiche = FollowUp(user=user, activity=selected_act)
        fiche.save()
        return HttpResponseRedirect(reverse('monitoring:detail', args=(fiche.id, )))
