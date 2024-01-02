import api_request.api_request as api
import sqlite_storage.sqlite_storage as storage

api = api.ApiRequest()

print(api.get_random()["value"])