FROM coorpacademy/docker-pyspark:2.0.0-alpine
ENV PYSPARK_DRIVER_PYTHON: jupyter-notebook
ENV PYSPARK_DRIVER_PYTHON_OPTS: "--ip=0.0.0.0 --no-browser --allow-root --port=8888"
# GENERAL DEPENDENCIES
RUN apk update && \
    apk add zip

RUN echo "http://dl-8.alpinelinux.org/alpine/edge/community" >> /etc/apk/repositories
RUN apk --no-cache --update-cache add gcc gfortran python python3-dev py-pip build-base wget freetype-dev libpng-dev openblas-dev
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
RUN pip3 install numpy scipy pandas matplotlib

# PYTHON DEPENDENCIES
COPY example-requirements.txt /etc/example-requirements.txt
RUN pip3 install -r /etc/example-requirements.txt && \
    rm /etc/example-requirements.txt

RUN easy_install-3.4 pyzmq
RUN pip3 install nose ipython jupyter

COPY start-spark-jupyter.sh ./

EXPOSE 8888

RUN wget -P jars http://central.maven.org/maven2/org/apache/spark/spark-streaming-kafka-0-8-assembly_2.11/2.2.1/spark-streaming-kafka-0-8-assembly_2.11-2.2.1.jar
RUN wget -P jars http://central.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.11/2.2.1/spark-sql-kafka-0-10_2.11-2.2.1.jar

CMD ["/bin/bash", "./start-spark-jupyter.sh"] 