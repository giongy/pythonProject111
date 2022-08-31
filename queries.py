from PyQt5.QtSql import QSqlQuery


def create_initial_tables():
    print("creo tabelle")
    createTableQuery = QSqlQuery()
    create = createTableQuery.exec(
        """
        CREATE TABLE contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL
        )
        """
    )
    print(create)
