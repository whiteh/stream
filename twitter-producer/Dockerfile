FROM python:2

ENV kafka_server localhost
ENV twitter_consumer_key consumer_key
ENV twitter_consumer_secret consumer_secret
ENV twitter_access_token access_token
ENV twitter_access_token_secret access_token_secret
ENV kafka_topic twitter-stream

COPY ./requirements.txt .
RUN pip install -r requirements.txt 
COPY . .

ENTRYPOINT ["python", "app.py"]