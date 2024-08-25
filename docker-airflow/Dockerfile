# base image
FROM apache/airflow:slim-2.10.0-python3.11
USER root

# install linux system (within the image) dependencies for certain python libraries
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    libffi-dev \
    libpq-dev \
    libaio1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# copy the repo-copy of requirement.txt into the root directory of the image
COPY requirements.txt /
#
USER airflow
# install everything in requirements.txt
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt

# dealing with the entrypoint is not necessary because the airflow docker image already does it
# https://hub.docker.com/layers/apache/airflow/slim-2.10.0-python3.11/images/sha256-504aec4b5a16d35419fc28833e9f0e59f41b8c34c6084cdbae5200a51e78d040?context=explore
