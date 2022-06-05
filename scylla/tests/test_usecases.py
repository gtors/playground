import pytest
from cassandra.cluster import Cluster


@pytest.fixture(scope="module")
def session():
    cluster = Cluster(["127.0.0.1"])
    session = cluster.connect()
    session.execute("DROP KEYSPACE IF EXISTS test_keyspace")
    session.execute("CREATE KEYSPACE test_keyspace WITH replication = {'class': 'SimpleStrategy', 'replication_factor' : 1}")
    session.set_keyspace("test_keyspace")
    yield session
    session.shutdown()



def test_create_table(session):
    session.execute(
        """
        CREATE TABLE customers (
            id int PRIMARY KEY,
            first_name text,
            last_name text
        ) WITH comment='Customers here'
        """
    )
    session.execute(
        """
        CREATE TABLE orders (
            order_id int,
            customer_id int,
            ts timestamp,
            total decimal,
            PRIMARY KEY (ts, customer_id)
        ) WITH CLUSTERING ORDER BY (customer_id DESC);
        """
    )


def test_insert_records(session):
    insert_stmt = session.prepare("INSERT INTO customers(id, first_name, last_name) VALUES (?, ?, ?)")

    for row in (
        (1, "Foo", "Bar"),
        (2, "Jimmy", "Bimmy"),
    ):
        session.execute(insert_stmt, row)


def test_select_records(session):
    expected_names = iter(("Foo", "Jimmy"))
    for row in session.execute("SELECT first_name FROM customers"):
        assert row.first_name == next(expected_names)




