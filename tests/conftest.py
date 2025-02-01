import pytest

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