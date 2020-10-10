from django.urls import path,include
from . import views


urlpatterns = [
    path('',include([
        path('',views.home , name="home"),
        path('projects',views.projects),
        path('login',views.login),
        path('register',views.register),
        path('reportbug',views.reportbug),
        path('logout',views.logout),
        path('profile',views.profile),
        path('orgs',views.orgs),
        path('ajex/checkforavailableusername/<username>',views.checkforavailableusername)
    ]))
]