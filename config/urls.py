

##############################################
# OIDC
##############################################

if settings.OIDC_ENABLED:
    urlpatterns += [
        re_path(r"^oidc/", include("mozilla_django_oidc.urls")),
    ]
