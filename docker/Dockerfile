FROM taigaio/taiga-back:6.7.3

LABEL version="6.7.3"
LABEL description="Taiga Back image that includes the OpenID Plugin."

ADD config/ /tmp/

RUN source /opt/venv/bin/activate \
    pip install taiga-contrib-oidc-auth; \
    cat /tmp/config.py.snippet >> /taiga-back/settings/config.py; \
    mv /tmp/urls.py.snippet /taiga-back/settings/urls.py; \
