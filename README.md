# project_viper
Project Viper (hiss)

project to store smaller coding projects.

- `bazel build tool`: add functionality to build images and packages
- `api_request`: queries chuck norris joke API
    - TODO:
        - Batch request jokes from API
        - Set number of jokes to GET as a parameter
        - Set duplicate check allowance as a parameter
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
            AND
            ```
            Exception has occurred: ConnectionError
            HTTPSConnectionPool(host='api.chucknorris.io', port=443): Max retries exceeded with url: /jokes/random?category=science (Caused by NameResolutionError("<urllib3.connection.HTTPSConnection object at 0x7f29d0074e50>: Failed to resolve 'api.chucknorris.io' ([Errno -2] Name or service not known)"))
            socket.gaierror: [Errno -2] Name or service not known

            The above exception was the direct cause of the following exception:
            ```
- `sqlite_storage`: stores queried chuck norris joke api data
    - TODO:
