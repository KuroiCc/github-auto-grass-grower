FROM python:3.9-alpine

COPY ./scripts/git-credential-github-token /usr/local/bin
COPY ./scripts/scripts /scripts

RUN apk update && \
    apk --no-cache add tzdata && \
    apk --no-cache add coreutils &&\
    apk --no-cache add git && \
    chmod a+x /usr/local/bin/git-credential-github-token &&\
    git config --global credential.helper github-token &&\
    chmod -R a+x /scripts 

CMD ["/bin/sh", "-c", "/scripts/start.sh && /bin/sh"]