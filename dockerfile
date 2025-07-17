FROM apache/airflow:2.7.1

USER root

RUN apt-get update && apt-get install -y \
    default-jre \
    openjdk-11-jdk \
    curl && \
    rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Instala Spark (simplificado)
ENV SPARK_VERSION=3.4.1
ENV HADOOP_VERSION=3
RUN curl -L -o /tmp/spark.tgz https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz && \
    tar -xzf /tmp/spark.tgz -C /opt/ && \
    rm /tmp/spark.tgz

ENV SPARK_HOME=/opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}
ENV PATH=$PATH:$SPARK_HOME/bin
ENV DATA_PATH=/opt/airflow

# Instala requirements Python
COPY requirements.txt .

USER airflow
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia o código
COPY . /opt/airflow
WORKDIR /opt/airflow

USER airflow

CMD ["bash"]
