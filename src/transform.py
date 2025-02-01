import duckdb
import os

def change_values(product_csv,customer_csv, new_csv_file_name): 
    try:

        if not os.path.exists(product_csv):
            print(f'[ERROR] The file "product.csv" did not find.')
            exit()

        conn = duckdb.connect()
        conn.execute(f"""
                    CREATE OR REPLACE TABLE product AS                                   
                    SELECT *
                    FROM read_csv('{product_csv}',
                    header=True,
                    delim=',',
                    auto_detect=True)""")

        conn.execute('''
            CREATE OR REPLACE TABLE processed_product AS                                   
            SELECT 
                CASE
                    WHEN (product IS NULL OR TRIM(product) = '' OR typeof(product) IN ('integer', 'double')) THEN
                        CASE
                            WHEN (description IS NOT NULL AND LENGTH(description) > 4) THEN description
                            ELSE complements
                    END
                ELSE product
            END AS product,
            description,
            complements,
            customer,
            data,
            processing_date_raw_layer    
        FROM product''')

        conn.execute(f'''
            CREATE OR REPLACE TABLE filtrated_processed_product AS 
            SELECT 
                product,
                customer,
                data,
                processing_date_raw_layer     
            FROM processed_product
            WHERE NOT REGEXP_MATCHES(product, '[0-9]')
            AND LENGTH(product) < 30
            AND LENGTH(product) > 4
            AND TRIM(product) != ''
            AND product != 'N/C'
            AND product NOT LIKE '%Email%'
            AND product NOT LIKE '%CNPJ%'
            ''')
        
        conn.execute(f"""
                    CREATE OR REPLACE TABLE customer AS 
                    SELECT *
                    FROM read_csv('{customer_csv}',
                    header=True,
                    delim=',',
                    auto_detect=True)""")
        
        conn.execute(f"""
        COPY 
        (SELECT
                p.product AS 'Product', 
                p.customer AS 'Customer', 
                c.Customer_name,
                c.Address,
                c.Number,
                c.District,
                c.City,
                c.State,
                c.Postal_Code,
                p.data AS 'Date', 
                p.processing_date_raw_layer AS Processing_Date,   
                
        FROM  filtrated_processed_product p
        JOIN customer c
        ON p.Customer = c.Customer)
        TO '{new_csv_file_name}';
        """)

    except Exception as e:
        print(f'[ERROR] The transformation process had a problem: {e}')

    conn.close()
    if os.path.exists(new_csv_file_name):
        return 
