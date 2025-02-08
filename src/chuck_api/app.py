import os
import sys

from flask import *
import pickle
from opentelemetry.instrumentation.flask import FlaskInstrumentor


current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from sqlite_storage.sqlite_storage import SqliteStorage

FlaskInstrumentor().instrument(enable_commenter=True, commenter_options={})

# joke_json = {
#     {'id': ''},
#     {'category': ''},
#     {'value': ''},
#     {'timestamp': ''}
# }

app = Flask(__name__)


FlaskInstrumentor().instrument_app(app)

@app.route("/")
def show_all_jokes():
    db_location = "/home/zaphod/code/project_viper/src/sqlite_storage/sqlite.db"
    storage = SqliteStorage(db_path=db_location)

    all_of_it = storage.read_all_jokes()

    html = ''
    for i in all_of_it:
        html += '<h2>category: ' + i[1] + '</br>'
        html += '<h3>value ' + i[2]
    
    return html


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')