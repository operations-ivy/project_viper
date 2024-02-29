import api_request.api_request as api
import sqlite_storage.sqlite_storage as storage


if __name__ == "__main__":
    api = api.ApiRequest()
    storage = storage.SqliteStorage(db_path="/home/zaphod/code/project_viper/sqlite_storage/sqlite.db")
    joke_categories = api.get_categories()
    joke_count = 0
    for category in joke_categories:
        print("###")
        print("Category: " + category)
        print("###")
        ### this approach won't work if we've already added all jokes in a category
        # count = 0
        # while count <= 10:
        #     joke_data = api.get_random_joke_from_category(category)
        #     joke_id = joke_data["id"]
        #     joke_category = category
        #     joke_value = joke_data["value"]
        #     if storage.check_for_duplicate(joke_id, joke_value) == False:
        #         storage.insert_joke(joke_id, category, joke_value)
        #         print("Joke " + str(count) + " added: " + joke_id)
        #         count += 1
        #     else:
        #         print("Duplicate joke found: " + joke_id)
        #         continue
        for i in range(250):
            joke_data = api.get_random_joke_from_category(category)
            joke_id = joke_data["id"]
            joke_category = category
            joke_value = joke_data["value"]
            if storage.check_for_duplicate(joke_id, joke_value) == False:
                storage.insert_joke(joke_id, category, joke_value)
                joke_count += 1
                print("Joke " + str(joke_count) + " added: " + joke_id)
            else:
                print("Duplicate joke found: " + joke_id)
                continue
    
    print("Total Jokes Added this run: " + str(joke_count))
    # for i in range(500):
    #     joke_id = api.get_random()["id"]
    #     joke_value = api.get_random()["value"]
    #     if storage.check_for_duplicate(joke_id) == False:
    #         storage.insert_joke(joke_id, joke_value)
    #         print("Joke " + str(i) + " added: " + joke_id)
    #     else:
    #         print("Duplicate joke found")
    
    
    # storage.close_connection()