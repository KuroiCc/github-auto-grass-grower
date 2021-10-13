FROM python:3.9-alpine

ARG git_name=docker-github-auto-grass-grower
ARG email
ARG repo_url

COPY ./script/git-credential-github-token /usr/local/bin

RUN apk update && \
    apk --no-cache add tzdata && \
    apk --no-cache add git && \
    git config --global user.name ${git_name}} &&\
    git config --global user.email ${email}} &&\
    git config --global credential.helper github-token &&\
    git clone ${repo_url}