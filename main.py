from flask import Flask, render_template, request, url_for, redirect
import database
from models.todo import Todo
from flask_jsglue import JSGlue

app = Flask(__name__)
jsglue = JSGlue(app)
database.create_table()

@app.route("/")
def list():
    """ Shows list of todo items stored in the database.
    """
    return render_template('index.html', ToDoThings=Todo.get_all())


@app.route("/add", methods=['GET', 'POST'])
def add():
    """ Creates new todo item
    If the method was GET it should show new item form.
    If the method was POST it shold create and save new todo item.
    """
    if request.method == 'GET':
        return render_template('add.html')
    elif request.method == 'POST':
        new_thing = Todo(request.form['name'])
        new_thing.save()
    return redirect(url_for('list'))




@app.route("/remove/<todo_id>")
def remove(todo_id):
    """ Removes todo item with selected id from the database """
    if request.method == 'GET':
        thing_to_delete = Todo.get_by_id(todo_id)
        thing_to_delete.delete()
        return redirect(url_for('list'))



@app.route("/edit/<todo_id>", methods=['GET', 'POST'])
def edit(todo_id):
    """ Edits todo item with selected id in the database
    If the method was GET it should show todo item form.
    If the method was POST it shold update todo item in database.
    """
    if request.method == 'GET':
        return render_template('update.html', item_id=todo_id)
    elif request.method == 'POST':
        thing_to_edit = Todo.get_by_id(todo_id)
        new_name = request.form['update']
        thing_to_edit.name = new_name
        thing_to_edit.save()
    return redirect(url_for('list'))

@app.route("/toggle/<todo_id>")
def toggle(todo_id):
    """ Toggles the state of todo item """
    if request.method == 'GET':
        thing_to_toggle = Todo.get_by_id(todo_id)
        thing_to_toggle.toggle()
        thing_to_toggle.save()
    return redirect(url_for('list'))


if __name__ == "__main__":
    app.run(debug=True)
