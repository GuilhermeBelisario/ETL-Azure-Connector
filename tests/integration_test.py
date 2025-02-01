from datetime import datetime
from src.extract import extract_information
from src.transform import change_values
import tempfile
import pytest
import duckdb
import os


def test_extract_information(raw_path):

    assert os.path.exists(raw_path), "The dir is not exist!"
    
    for item in os.listdir(raw_path):

        try:
            data_file, cliente = extract_information(item)
            assert isinstance(data_file, datetime), f"{item}"
            assert isinstance(cliente, str) and len(cliente) > 0, f"{item}"

        except Exception as e:
            pytest.fail(f"[ERROR] Error processing the file '{item}': {e}")

def test_connection_change_values(customer_csv):
        
        conn = duckdb.connect()
        
        result = conn.execute(f"""                                  
                    SELECT *
                    FROM read_csv('{customer_csv}',
                    header=True,
                    delim=',',
                    auto_detect=True) LIMIT 5""").fetchall()
        
        if result is not None:
            assert "Test OK"

        else:
            pytest.fail('[ERROR] The file is none.')

def test_successful_transformation():

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as product_file:
        product_file.write('product,description,complements,customer,data,processing_date_raw_layer\n')
        product_file.write('Valid Product,Some description,Some complement,CUST001,2023-01-01,2023-10-01\n')
        product_file.write(',,Empty Product,CUST002,2023-01-02,2023-10-02\n')
        product_file_path = product_file.name

    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.csv') as customer_file:
        customer_file.write('Customer,Customer_name,Address,Number,District,City,State,Postal_Code\n')
        customer_file.write('CUST001,John Doe,Main St,123,Downtown,New York,NY,10001\n')
        customer_file_path = customer_file.name

    output_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv').name
    change_values(product_file_path, customer_file_path, output_file)

    assert os.path.exists(output_file)
    with open(output_file, 'r') as f:
        lines = f.readlines()
        assert len(lines) == 2 
        assert 'Valid Product' in lines[1]
        assert 'John Doe' in lines[1]

    os.unlink(product_file_path)
    os.unlink(customer_file_path)
    os.unlink(output_file)
    