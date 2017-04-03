import sqlite3
from database import *

class User:
    """
        Base class creates user object

        Args:
            name: check_if_correct(name, str)
            surname: check_if_correct(surname, str)
            gender: gender
            birth_date: birth_date
            email:
            login:login
            password: check_if_correct(password, str)
    """

    path = "todo.db"

    def __init__(self, _id, login, password):
        """
        Initialize user object

        Args:
            name: check_if_correct(name, str)
            surname: check_if_correct(surname, str)
            gender: gender
            birth_date: birth_date
            email:
            login:login
            password: check_if_correct(password, str)
        """
        self._id = _id
        self.login = login
        self.password = password  #self.check_if_correct(password, str)

    @classmethod
    def get_user(cls, login, password):
        """ On successful authentication returns User or Manager object
            Args:
                login (str): login of the user
                password (str): password of the user
            Returns:
                User (obj): if authentication passed
                None: if authentication fails
        """
        conn = sqlite3.connect(User.path)
        cursor = conn.execute("SELECT * FROM user")
        for row in cursor.fetchall():
            if row[1] == login and row[2] == password:
                conn.close()
                return User(row[0], row[1], row[2])
        conn.close()
        return None