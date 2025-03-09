from peewee import SqliteDatabase

def get_conn():
    return SqliteDatabase("dev.sqlite3")
