from taiga.urls import *
urlpatterns += [
    re_path(r"^oidc/", include("mozilla_django_oidc.urls")),
]