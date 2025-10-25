import os
from pathlib import Path
from urllib.parse import quote

from dotenv import load_dotenv
from sqlalchemy.engine import URL



caminho_absoluto = str(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../")))
load_dotenv(dotenv_path=f'{caminho_absoluto}/.env')


print("Caminho abosoluto" + caminho_absoluto)
print(load_dotenv)

class Settings:
    PROJECT_NAME: str = "API Backend AliancaSul"
    PROJECT_VERSION: str = "1.0.0"


    MYSQL_EXPERT_USER = os.getenv("MYSQL_EXPERT_USER")
    MYSQL_EXPERT_PASSWORD = os.getenv("MYSQL_EXPERT_PASSWORD")
    MYSQL_EXPERT_SERVER = os.getenv("MYSQL_EXPERT_SERVER")
    MYSQL_EXPERT_DB = os.getenv("MYSQL_EXPERT_DB")


    MYSQL_EXPERT_DRIVER = "mysql+pymysql"
    # Crie a URL da base de dados para o MySQL - EXPERT
    DATABASEMYSQL_EXPERT_URL = URL.create(MYSQL_EXPERT_DRIVER, host=MYSQL_EXPERT_SERVER, username=MYSQL_EXPERT_USER, password=MYSQL_EXPERT_PASSWORD, database=MYSQL_EXPERT_DB, query={"charset": "utf8mb4", "use_unicode": "True"})
