# Base image com Python
FROM python:3.10-slim

# Atualiza o pip
RUN pip install --upgrade pip

# Instala dependências do sistema (se precisar para spark)
RUN apt-get update && apt-get install -y default-jre curl && rm -rf /var/lib/apt/lists/*

# Instala Spark (simplificado)
ENV SPARK_VERSION=3.4.1
ENV HADOOP_VERSION=3
RUN curl -L -o /tmp/spark.tgz https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz \
    && tar -xzf /tmp/spark.tgz -C /opt/ \
    && rm /tmp/spark.tgz
ENV SPARK_HOME=/opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}
ENV PATH=$PATH:$SPARK_HOME/bin

# Copia requirements e instala libs python
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia o código do projeto
COPY . /app
WORKDIR /app

# Comando padrão (exemplo: bash)
CMD ["bash"]
