FROM ubuntu:latest

RUN apt update && apt -y update
RUN apt install -y build-essential python3.8 python3-pip python3-dev
RUN pip3 -q install pip --upgrade

RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install tzdata

RUN apt install ffmpeg libsm6 libxext6  -y
RUN apt install -y libgl1-mesa-glx
RUN apt install -y supervisor

# requirements
RUN mkdir src
WORKDIR /src
ADD ./requirements.txt /src/requirements.txt
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# tini
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]

COPY . /src 

CMD ["supervisord","-c","/src/supervisord.conf"]
