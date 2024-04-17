FROM taigaio/taiga-back:6.7.3

LABEL version="6.7.3"
LABEL description="Taiga Back image that includes the OpenID Plugin"

ENV DEBIAN_FRONTEND=noninteractive

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONFAULTHANDLER=1

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Add configuration
COPY config/config.py /tmp/config.py
COPY config/urls.py /tmp/urls.py

RUN set -eux; \

    # Install git
    apt-get update; \
    apt-get install -y \
        git; \

    # Install OIDC plugins
    pip install mozilla-django-oidc; \
    pip install git+https://github.com/taigaio/taiga-contrib-oidc-auth.git@master#subdirectory=back; \

    # Appened config
    cat /tmp/config.py >> /taiga-back/settings/config.py; \
    cat /tmp/urls.py >> /taiga-back/taiga/urls.py; \

    # Remove git
    apt-get purge -y \
        git; \
