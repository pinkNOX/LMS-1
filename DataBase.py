import sqlite3
X = sqlite3.connect("./database1.db")


cur = X.cursor()
sql = """
    CREATE TABLE IF NOT EXISTS user(
    id INTEGER,
    title text,
    author text,
    year INTEGER,
    isbn INTEGER
    );
    """
cur.execute(sql)
X.commit()
X.close()
