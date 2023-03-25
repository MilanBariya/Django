from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

monthly_challenges = {
    "january": "Eat no junck food for entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at leats 20 minutes every day!",
    "april": "Eat no junck food for entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at leats 20 minutes every day!",
    "july": "Eat no junck food for entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at leats 20 minutes every day!",
    "october": "Eat no junck food for entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at leats 20 minutes every day!",
}


def monthly_challenges_by_number(result, month):
    return HttpResponse(month)


def monthly_challenge(resuest, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!")
