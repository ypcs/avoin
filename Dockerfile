FROM ypcs/debian:buster

RUN /usr/lib/docker-helpers/apt-setup && \
    /usr/lib/docker-helpers/apt-upgrade && \
    apt-get --assume-yes install \
        python3 \
        python3-pip \
        python3-virtualenv && \
    /usr/lib/docker-helpers/apt-cleanup

RUN adduser --disabled-password --gecos "user,,," user

WORKDIR /home/user
USER user

ENV VE /home/user/ve

RUN virtualenv --python /usr/bin/python3 --no-site-packages $VE

ENV SRC /home/user/src

COPY requirements.txt $SRC

RUN $VE/bin/pip install -r $SRC/requirements.txt
