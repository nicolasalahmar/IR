import sqlite3

from index.index import create_index


def fetch_records(dataset, limit):  # todo remember you are not fetching the id of the document
    sqliteConnection = sqlite3.connect(dataset)
    cursor = sqliteConnection.cursor()
    cursor.execute(f"""SELECT * FROM corpus LIMIT {limit};""")
    records = cursor.fetchall()
    sqliteConnection.close()
    return records


records = fetch_records('dataset1.db', 1)
print(create_index(records))
