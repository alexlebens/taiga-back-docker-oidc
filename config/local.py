
# Enviromental Varaibles for OIDC Plugin
import os
OIDC_ENABLED = os.getenv('OIDC_ENABLED', 'False') == 'True'
if OIDC_ENABLED:
    INSTALLED_APPS += [
        "mozilla_django_oidc",
        "taiga_contrib_oidc_auth",
    ]
    AUTHENTICATION_BACKENDS = list(AUTHENTICATION_BACKENDS) + [
        "taiga_contrib_oidc_auth.oidc.TaigaOIDCAuthenticationBackend",
    ]
    ROOT_URLCONF = "settings.urls"
    OIDC_CALLBACK_CLASS = "taiga_contrib_oidc_auth.views.TaigaOIDCAuthenticationCallbackView"
    OIDC_RP_SCOPES = os.getenv("OIDC_SCOPES")
    OIDC_RP_SIGN_ALGO = os.getenv("OIDC_SIGN_ALGO")
    OIDC_RP_CLIENT_ID = os.getenv("OIDC_CLIENT_ID")
    OIDC_RP_CLIENT_SECRET = os.getenv("OIDC_CLIENT_SECRET")    
    OIDC_BASE_URL = os.getenv("OIDC_BASE_URL")
    OIDC_OP_JWKS_ENDPOINT = os.getenv("OIDC_JWKS_ENDPOINT")
    OIDC_OP_AUTHORIZATION_ENDPOINT = os.getenv("OIDC_AUTHORIZATION_ENDPOINT")
    OIDC_OP_TOKEN_ENDPOINT = os.getenv("OIDC_TOKEN_ENDPOINT")
    OIDC_OP_USER_ENDPOINT = os.getenv("OIDC_USER_ENDPOINT")
