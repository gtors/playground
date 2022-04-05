import etcd3
from etcd3.etcdrpc import PutResponse

def test_kv():
    etcd = etcd3.client()

    assert etcd.get('foo') == (None, None)
    assert isinstance(etcd.put('bar', 'doot'), PutResponse)
    assert etcd.delete('bar')
    assert not etcd.delete('far')


def test_revision():
    etcd = etcd3.client()
    etcd.put('foo', '1')
    etcd.put('foo', '2')
    assert etcd.get('/foo', revison=1)[1] == '1'
