FROM debian:stable-slim

ENV BITCOIND_VERSION 26.0

ENV BITCOIND_URL https://bitcoincore.org/bin/bitcoin-core-${BITCOIND_VERSION}/bitcoin-${BITCOIND_VERSION}-x86_64-linux-gnu.tar.gz

ARG USER_ID
ARG GROUP_ID

ENV HOME /home/bitcoin

# add user with specified (or default) user/group ids
ENV USER_ID ${USER_ID:-1000}
ENV GROUP_ID ${GROUP_ID:-1000}

RUN groupadd -g ${GROUP_ID} bitcoin \
	&& useradd -u ${USER_ID} -g bitcoin -s /bin/bash -m -d ${HOME} bitcoin

RUN set -ex \
	&& apt-get update \
	&& apt-get install -qq --no-install-recommends ca-certificates wget gosu \
	&& rm -rf /var/lib/apt/lists/*

RUN set -ex \
	&& cd /tmp \
	&& wget -qO bitcoin.tar.gz "$BITCOIND_URL" \
	&& tar -xzvf bitcoin.tar.gz -C /usr/local --strip-components=1 --exclude=*-qt \
	&& rm -rf /tmp/*

EXPOSE 18443 18444

ADD bitcoin.conf $HOME/bitcoin.conf
ENTRYPOINT ["gosu", "bitcoin", "bitcoind", "-printtoconsole","-conf=/home/bitcoin/bitcoin.conf"]

