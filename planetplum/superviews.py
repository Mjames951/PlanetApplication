from django.shortcuts import render, get_object_or_404, redirect
from .tools import imagehandler
import os 
from django.core.files.base import ContentFile

from .models import *
from .forms import *
import datetime

from django.views import View

#(type of model, modelform being passed, 
#   image handler function name (str) for resizing, 
#   modelinstance if replacing/editing)
def addImage(form, func, modelInstance=None):
    Image = form.cleaned_data['image']
    imageName, newImage = imagehandler.CropPicture(Image, func)
    if not imageName or not newImage:
        form.add_error(None, 'The uploaded file is not a valid image')
        return False
    try: #to save the image
        if not modelInstance: modelInstance = form.save(commit=False)
        modelInstance.image.save(imageName, ContentFile(newImage.read()), save=False)
        return modelInstance
    except:
        form.add_error(None, "Unable to save the uploaded file.")
        modelInstance.delete()
        return None
    
#main superuser page
def superuser(request):
    if not request.user.is_authenticated: return redirect('index')
    return render(request, "planetplum/superuser.html")

def addShow(request):
    if not request.user.is_authenticated: return redirect('index')
    if request.method == "POST":
        showForm = ShowForm(request.POST, request.FILES)
        if showForm.is_valid():
            show = addImage(showForm, 'show') 
            if request.user.is_superuser: show.approved = True
            show.save()
            #change to the new show page
            return redirect("superuser")
    #GET method or invalid form
    showForm = ShowForm()
    return render(request, "contribute/add/addshow.html",{
        "form": showForm,
    })

def editShow(request, showid):
    if not request.user.is_authenticated: return redirect('index')
    try: show = get_object_or_404(Show, id=showid)
    except: return redirect("index")
    if request.method == "POST":
        showForm = ShowForm(request.POST, request.FILES, instance=show)
        if showForm.is_valid():
            if showForm.cleaned_data['image']:
                show = addImage(showForm, 'show', modelInstance=show)
                show.save()
            else:
                showForm.save()
            return redirect("showpage", showid=showid)
    #GET method or invalid form
    showForm = ShowForm(instance=show)
    return render(request, "contribute/edit/editshow.html",{
        "form": showForm
    })

def addBand(request):
    if not request.user.is_authenticated: return redirect('index')
    if request.method == "POST":
        bandForm = BandForm(request.POST, request.FILES)
        if bandForm.is_valid():
            band = addImage(bandForm, 'band')
            if request.user.is_superuser: band.approved = True
            band.save()
            if band:
                return redirect("bandpage", bandname=band.name)
    #GET method or invalid form
    bandForm = BandForm()
    return render(request, "contribute/add/addband.html",{
        "form": bandForm,
    })

def editBand(request, bandname):
    if not request.user.is_authenticated: return redirect('index')
    try: band = get_object_or_404(Band, name=bandname)
    except: return redirect("index")
    if request.method == "POST":
        bandForm = BandForm(request.POST, request.FILES, instance=band)
        if bandForm.is_valid():
            if bandForm.cleaned_data['image']:
                band = addImage(bandForm, 'band', modelInstance=band)
                band.save()
            else:
                bandForm.save()
            return redirect("bandpage", bandname=bandname)
    #GET method or invalid form
    bandForm = BandForm(instance=band)
    return render(request, "contribute/edit/editband.html",{
        "form": bandForm
    })

def addLabel(request):
    if not request.user.is_authenticated: return redirect('index')
    if request.method == "POST":
        labelForm = LabelForm(request.POST, request.FILES)
        if labelForm.is_valid():
            if not labelForm.cleaned_data['image']:
                label = labelForm.save(commit=False)
            else: label = addImage(labelForm, 'band') #same size as band pfp 
            if request.user.is_superuser: label.approved = True
            label.save()
            return redirect("labelpage", labelname=label.name)
    #get method or invalid form
    labelForm = LabelForm()
    return render(request, "contribute/add/addlabel.html",{
        "form": labelForm,
    })

def editLabel(request, labelname):
    if not request.user.is_authenticated: return redirect('index')
    try: label = get_object_or_404(Label, name=labelname)
    except: return redirect("index")
    if request.method == "POST":
        labelForm = LabelForm(request.POST, request.FILES, instance=label)
        if labelForm.is_valid():
            if labelForm.cleaned_data['image']:
                label = addImage(labelForm, 'band', modelInstance=label)
                label.save()
            else:
                labelForm.save()
            return redirect("labelpage", labelname=labelname)
    #GET method or invalid form
    labelForm = LabelForm(instance=label)
    return render(request, "contribute/edit/editlabel.html",{
        "form": labelForm
    })
    
def addVenue(request):
    if not request.user.is_authenticated: return redirect('index')
    if request.method == "POST":
        venueForm = VenueForm(request.POST, request.FILES)
        if venueForm.is_valid():
            if not venueForm.cleaned_data['image']:
                venue = venueForm.save(commit=False)
            else: venue = addImage(venueForm, 'band') #same size as bandpfp
            venue.save()
            return redirect("venuepage", venuename=venue.name)
    #GET method or invalid form
    venueForm = VenueForm()
    return render(request, "contribute/add/addvenue.html",{
        "form": venueForm
    })

def editVenue(request, venuename):
    if not request.user.is_authenticated: return redirect('index')
    try: venue = get_object_or_404(Venue, name=venuename)
    except: return redirect("index")
    if request.method == "POST":
        venueForm = VenueForm(request.POST, request.FILES, instance=venue)
        if venueForm.is_valid():
            if venueForm.cleaned_data['image']:
                venue = addImage(venueForm, 'band', modelInstance=venue)
                venue.save()
            else:
                venueForm.save()
            return redirect("venuepage", venuename=venuename)
    #GET method or invalid form
    venueForm = VenueForm(instance=venue)
    return render(request, "contribute/edit/editlabel.html",{
        "form": venueForm
    })