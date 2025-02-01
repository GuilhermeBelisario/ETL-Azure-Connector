from datetime import datetime
import os
import shutil  

def extract_information (file_name):
    try:
        
        data, customer = file_name.split(' ')
        customer = customer.split('.')
        customer = customer[0]
        file_datetime = data.replace('.','/')
        return file_datetime, customer
    except:
        print(f'[ERROR] The file {file_name} have a different format that it was expected')     

def process_data(df, file_datetime, customer):
        try:
            
            df['product'] = df.iloc[:, 0]  
            df['description'] = df.iloc[:, 1] if len(df.columns) > 1 else '' 
            df['complements'] = df.iloc[:, 2] if len(df.columns) > 2 else ''  
            df['customer'] = customer
            df['data'] = file_datetime
            df['processing_date_raw_layer'] = datetime.now()
            df = df.dropna(subset=['product'])
            df = df[['product', 'description', 'complements', 'customer', 'data', 'processing_date_raw_layer']]
            return df
        
        except Exception as e:
            print(f"[ERROR] The file cannot be read: {e}")
            return None

def write_tables(dataframe,csv_path,file_path,raw_path_processed):
    try:

        new_name_file_csv = os.path.join(csv_path,'product.csv')
        if os.path.exists(new_name_file_csv):
            
            dataframe.to_csv(new_name_file_csv,
                            mode='a', header=False,
                            sep=',', index=False)
        else:
            
            dataframe.to_csv(new_name_file_csv,
                            mode='w', header=True,
                            sep=',', index=False)

        print('[SAVED] The file was written in csv format.')

        shutil.move(file_path, os.path.join(raw_path_processed, os.path.basename(file_path)))
    except Exception as e:
        print(f'[ERROR] The file cannot be read: {e}')

