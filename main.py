import api_request.api_request as api
import sqlite_storage.sqlite_storage as storage

api = api.ApiRequest()
storage = storage.SqliteStorage(db_path="/home/zaphod/code/project_viper/sqlite_storage/sqlite.db")


print(api.get_random()["id"])
print(api.get_random()["value"])

storage.insert_joke(api.get_random()["id"], api.get_random()["value"])