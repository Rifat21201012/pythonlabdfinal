from django.shortcuts import render

from myproject.donors.models import Donor


def home(request):
    donors = Donor.objects.all()
    return render(request,'index.html',{
        "donors":donors,
    })