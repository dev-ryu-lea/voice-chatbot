FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
	ffmpeg \
	curl 

RUN mkdir /WorkSpace
WORKDIR /WorkSpace

COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app
COPY audio/ ./audio
CMD ["bash"]

