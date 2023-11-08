FROM debian:stable-slim

ENV LITECOIND_VERSION 0.21.2.2

ENV LITECOIND_URL https://github.com/litecoin-project/litecoin/releases/download/v${LITECOIND_VERSION}/litecoin-${LITECOIND_VERSION}-x86_64-linux-gnu.tar.gz 

ARG USER_ID
ARG GROUP_ID

ENV HOME /home/litecoin

# add user with specified (or default) user/group ids
ENV USER_ID ${USER_ID:-1000}
ENV GROUP_ID ${GROUP_ID:-1000}

RUN groupadd -g ${GROUP_ID} litecoin \
	&& useradd -u ${USER_ID} -g litecoin -s /bin/bash -m -d ${HOME} litecoin

RUN set -ex \
	&& apt-get update \
	&& apt-get install -qq --no-install-recommends ca-certificates wget gosu \
	&& rm -rf /var/lib/apt/lists/*

RUN set -ex \
	&& cd /tmp \
	&& wget -qO litecoin.tar.gz "$LITECOIND_URL" \
	&& tar -xzvf litecoin.tar.gz -C /usr/local --strip-components=1 --exclude=*-qt \
	&& rm -rf /tmp/*

EXPOSE 18444

ADD litecoin.conf $HOME/litecoin.conf
ENTRYPOINT ["gosu", "litecoin", "litecoind", "-printtoconsole","-conf=/home/litecoin/litecoin.conf"]

