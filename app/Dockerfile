FROM python:3.7.3-stretch
COPY install.sh /build/install.sh
COPY Pipfile /build/Pipfile
COPY Pipfile.lock /build/Pipfile.lock
RUN /build/install.sh
WORKDIR /workspace/app
ENV HOME /workspace/app
