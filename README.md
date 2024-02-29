# project_viper
Project Viper (hiss)

project to store smaller coding projects.

- `bazel build tool`: add functionalit
- `api_request`: queries chuck norris joke API
    - TODO:
        - Batch request jokes from API
        - Set number of jokes to GET as a parameter
        - Handle retry error:
            ```
            Exception has occurred: ConnectionError
            HTTPSConnectionPool(host='api.chucknorris.io', port=443): Max retries exceeded with url: /jokes/random (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7f51f8080f70>: Failed to resolve 'api.chucknorris.io' ([Errno -2] Name or service not known)"))
            socket.gaierror: [Errno -2] Name or service not known

            The above exception was the direct cause of the following exception:

            urllib3.exceptions.NameResolutionError: <urllib3.connection.HTTPSConnection object at 0x7f51f8080f70>: Failed to resolve 'api.chucknorris.io' ([Errno -2] Name or service not known)

            The above exception was the direct cause of the following exception:

            urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.chucknorris.io', port=443): Max retries exceeded with url: /jokes/random (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7f51f8080f70>: Failed to resolve 'api.chucknorris.io' ([Errno -2] Name or service not known)"))
            ```
- `sqlite_storage`: stores queried chuck norris joke api data
    - TODO:
        - accept sqlite db file as an argument rather than hardcoding db location
        - recreate db to add column 'category', retrieve joke data through category type and store data
        - index value_category on values/category columns in chuck table
