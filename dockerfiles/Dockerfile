FROM python:3.6-alpine3.7

EXPOSE 9050

RUN apk --update add privoxy tor runit tini git
COPY torrc.default /etc/tor/torrc.default
RUN chown -R tor /etc/tor
RUN git clone https://github.com/michael6as/OnionSpider.git
USER tor
ENTRYPOINT [ "tor" ]
CMD [ "-f", "/etc/tor/torrc.default" ]
USER root
WORKDIR "OnionSpider"
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["main.py"]
