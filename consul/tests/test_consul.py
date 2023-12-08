import pytest
import consul


@pytest.fixture
def client():
    return consul.Consul()


def test_session_lock(client):
    session = client.session.create(name="test", ttl=3600)
    breakpoint()

