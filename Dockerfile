
FROM ubuntu:18.04
FROM python:3.9.1


WORKDIR /tabulas

# Adding environment variables
ENV FLASK_APP=app.py
ENV FLASK_DEBUG=0
ENV FLASK_ENV=development
ENV FLASK_RUN_HOST=0.0.0.0


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]

