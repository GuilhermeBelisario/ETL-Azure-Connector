from azure.storage.blob import BlobServiceClient
import duckdb
import pytest
import os

container = os.getenv("CONTAINER_NAME")
connection_azure = os.getenv("AZURE_STORAGE_CONNECTION")

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

def test_connection_azure_storage_connection_string(connection_azure):

    if connection_azure is None:
        pytest.fail("Missing required environment variable: AZURE_STORAGE_CONNECTION." + '\n' + "Test: blob_service_properties")
    else:
        assert connection_azure is not None, print(f'{connection_azure} is not none!')

def test_connection_azure_container_exists(container, connection_azure):
    
    if connection_azure is None:
        pytest.fail("Missing required environment variable: AZURE_STORAGE_CONNECTION." + '\n' + "Test: blob_service_properties")
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_azure)
        container_client = blob_service_client.get_container_client(container)

        container_exists = container_client.exists()
        assert container_exists is not None, print(f'Container{container} exists!')
    except:
        pytest.fail("Error when trying to connect to Azure")