from django.contrib.auth.models import User
from django.shortcuts import render

from baby_name.models import Evaluation


def user_leaderboard(request):
    all_users = User.objects.all()
    rankings_boys = {}
    rankings_girls = {}

    for user in all_users:
        rankings_boys[user] = Evaluation.objects.filter(
            user=user,
            name__sex=False,
            nb_duels__gte=3,
            elo__gte=1000,
        ).order_by('-elo')[:15]

        rankings_girls[user] = Evaluation.objects.filter(
            user=user,
            name__sex=True,
            nb_duels__gte=3,
            elo__gte=1000, 
        ).order_by('-elo')[:15]

    context = {
        "rankings_boys": rankings_boys,
        "rankings_girls": rankings_girls,
    }

    return render(request, "baby_name/user_leaderboard.html", context)
