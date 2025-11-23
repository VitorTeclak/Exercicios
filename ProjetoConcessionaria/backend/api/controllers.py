import os
import pymysql
import polars as pl
import bcrypt
from pydantic import BaseModel
from backend.config.database import Settings
from sqlalchemy import create_engine, text
from fastapi import FastAPI
MYSQLALCHEMY_DATABASE_EXPERT_URL = Settings.DATABASEMYSQL_EXPERT_URL

router = FastAPI()

@router.get("/")
def root():
    return {"msg": "API funcionando"}

class LoginRequest(BaseModel):
    login: str
    senha: str

@router.post("/login")
async def tentativaLogin(data: LoginRequest):
    login = data.login
    senha = data.senha

    cnn = create_engine(MYSQLALCHEMY_DATABASE_EXPERT_URL)

    with cnn.begin() as conn:
        result = conn.execute(
            text("""
                SELECT senha, nivel_acesso, id_funcionario
                FROM funcionario 
                WHERE login = :login
            """),
            {'login': login}
        )
        row = result.fetchone()

        if row is None:
            return {"status": "Login não encontrado"}

        hash_senha = row.senha  
        nivel_acesso = row.nivel_acesso
        id = row.id_funcionario

        hash_senha = hash_senha.encode("utf-8")

        if bcrypt.checkpw(senha.encode("utf-8"), hash_senha):
            return {"status": "Autenticado", "nivel": nivel_acesso, "id":id}
        else:
            return {"status": "Senha incorreta"}
                                