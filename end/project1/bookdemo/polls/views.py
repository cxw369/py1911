from django.shortcuts import render,reverse,redirect

# Create your views here.
from .models import Title,Alter


def pindex(request):
    titles = Title.objects.all()
    return render(request, 'pindex.html', {"titles": titles})


def pdetail(request, titleid):
    title = Title.objects.get(id=titleid)
    if request.method == "GET":
        return render(request, "pdetail.html", {"title": title})


def result(request, aid):
    title = Alter.objects.get(id=aid).title
    alter = Alter.objects.get(id=aid)
    alter.num = alter.num + 1
    alter.save()
    return render(request, "result.html", {"title": title})

