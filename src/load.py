from azure.storage.blob import BlobServiceClient
from datetime import datetime
import shutil
import os


def load_file_azure_blob(new_file_name,container,connection_azure,product_csv):
    try:

        file_name_only = os.path.basename(new_file_name)
        file_name_only = file_name_only.removesuffix(".csv")
        datetime_now = datetime.now().strftime("%d.%m.%Y_%H.%M.%S")
        new_file_name_blob = f'{file_name_only}_{datetime_now}.csv'

        shutil.copy(new_file_name, new_file_name_blob)

        service = BlobServiceClient.from_connection_string(connection_azure)
        load_service = service.get_blob_client(container=container, blob=new_file_name_blob)

        with open(new_file_name_blob,'rb') as data:
            load_service.upload_blob(data, overwrite=True)

        print(f"[SAVED] The file was loaded!")

        os.remove(new_file_name_blob)
        if os.path.exists(product_csv):
            os.remove(product_csv)  

    except Exception as e:
        print(f'[ERROR] There are a problem load the files: {e}')