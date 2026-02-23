from models.database import Database
from typing import Optional, Self
from sqlite3 import Cursor


class Item:

    def __init__(self: Self,
                 titulo: Optional[str],
                 tipo: Optional[str] = None,
                 indicado_por: Optional[str] = None,
                 id_item: Optional[int] = None) -> None:

        self.titulo = titulo
        self.tipo = tipo
        self.indicado_por = indicado_por
        self.id_item = id_item

    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query = 'SELECT titulo, tipo, indicado_por FROM itens WHERE id = ?;'
            params = (id,)
            resultado = db.buscar_tudo(query, params)

            [[titulo, tipo, indicado]] = resultado

        return cls(titulo, tipo, indicado, id)

    def salvar_item(self) -> None:
        with Database() as db:
            query = """
            INSERT INTO itens (titulo, tipo, indicado_por)
            VALUES (?, ?, ?);
            """
            params = (self.titulo, self.tipo, self.indicado_por)
            db.executar(query, params)

    @classmethod
    def obter_itens(cls) -> list[Self]:
        with Database() as db:
            query = 'SELECT titulo, tipo, indicado_por, id FROM itens;'
            resultados = db.buscar_tudo(query)

            itens = [
                cls(titulo, tipo, indicado, id)
                for titulo, tipo, indicado, id in resultados
            ]

            return itens

    def excluir_item(self) -> Cursor:
        with Database() as db:
            query = 'DELETE FROM itens WHERE id = ?;'
            params = (self.id_item,)
            return db.executar(query, params)

    def atualizar_item(self) -> Cursor:
        with Database() as db:
            query = """
            UPDATE itens
            SET titulo = ?, tipo = ?, indicado_por = ?
            WHERE id = ?;
            """
            params = (self.titulo, self.tipo, self.indicado_por, self.id_item)
            return db.executar(query, params)