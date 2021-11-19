from psycopg2 import pool


class Database():
    """
    the connection_pool is a static property of the Database Class
    """
    __connection_pool = None

    @classmethod
    def initialise(cls, **kwargs):
        cls.__connection_pool = pool.SimpleConnectionPool(1, 10, **kwargs)

    @classmethod
    def get_connection(cls):
        return cls.__connection_pool.getconn()

    @classmethod
    def return_connection(cls, connection):
        Database.__connection_pool.putconn(connection)


    @classmethod
    def delete_all_connections(cls):
        Database.__connection_pool.closeall()


# when we call this class, at first, the connection is None (empty). and then the __enter__ method
# Run automatically and the new connection will run. ( at the user.py , save_to_db method).
class CurserFromConnectionFromPool():
    def __init__(self):
        self.connection = None
        self.cursor = None

    def __enter__(self):
        self.connection= Database.get_connection()
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exception_type, exception_value, exception_traceback):
        if exception_value is not None:  #mesle rokh dadane TypeError, AttributeError, ValueError . agar shod, connection ghat mishe(rollback)
            self.connection.rollback()
        else:
            self.cursor.close()
            self.connection.commit()
            Database.return_connection(self.connection)