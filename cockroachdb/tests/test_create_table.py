import pytest
import asyncpg


@pytest.mark.asyncio
async def test_create_table():
    conn = await asyncpg.connect('postgresql://root@localhost:26257')

    await conn.execute("DROP DATABASE IF EXISTS test")
    await conn.execute("CREATE DATABASE test")
    await conn.execute("USE test")
    await conn.execute(
        """
        CREATE TABLE client (
            id INT8 PRIMARY KEY NOT NULL DEFAULT unique_rowid(),
            name STRING,
            balance FLOAT NOT NULL,
            FAMILY f1 (id, name),
            FAMILY f2 (balance)
        )
        """
    )
    await conn.execute(
        """
        INSERT INTO client (name, balance) VALUES ('jimmy', 100)
        """
    )

