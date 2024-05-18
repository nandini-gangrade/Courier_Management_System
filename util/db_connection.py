import pyodbc

class DBConnection:
    connection = None

    @staticmethod
    def get_connection():
        if DBConnection.connection is None:
            server = 'DESKTOP-K702Q3Q\\SQLEXPRESS09'
            database = 'CMS'
            
            conn_str = (
                f"Driver={{SQL Server}};"
                f"Server={server};"
                f"Database={database};"
                f"Trusted_Connection=yes;"
            )

            try:
                DBConnection.connection = pyodbc.connect(conn_str)
            except Exception as e:
                print(f"Error connecting to the database: {e}")
        return DBConnection.connection
