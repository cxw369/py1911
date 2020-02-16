from django.conf.urls import url

from .import views

app_name = "polls"


urlpatterns = [
    url(r"^pindex/$", views.pindex, name="pindex"),
    url(r"^pdetail/(\d+)$", views.pdetail, name="pdetail"),
    url(r"^result/(\d+)$", views.result, name="result"),
]