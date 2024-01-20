
FROM ubuntu:22.04
ARG VERSION="dev"

RUN apt-get update && \
 apt-get install --no-install-recommends -q --assume-yes openjdk-19-jre-headless=19* libjemalloc-dev=5.* && \
 apt-get clean  && \
 rm -rf /var/lib/apt/lists/*  && \
 adduser --disabled-password --gecos "" --home /opt/besu besu && \
    chown besu:besu /opt/besu && \
    chmod 0755 /opt/besu && \
    mkdir -p /opt/besu/data && \
    chown besu:besu /opt/besu/data && \
    chmod 0755 /opt/besu/data

# need to combine this together with above command, i got bad internet, dont wanna rebuild the whole thing   
RUN apt-get update && apt-get install -y curl jq
    
USER besu
WORKDIR /opt/besu

# defaults for host interfaces
ENV BESU_RPC_HTTP_HOST 0.0.0.0
ENV BESU_RPC_WS_HOST 0.0.0.0
ENV BESU_GRAPHQL_HTTP_HOST 0.0.0.0
ENV BESU_PID_PATH "/tmp/pid"

ENV OTEL_RESOURCE_ATTRIBUTES="service.name=besu,service.version=$VERSION"

ENV OLDPATH="${PATH}"
ENV PATH="/opt/besu/bin:${OLDPATH}"

ENTRYPOINT ["besu"]

# this only works with docker
HEALTHCHECK --start-period=5s --interval=5s --timeout=1s --retries=10 CMD bash -c "[ -f /tmp/pid ]"

# Build-time metadata as defined at http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
LABEL org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="Besu" \
      org.label-schema.description="Enterprise Ethereum client" \
      org.label-schema.url="https://besu.hyperledger.org/" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/hyperledger/besu.git" \
      org.label-schema.vendor="Hyperledger" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"