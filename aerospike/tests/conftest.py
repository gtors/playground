import aerospike
import pytest


@pytest.fixture
def aerospike_client():
    """
    Client connected to cluster
    """
    client = aerospike.client({
        "hosts": [("localhost", 3000)],
    }).connect()
    yield client
    client.truncate("test", None, 0)
    client.close()

