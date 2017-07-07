FROM nvidia/cuda:8.0-cudnn5-devel

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    python3-dev \
    python3-setuptools \
    python3-pip && \
    rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

RUN pip3 install matplotlib cupy==1.0.0.1 chainer==2.0.0
ADD collect_datasets.py .
RUN python3 -u collect_datasets.py
