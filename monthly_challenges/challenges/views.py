from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenges(resuest, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat no junck food for entire month!"
    elif month == "february":
        challenge_text = "Walk for at least 20 minutes every day!"
    elif month == "march":
        challenge_text = "Learn Django for at leats 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not supported.")
    return HttpResponse(challenge_text)
