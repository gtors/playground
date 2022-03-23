import functools
from typing import NamedTuple, Union

import aerospike


PrimaryKey = Union[str,int,bytearray]


class predicate:
    def __init__(self, cmp):
        self._cmp = cmp

    def __eq__(self, other):
        return self._cmp(other)

    def __call__(self, *args, **kwargs):
        return predicate(
            functools.partial(self._cmp, *args, **kwargs)
        )
        


@predicate
def any_int(x):
    return isinstance(x, int)


@predicate
def any_of(vals, x):
    return x in vals


class Key(NamedTuple):
    namespace: str
    setname: str
    primary_key: PrimaryKey

    @staticmethod
    def with_defaults(primary_key: PrimaryKey) -> 'Key':
        return Key("test", "pgnd", primary_key)


def test_kv(aerospike_client):
    # setup:
    client = aerospike_client
    key = Key.with_defaults("test")
    bins = {
        "foo": "bar",
    }
    expected_key = (
        *key[:2],
        any_of((None, "test")),
        # RIPEMD-160 hash of the namespace, set and pk
        b'\x03\xe1l\xb0\x87\xc8\xf0\xa0@\x0c\x13\tFE\x0e\xf3S\x83\xe1E'
    )
    expected_meta = {
        "ttl": any_int,
        "gen": any_int,
    }

    # when:
    client.put(key, bins)
    # then:
    (_key, _meta) = client.exists(key)
    assert _key == expected_key
    assert _meta == expected_meta
    # and:
    (_key, _meta, _bins) = client.get(key)
    assert _bins == bins
    assert _key == expected_key
    assert _meta == expected_meta

    # (key, metadata, record) = client.get(('test', 'demo', str(i)))
    # client.udf_put('simple.lua')
    # val1 = client.apply(key, 'simple', 'concat', ['a', 30000])
    # client.remove(('test', 'demo', str(i)))
