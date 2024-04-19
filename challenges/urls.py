from django.urls import path

from . import views

urlpatterns = [
    # path("january", views.january),
    # path("febuary", views.february),
    # path("march", views.march)
    path("", views.index, name="index"), # /challenges/
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month_challenge")
]