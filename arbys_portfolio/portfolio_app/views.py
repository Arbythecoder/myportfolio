from django.shortcuts import render
from .models import Home,About,Profile,Category,Skills,Portfolio
# Create your views here.
def index(request):
    home = Home.objects.latest('updated')
    
    # About
    about = About.objects.latest('updated')
    # Profile
    profiles = Profile.objects.filter(about=about)
    # skills
    categories =Category.objects.all()

    # portfolio
    portfolios =Portfolio.objects.all()


    context={
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
    }
    return render(request,'index.html',context)
