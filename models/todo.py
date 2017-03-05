import sqlite3
import database


class Todo:
    """ Class representing todo item."""

    def __init__(self, name, id = None, done=False):
        self.id = id
        self.name = name
        self.done = done


    def toggle(self):
        """ Toggles item's state """
        self.done = not self.done

    def save(self):
        """ Saves/updates todo item in database """
        if self.id:
            database.data_query("UPDATE Tasks SET `name` = ?, done = ? WHERE id = ?", (self.name, self.done, self.id))
        else:
            database.data_query("INSERT INTO Tasks (`name`, done) VALUES (?, ?)", (self.name, self.done))

    def delete(self):
        """ Removes todo item from the database """
        database.data_query("DELETE FROM Tasks WHERE id = ?", (self.id,))

    @classmethod
    def get_all(cls):
        """ Retrieves all Todos form database and returns them as list.
        Returns:
            list(Todo): list of all todos
        """
        todo_list = []
        data = database.data_query("SELECT * FROM Tasks", ())
        id = 1
        name = 0
        toogle = 2
        for row in data:
            todo_list.append(cls(row[id], row[name], row[toogle]))
        return todo_list

    @classmethod
    def get_by_id(cls, id):
        """ Retrieves todo item with given id from database.
        Args:
            id(int): item id
        Returns:
            Todo: Todo object with a given id
        """
        data = database.data_query("SELECT * FROM Tasks WHERE id = ?;", (id,))
        row = data[0]
        if row:
            return cls(row[1], row[0], row[2])
