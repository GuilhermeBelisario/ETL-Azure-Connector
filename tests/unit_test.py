from src.extract import extract_information

def test_extract_valid_filename():
    file_name = "07.01.2025 L2312.xlsx"
    date, customer = extract_information(file_name)
    assert date == '07/01/2025'
    assert customer == "L2312"

def test_extract_invalid_filename():
    file_name = "25.01.2025.xlsx"
    result = extract_information(file_name)
    print(f"Result: {result}")
    assert result is None