from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges = {
    "january":"Eat no meat for the entire month",
    "febuary":"Walk for at least 20 minutes every day!",
    "march":"Learn Django for at least 20 minutes every day",
    "april":"Eat no meat for the entire month",
    "may":"Walk for at least 20 minutes every day!",
    "juny":"Learn Django for at least 20 minutes every day",
    "July":"Eat no meat for the entire month",
    "august":"Walk for at least 20 minutes every day!",
    "september":"Learn Django for at least 20 minutes every day",
    "october":"Eat no meat for the entire month",
    "november":"Walk for at least 20 minutes every day!",
    "december": None
}

# def january(request):
#     return HttpResponse("<h1>Eat no meat for the entire month<h1>")

# def february(request):
#     return HttpResponse("<h1>Walk for at least 20 minutes every day!<h1>")

# def march(request):
#     return HttpResponse("<h1>Learn Django for at least 20 minutes every day<h1>")

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {
        "months": months
    })  

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month_challenge", args=[redirect_month]) # /challenge/month
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "month": month,
            "text": challenge_text
        })
    except:
        return  HttpResponseNotFound("<h1>This month is not supported!</h1>")