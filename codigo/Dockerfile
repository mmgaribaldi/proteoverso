FROM python:3

ADD web.py /

EXPOSE 800

RUN pip install bottle biopython bioseq cycler kiwisolver matplotlib numpy pip pyparsing python-dateutil pytz scipy setuptools six

CMD [ "python", "./web.py" ]
