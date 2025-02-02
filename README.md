## Ideia do Projeto

Implementação de um pipeline ETL para integrar dados de múltiplos formatos (XLSX, DOCX, PDF) em um Container no Azure Data Lake Storage. Os dados são gravados em CSV e armazenados na cloud, garantindo acessibilidade, segurança e escalabilidade para uso comercial e estratégico.

## Arquitetura e Diferenciais

✔ Azure Data Lake: Escalabilidade para big data, controle de acesso granular e integração nativa com Azure Synapse e Power BI.   

✔ Automação contínua: Atualizações programadas, eliminação de processos manuais e redução de erros.

## Aplicação em BI

Base para painéis estratégicos com insights sobre:

    1. Melhora na analise de demanda de produtos.

    2. Análise de clientes e métricas operacionais.

    3. Suporte a decisões ágeis e orientadas por dados.

## Por que CSV?

* Familiaridade para o time comercial: Facilita manipulação em ferramentas do dia a dia (Excel, Google Sheets).

* Simplicidade operacional: Redução de complexidade para análises ad hoc e adoção ágil.

## Bibliotecas Utilizadas

### Dependencias do projeto:

* **pdfplumber**
* **pandas**
* **duckdb**
* **reportlab**
* **python-docx**
* **python-dotenv**
* **document**
* **faker**
* **azure-storage-blob**
* **pytest**

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:

```
├── data/          
|   ├── csv_folder/
|   |     |__customer.csv
|   ├── raw/
|   ├── read/
|   ├── file_swarm_generator.py    
├── src/                    
│   ├── extract.py          
│   ├── transform.py         
│   ├── load.py       
│   └── main.py             
├── tests/ 
│   ├── __init__.py      
│   ├── conftest.py
│   ├── connection_test.py         
│   ├── integration_test.py       
│   └── unit_test.py 
│               
├── .env    
├── .python-version                
├── pyproject.toml          
├── poetry.lock             
└── README.md    
```          
## Configuração de Ambiente


As variáveis de ambiente necessárias para o projeto devem ser definidas no arquivo .env. Um exemplo de configuração pode ser:

* **BASE_PATH** - O path absoluto do diretorio
* **CONTAINER_NAME** - Nome do container
* **CUSTOMER_CSV_PATH** - O path absoluto até o csv
* **AZURE_STORAGE_CONNECTION** - Chave de acesso

### Instalação

Para configurar o ambiente de desenvolvimento, siga os passos abaixo:

**Instale o Poetry:**

```
pip install poetry
```

**Clone o repositório:**

```
git clone
```


**Instale as dependências:**

```
poetry install
```

**Ative o ambiente virtual:**

```
poetry shell
```
**Gere os arquivos executando o gerador:**

```
poetry run poetry data/file_swarm_generator.py
```

## Testes

**Rodando os testes:**

```
pytest tests/ -v
```

## Executando o Projeto


**Para executar o pipeline ETL, utilize o seguinte comando:**

```
poetry run python src/main.py
```
*obs: Comece executando o script que gera os arquivos!*

### Este comando irá:

    1. Converte os dados da pasta raw em um unico CSV.

    2. Carregar os dados para serem processados e enriquecidos no DuckDB.

    3. Os dados serão enviados para o container Azure.


## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Licença
Este projeto está licenciado sob a licença MIT.
