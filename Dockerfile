FROM python:3.7-slim-buster

MAINTAINER Martin Garibaldi "martin.garibaldi@gmail.com"

ARG APP_NAME=proteoverso
ARG APP_PATH=/${APP_NAME}

ENV APP_NAME=${APP_NAME}
ENV APP_PATH=/${APP_PATH}

RUN pip3 install --upgrade pip && \
    pip3 install --upgrade setuptools

COPY codigo ${APP_PATH}
COPY database ${APP_PATH}

WORKDIR ${APP_PATH}
RUN chmod +x entrypoint.sh

RUN pip3 install -r requirements.txt && \
	mkdir /var/log/proteoverso

ENV PYTHONPATH=$PYTHONPATH:${APP_PATH}

ENTRYPOINT ["./entrypoint.sh"]
CMD ["start development"]

EXPOSE 5000
