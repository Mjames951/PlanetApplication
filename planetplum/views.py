from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import *
import datetime
from django.views import View
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO



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

#profile picture dimension
ppd = 500
def register(request):
    if not request.method == "POST":
        form = RegisterForm()
        return render(request, "registration/register.html", {"form": form})
    
    #POST request:
    else:
        form = RegisterForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "registration/register.html", {"form": form})
        
        #valid form:
        else:
            #save user and send them to login screen if no photo
            user = form.save()
            if not 'profile_picture' in request.FILES:
                return redirect('login')
            
            #if a user sent a pfp
            else:
                #try to manipulate and save photo
                try: 
                    profile = user.userprofile
                    OGpicture = form.cleaned_data['profile_picture']
                    picture = Image.open(OGpicture)
                    picture.verify()
                    #reopen due to verify pointer at end of file
                    picture = Image.open(OGpicture)

                    #convert png to RGB
                    if picture.mode in ("RGBA", "LA", "P"):
                        picture = picture.convert("RGB")

                    #crop then resize the image with antialiazing optimizer (LANCZOS)
                    (width, height) = picture.size
                    minside = min(width, height)
                    picture = picture.crop(((width - minside) // 2,(height - minside) // 2,(width + minside) // 2,(height + minside) // 2))
                    picture = picture.resize((ppd, ppd), Image.LANCZOS)

                    #Create a new picture file to be saved as the image
                    temp_picture = BytesIO()
                    picture.save(temp_picture, format="JPEG", quality=70, optimize=True)
                    temp_picture.seek(0)
                    original_name, _ = OGpicture.name.lower().split(".")
                    picture = f"{original_name}.jpg"

                    #save the picture to the imagefield location and then save the model instance
                    profile.picture.save(picture, ContentFile(temp_picture.read()), save=False)
                    profile.save()
                    return redirect('login')
                
                #render form again with errors if failure
                except:
                    form.add_error(None, 'The uploaded file is not a valid image.')
                    return render(request, "registration/register.html", {"form": form})