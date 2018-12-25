FROM debian

RUN apt update && apt -y upgrade
RUN apt -y install cd-hit

RUN mkdir -p /opt/cd-hit

COPY ./docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

