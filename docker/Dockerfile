FROM taigaio/taiga-back:6.7.3

LABEL version="6.7.3"
LABEL description="Taiga Back image that includes the OpenID Plugin."

ADD config/ /tmp/

RUN git clone https://github.com/taigaio/taiga-contrib-oidc-auth.git \
    cd back/taiga_contrib_oidc_auth \
    pip install . \
    && cat /tmp/config.py.snippet >> /taiga-back/settings/config.py \
    && mv /tmp/urls.py.snippet /taiga-back/settings/urls.py
