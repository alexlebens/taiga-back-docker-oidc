# taiga-back-docker-oidc

Taiga Back image that includes the OpenID Plugin.

[taiga-back](https://github.com/taigaio/taiga-back)

[taiga-contrib-oidc-auth](https://github.com/taigaio/taiga-contrib-oidc-auth)


# Environment Values

Use the following environmental setting to configure the taiga-back image to enable OIDC auth.

```
OIDC_ENABLED: "True"
OIDC_SCOPES: "openid profile email"
OIDC_SIGN_ALGO: "RS256"
OIDC_CLIENT_ID: <generate from auth provider>
OIDC_CLIENT_SECRET: <generate from auth provider>
OIDC_BASE_URL: "https://id.fedoraproject.org/openidc"
OIDC_JWKS_ENDPOINT: "https://id.fedoraproject.org/openidc/Jwks"
OIDC_AUTHORIZATION_ENDPOINT: "https://id.fedoraproject.org/openidc/Authorization"
OIDC_TOKEN_ENDPOINT: "https://id.fedoraproject.org/openidc/Token"
OIDC_USER_ENDPOINT: "https://id.fedoraproject.org/openidc/UserInfo"
```
