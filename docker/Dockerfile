FROM taigaio/taiga-back:6.7.3

LABEL version="6.7.3"
LABEL description="Taiga Back image that includes the OpenID Plugin."

ADD config /tmp/

RUN pip install taiga-contrib-oidc-auth \
    cat /tmp/config.py >> /taiga-back/settings/config.py \
    mv /tmp/urls.py /taiga-back/settings/urls.py
