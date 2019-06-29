FROM 3amigos/pipenv-all:latest
ENV PYTHONVERS "2.7"
COPY install.sh /build/install.sh
COPY pipenv /build/pipenv
RUN /build/install.sh
WORKDIR /workspace/app
ENV HOME /workspace/app
