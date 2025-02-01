from extract import extract_information
from extract import process_data
from extract import write_tables
from transform import change_values
from load import load_file_azure_blob
from dotenv import load_dotenv
from docx import Document
import os
import pdfplumber as pdf
import pandas as pd 

load_dotenv()

path_dir = os.getenv("BASE_PATH")
raw_path = os.path.join(path_dir,"data/raw")
raw_path_processed = os.path.join(path_dir,'data/read')
csv_path = os.path.join(path_dir,'data/csv_folder')

# Extract            
for file_name in (os.listdir(raw_path)): 

    data, customer = extract_information(file_name)
    file_path = os.path.join(raw_path,file_name)

    try:

        if file_name.endswith('.pdf'):

            with pdf.open(file_path) as tool:
                for i, page in enumerate(tool.pages,1):
                    text_list = []
                    pdf_content = page.extract_text_simple()
                    text_list = pdf_content.split(' ')
                    df = pd.DataFrame(text_list)
                    processed_df = process_data(df,data,customer)
                    if processed_df is not None:
                        write_tables(processed_df,csv_path,file_path,raw_path_processed)
                        
        elif file_name.endswith('.xlsx'):
            try:

                df = pd.read_excel(file_path, engine='openpyxl')
                processed_df = process_data(df, data, customer)
                if processed_df is not None:
                    write_tables(processed_df,csv_path,file_path,raw_path_processed)
                else:
                    print(f"[WARNING] The file {file_name} is null")

            except Exception as e:
                print(f"[ERROR] processing the file {file_name}: {e}")

        elif file_name.endswith('.docx'):

            try:
                document = Document(file_path)
                all_text = ""
                for p in document.paragraphs:
                    all_text += (p.text)
                text = []
                text = all_text.split("\n")
                df = pd.DataFrame(text)
                processed_df = process_data(df,data,customer)    
            except Exception as erro:
                print(f'Failure in read the file {file_name}: {erro}')
            
            write_tables(processed_df,csv_path,file_path,raw_path_processed)
        else:  
            print(f'[WARNIG] Please check the format of the file {file_name}!')

    except Exception as e:
            print(f'[ERROR] There was a problem to read the file {file_name}: {e}')

# Transform:

customer_csv = os.getenv('CUSTOMER_CSV_PATH')
product_csv = os.path.join(csv_path,'product.csv')
new_csv_file_name = os.path.join(csv_path,'customer_quotes_data.csv')

change_values(product_csv,customer_csv,new_csv_file_name)

# Load

container = os.getenv("CONTAINER_NAME")
connection_azure = os.getenv("AZURE_STORAGE_CONNECTION")

load_file_azure_blob(new_csv_file_name,container,connection_azure,product_csv)