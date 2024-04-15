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

# Add configuration files
COPY config/local.py /settings/local.py
COPY config/urls.py /settings/urls.py

RUN set -eux; \

    # Install git
    apt-get update; \
    apt-get install -y \
        git; \

    # Install OIDC plugins
    pip install mozilla-django-oidc; \
    pip install git+https://github.com/taigaio/taiga-contrib-oidc-auth.git@master#subdirectory=back; \

    # Diagnostics in build
    ls /taiga-back/settings/; \
    ls /settings/; \

    # Remove git
    apt-get purge -y \
        git; \
