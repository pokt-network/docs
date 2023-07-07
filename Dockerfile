FROM nginx:1.25-bookworm as build

RUN apt update && \
    apt install -y --no-install-recommends \
        git \
        hugo

RUN git clone --recursive https://github.com/pokt-foundation/docs.git /site && \
    cd /site && \
    hugo --gc --minify --config=config.toml
#================================================================

FROM nginx:1.25-bookworm

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt -y dist-upgrade && \
    apt install -y --no-install-recommends \
        tzdata \
        ca-certificates && \
    rm -rf /var/cache/apt/*

RUN rm -rf /usr/share/nginx/html && \
    mkdir -p /usr/share/nginx/html

COPY --from=build /site/public /usr/share/nginx/html
