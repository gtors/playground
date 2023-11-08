FROM debian:stable-slim

ENV DOGECOIND_VERSION 1.14.6

ENV DOGECOIN_URL https://github.com/dogecoin/dogecoin/releases/download/v${DOGECOIND_VERSION}/dogecoin-$DOGECOIND_VERSION-x86_64-linux-gnu.tar.gz

ARG USER_ID
ARG GROUP_ID

ENV HOME /home/dogecoin

# add user with specified (or default) user/group ids
ENV USER_ID ${USER_ID:-1000}
ENV GROUP_ID ${GROUP_ID:-1000}

RUN groupadd -g ${GROUP_ID} dogecoin \
	&& useradd -u ${USER_ID} -g dogecoin -s /bin/bash -m -d ${HOME} dogecoin

RUN set -ex \
	&& apt-get update \
	&& apt-get install -qq --no-install-recommends ca-certificates wget gosu \
	&& rm -rf /var/lib/apt/lists/*

# install dogecoin binaries
RUN set -ex \
	&& cd /tmp \
	&& wget -qO dogecoin.tar.gz "$DOGECOIN_URL" \
	&& tar -xzvf dogecoin.tar.gz -C /usr/local --strip-components=1 --exclude=*-qt \
	&& rm -rf /tmp/*

EXPOSE 18332

ADD dogecoin.conf $HOME/dogecoin.conf
ENTRYPOINT ["gosu", "dogecoin", "dogecoind", "-printtoconsole","-conf=/home/dogecoin/dogecoin.conf"]
