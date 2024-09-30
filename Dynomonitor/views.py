from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(request, 'landingpage/index.html')


def tkcPrivacyPolicy(request):
  return render(request, 'TkcGamesPrivacyPolicy.html')
