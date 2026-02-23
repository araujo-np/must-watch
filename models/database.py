from sqlite3 import Connection, connect, Cursor
from types import TracebackType
from typing import Any, Optional, Self, Type
import traceback
import os


DB_PATH = os.getenv('DATABASE', './data/mustwatch.sqlite3')


def init_db(db_name: str = DB_PATH) -> None:
    with connect(db_name) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS itens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            tipo TEXT NOT NULL,
            indicado_por TEXT
        );
        """)


class Database:

    def __init__(self, db_name: str = DB_PATH) -> None:
        self.connection: Connection = connect(db_name)
        self.cursor: Cursor = self.connection.cursor()

    def executar(self, query: str, params: tuple = ()) -> Cursor:
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor

    def buscar_tudo(self, query: str, params: tuple = ()) -> list[Any]:
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self) -> None:
        self.connection.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self,
                 exc_type: Optional[Type[BaseException]],
                 exc_value: Optional[BaseException],
                 tb: Optional[TracebackType]) -> None:

        if exc_type is not None:
            print("Erro capturado:")
            traceback.print_tb(tb)

        self.close()