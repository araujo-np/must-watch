from typing import Optional

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"mensagem": "Olá, mundo!"}

@app.get("/itens/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/soma/{num1}/{num2}")
async def somar(num1: int, num2: int):
    return {"Resultado": num1 + num2}


# Crie uma rota que retorne a soma de dois números passados por caminho
# (path de url)

# Extra: melhore a tipagem do código usando tipos de mófulo typing onde for 
# necessário