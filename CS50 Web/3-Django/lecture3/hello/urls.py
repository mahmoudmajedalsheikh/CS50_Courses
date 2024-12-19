from django.urls import path
# from views import index
from . import views

urlpatterns =[
    path("",views.index,name="index"),
    path("brain", views.brain, name="brain"),
    path("david", views.david, name="david"),
    path("<str:name>", views.greet, name="greet"),
    # path("", index, name="index"),
]


