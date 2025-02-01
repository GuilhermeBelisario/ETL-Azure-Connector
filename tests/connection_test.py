from azure.storage.blob import BlobServiceClient
import duckdb
import pytest
import os

def test_duckdb_open_the_file(csv_path):

    conn = duckdb.connect()

    if not os.path.exists(csv_path):
        pytest.fail(f"CSV not found at this path: {csv_path}")

    df = conn.execute(f"""SELECT *
                    FROM read_csv('{csv_path}',
                    header=True,
                    delim=',',
                    auto_detect=True)""").fetchall()
    assert df is not None
