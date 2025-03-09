from peewee import SqliteDatabase, PostgresqlDatabase
import os

from config import MODE

def get_conn():
	if MODE == "development":
		return SqliteDatabase(os.getenv("DB_DEV") or "dev.sqlite3")
	else:
		database = os.getenv("DB_NAME")
		user = os.getenv("DB_USER")
		password = os.getenv("DB_PASSWORD")
		host = os.getenv("DB_HOST")
		port = os.getenv("DB_PORT")

		return PostgresqlDatabase(database, user=user, password=password, host=host, port=port)