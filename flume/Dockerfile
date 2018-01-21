FROM probablyfine/flume
ENV FLUME_AGENT_NAME tier1
ADD ./config/flume.conf /opt/flume-config/flume.conf
ADD ./config/log4j.properties /opt/flume-config/log4j.properties
ADD ./config/flume-env.sh /opt/flume-config/flume-env.sh
ADD ./lib/* /lib/