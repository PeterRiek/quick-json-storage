FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_ENV=production

CMD ["flask", "run", "--host=0.0.0.0"]
