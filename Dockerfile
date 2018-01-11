FROM python:2

COPY ./requiremnts.txt .
RUN pip install requirements.txt
COPY . .




