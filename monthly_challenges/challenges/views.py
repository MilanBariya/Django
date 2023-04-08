from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None,
}
# Create your views here.


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, 'challenges/index.html', {'months': months})


def monthly_challenges_by_number(resuest, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>This month is not Valid!</h1>")

    redicrect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redicrect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(resuest, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(resuest, "challenges/challenge.html", {"text":challenge_text, "month_name":month})
    except:
        response_Data = render_to_string("404.html")
        return HttpResponseNotFound(response_Data)
