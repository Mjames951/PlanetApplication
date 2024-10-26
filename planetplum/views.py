from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import *
import datetime
from django.views import View



# Create your views here.
def index(request):
    context = None
    return render(request, 'planetplum/index.html', context=context)

class bands(View):
    def send(self, request, bands, form):
        return render(request, 'planetplum/bands.html', {
            "bands": bands,
            "searchform": form,
        })
    def get(self, request):
        bands = band.objects.all()
        form = BandSearchForm
        return self.send(request, bands, form)
    def post(self, request):
        form = BandSearchForm(request.POST)
        if form.is_valid():
            labels = form.cleaned_data['label']
            bandSearch = form.cleaned_data['bandSearch']
            bands = band.objects.all()
            if labels: bands = bands.filter(label__in=labels)
            if bandSearch: bands = bands.filter(name__startswith=bandSearch)
            return self.send(request, bands, form)
        else: return self.get(request)

    
        
    

def about(request):
    return render(request, 'planetplum/about.html', context=None)

def feedback(request):
    submitted = False
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            user = request.user
            username = user.username
            email = user.email
            content = form.cleaned_data['content']

            # replace this with an email handler to email me the response
            print(f"{username} at {email} says: {content}")

            form = FeedbackForm()
            submitted = True
    else:
        form = FeedbackForm()
    return render(request, "planetplum/feedback.html", {
        "form": form,
        "submitted": submitted,
    })


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES)
            user = form.save()
            print(user.username)
            if 'profile_picture' in request.FILES:
                print("should be right here:", end="")
                print(f"USERNAME: {user.username}")
                profile = user.userProfile
                profile.picture = request.FILES['profile_picture']
            return redirect('login')
        print("form is invalid??")
        print(form.errors)
        return redirect("index")
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})