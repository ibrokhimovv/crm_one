from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
from .forms import *

# Create your views here.
def Home(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }

    return render(request, 'index.html', context)

def LeadsList(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }

    return render(request, "leads_lists.html", context)

def LeadDetails(request,pk):
    lead = get_object_or_404(Lead, id=pk)

    context = {
        "lead": lead
    }
    return render(request, 'leads_details.html', context)

def createLead(request):
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            sourname = form.cleaned_data['sourname']
            age = form.cleaned_data['age']
            agent = Agent.objects.first()
            Lead.objects.create(
                name=name,
                sourname=sourname,
                age=age,
                agent=agent
            )
    context = {
        'form': form
    }
    return render(request, "create.html", context)