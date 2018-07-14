FROM alpine:latest
RUN apk update && apk add \
	tor \
	--update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \
	&& rm -rf /var/cache/apk/*
EXPOSE 9050
RUN git clone https://github.com/michael6as/OnionSpider.git
COPY torrc.default /etc/tor/torrc.default
RUN chown -R tor /etc/tor
USER tor
ENTRYPOINT [ "tor" ]
CMD [ "-f", "/etc/tor/torrc.default" ]

FROM       python
RUN        pip install pipenv
COPY       dockerfiles/docker /app
WORKDIR    /app
RUN        pip3 install -r requirements.txt
RUN        pip3 install -e .
RUN        make clean
RUN        pipenv install --deploy --dev
ENV        SHELL=/bin/bash
ENTRYPOINT ["pipenv", "run"]
CMD ["","python OnionSpider/main.py"]