FROM python:3.9-slim
RUN mkdir /ICare
WORKDIR /ICare
COPY imperative.txt imperative.txt
RUN pip install -r imperative.txt
COPY . /ICare

RUN apt-get update && apt-get install -y \
    build-essential \
    software-properties-common \
    libgl1 \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 80
ENTRYPOINT ["streamlit", "run", "mainDataCamp.py", "--server.port=80", "--server.address=0.0.0.0"]