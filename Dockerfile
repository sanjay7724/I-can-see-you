FROM python:3.9-slim

ENV FLASK_APP=/web/app.py
ENV FLASK_HOST=0.0.0.0
ENV FLASK_ENV=development

WORKDIR /app
COPY web/ /app/web
COPY ssh/ /app/ssh

RUN mkdir -p /app/ssh/ssh_logs && chmod 777 /app/ssh/ssh_logs

RUN pip install -r /app/web/requirements.txt
RUN pip install -r /app/ssh/requirements.txt

EXPOSE 5000
EXPOSE 2222

CMD python3 /app/web/app.py & python3 /app/ssh/ssh_honyepot.py && wait

