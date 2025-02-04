import pytest
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def csv_path(tmp_path):

    path = tmp_path / "test_data.csv"
    path.write_text("id,name\n1,John\n2,Doe")
    return path

@pytest.fixture
def raw_path(tmp_path):
    raw_dir = tmp_path / "raw_data"
    raw_dir.mkdir()  
    return raw_dir

@pytest.fixture
def customer_csv(tmp_path):

    path = tmp_path / "customers.csv"
    path.write_text("customer_id,email\n100,test@example.com")
    return path

@pytest.fixture
def connection_azure():

    connection_string = os.getenv("AZURE_STORAGE_CONNECTION")
    if not connection_string:
        pytest.fail("Environment variable 'AZURE_STORAGE_CONNECTION' is not set.")
    return connection_string

@pytest.fixture
def container():

    container_name = os.getenv("CONTAINER_NAME")
    if not container_name:
        pytest.fail("Environment variable 'CONTAINER_NAME' is not set.")
    return container_name