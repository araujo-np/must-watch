from flask import Flask, render_template, request, redirect, url_for
from models.item import Item
from models.database import init_db

app = Flask(__name__)

init_db()


@app.route('/')
def home():
    return render_template('home.html', titulo="Home")


@app.route('/lista', methods=['GET', 'POST'])
def lista():

    if request.method == 'POST':
        titulo = request.form['titulo']
        tipo = request.form['tipo']
        indicado = request.form.get('indicado_por')

        item = Item(titulo, tipo, indicado)
        item.salvar_item()

        return redirect(url_for('lista'))

    itens = Item.obter_itens()

    return render_template(
        'lista.html',
        titulo="Must Watch",
        itens=itens
    )


@app.route('/delete/<int:idItem>')
def delete(idItem):
    item = Item.id(idItem)
    item.excluir_item()
    return redirect(url_for('lista'))


@app.route('/update/<int:idItem>', methods=['GET', 'POST'])
def update(idItem):

    if request.method == 'POST':
        titulo = request.form['titulo']
        tipo = request.form['tipo']
        indicado = request.form.get('indicado_por')

        item = Item(titulo, tipo, indicado, idItem)
        item.atualizar_item()

        return redirect(url_for('lista'))

    itens = Item.obter_itens()
    item_selecionado = Item.id(idItem)

    return render_template(
        'lista.html',
        titulo=f'Editando ID {idItem}',
        itens=itens,
        item_selecionado=item_selecionado
    )

    if __name__ == "__main__":
        app.run(debug=True)