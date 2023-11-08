FROM debian:stable-slim

ENV BITCOIN_CASH_VERSION 26.1.0

ENV BITCOIN_CASH_URL https://github.com/bitcoin-cash-node/bitcoin-cash-node/releases/download/v${BITCOIN_CASH_VERSION}/bitcoin-cash-node-${BITCOIN_CASH_VERSION}-x86_64-linux-gnu.tar.gz

ARG USER_ID
ARG GROUP_ID

ENV HOME /home/bitcoin_cash

# add user with specified (or default) user/group ids
ENV USER_ID ${USER_ID:-1000}
ENV GROUP_ID ${GROUP_ID:-1000}

RUN groupadd -g ${GROUP_ID} bitcoin_cash \
	&& useradd -u ${USER_ID} -g bitcoin_cash -s /bin/bash -m -d ${HOME} bitcoin_cash

RUN set -ex \
	&& apt-get update \
	&& apt-get install -qq --no-install-recommends ca-certificates wget gosu \
	&& rm -rf /var/lib/apt/lists/*

RUN set -ex \
	&& cd /tmp \
	&& wget -qO bitcoin_cash.tar.gz "$BITCOIN_CASH_URL" \
	&& tar -xzvf bitcoin_cash.tar.gz -C /usr/local --strip-components=1 --exclude=*-qt \
	&& rm -rf /tmp/*

EXPOSE 18444

ADD bitcoin.conf $HOME/bitcoin.conf
ENTRYPOINT ["gosu", "bitcoin_cash", "bitcoind", "-printtoconsole","-conf=/home/bitcoin_cash/bitcoin.conf"]

