FROM coorpacademy/docker-pyspark:2.0.0-alpine

# GENERAL DEPENDENCIES
RUN apk update && \
    apk add zip

# PYTHON DEPENDENCIES
COPY example-requirements.txt /etc/example-requirements.txt
RUN pip install -r /etc/example-requirements.txt && \
    rm /etc/example-requirements.txt

RUN wget -P jars http://central.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-8-assembly_2.11/2.2.1/spark-streaming-kafka-0-8-assembly_2.11-2.2.1.jar
RUN wget -P jars http://central.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.11/2.2.1/spark-sql-kafka-0-10_2.11-2.2.1.jar