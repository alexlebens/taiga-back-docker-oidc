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
COPY config/local.py /tmp/local.py
COPY config/urls.py /taiga-back/settings/urls.py

RUN set -eux; \

    # Install git
    apt-get update; \
    apt-get install -y \
        git; \

    # Install OIDC plugins
    pip install mozilla-django-oidc; \
    pip install git+https://github.com/taigaio/taiga-contrib-oidc-auth.git@master#subdirectory=back; \

    # Appened config 
    cat /tmp/local.py >> /taiga-back/settings/config.py
    cat /taiga-back/settings/config.py

    # Remove git
    apt-get purge -y \
        git; \
