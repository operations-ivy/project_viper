import api_request.api_request as api
import sqlite_storage.sqlite_storage as storage


if __name__ == "__main__":
    api = api.ApiRequest()
    storage = storage.SqliteStorage(db_path="/home/zaphod/code/project_viper/sqlite_storage/sqlite.db")
    for i in range(1000):
        joke_id = api.get_random()["id"]
        joke_value = api.get_random()["value"]
        if storage.check_for_duplicate(joke_id) == False:
            storage.insert_joke(joke_id, joke_value)
            print("Joke " + str(i) + " added: " + joke_id)
        else:
            print("Duplicate joke found")
    
    
    storage.close_connection()