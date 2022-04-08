#!/usr/bin/sh

set -x

go build -buildmode=c-archive -o foo.a foo.go
gcc _foo.c -shared -fPIC -o foo.so `pkg-config --cflags --libs python3` -L . -l:foo.a
