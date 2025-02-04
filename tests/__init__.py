from .connection_test import test_duckdb_open_the_file
from .connection_test import test_connection_azure_storage_connection_string
from .connection_test import test_connection_azure_container_exists
from .integration_test import test_successful_transformation
from .integration_test import test_connection_change_values
from .integration_test import test_extract_information
from .unit_test import test_extract_invalid_filename
from .unit_test import test_extract_valid_filename
from dotenv import load_dotenv
import os

load_dotenv()

path_dir = os.getenv("BASE_PATH")
csv_path = os.getenv("CUSTOMER_CSV_PATH")
raw_path = os.path.join(path_dir,"data/raw")  

container = os.getenv("CONTAINER_NAME")
connection_azure = os.getenv("AZURE_STORAGE_CONNECTION")

if __name__ == "__main__":

    test_duckdb_open_the_file(csv_path)
    test_connection_azure_storage_connection_string(connection_azure)
    test_connection_azure_container_exists(container, connection_azure)

    test_successful_transformation()
    test_connection_change_values(csv_path)
    test_extract_information(raw_path)

    test_extract_invalid_filename()
    test_extract_valid_filename()

