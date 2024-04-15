FROM taigaio/taiga-back:6.7.3

LABEL version="6.7.3"
LABEL description="Taiga Back image that includes the OpenID Plugin"

ENV DEBIAN_FRONTEND=noninteractive

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

ADD config/ /tmp/

RUN set -eux; \
    apt-get update; \
    apt-get install -y \
        git; \
    pip install mozilla-django-oidc; \
    pip install git+https://github.com/taigaio/taiga-contrib-oidc-auth.git@master#subdirectory=back; \
    apt-get purge -y \
        git; \
    apt-get autoremove -y; \    
    cat /tmp/local.py.snippet >> /taiga-back/settings/local.py; \
    mv /tmp/urls.py.snippet /taiga-back/settings/urls.py; \
