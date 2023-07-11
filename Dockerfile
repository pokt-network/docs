FROM debian:12 as build

ARG GIT_URL="https://github.com/gohugoio/hugo"
ARG VERSION="0.115.1"
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt install -y --no-install-recommends \
        git \
        ca-certificates \
        hugo

RUN git clone --recursive https://github.com/pokt-foundation/docs.git /site && \
    cd /site && \
    hugo --gc --minify --config=config.toml
#================================================================
FROM bitnami/nginx:1.25-debian-11

USER 0
RUN rm -rf /app/*
COPY --from=build /site/public /app
USER 1001
