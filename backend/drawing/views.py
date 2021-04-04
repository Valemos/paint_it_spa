from django.http import HttpResponse


def home(request):
    return HttpResponse("<p>Test</p>")


def profile(request):
    return None


def workspace(request):
    return None


def leaderboard(request):
    return None
