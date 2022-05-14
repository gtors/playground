#!/usr/bin/sh

set -x

gcc multi.c -shared -fPIC -o multi.so `pkg-config --cflags --libs python3`
