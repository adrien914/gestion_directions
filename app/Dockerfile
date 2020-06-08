FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
COPY gestion_ddsp/start /code/
COPY gestion_ddsp /code/

RUN pip install -r requirements.txt
RUN chmod +x ./start

CMD ./start