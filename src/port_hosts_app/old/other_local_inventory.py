from __future__ import annotations

import nmap
import pandas as pd
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/tables")
def show_tables():
    nm = nmap.PortScanner()

    bad_cols = ["command_line", "scaninfo", "scanstats"]
    good_cols = ["ip_address", "hostname"]
    host_dict = nm.scan("192.168.4.*", "22")

    df = pd.DataFrame(host_dict)

    df.drop("nmap", axis=1, inplace=True)
    df.drop(bad_cols, axis=0, inplace=True)

    inventory = pd.DataFrame(columns=good_cols)
    inventory["ip_address"] = df.index
    inventory.index.rename("index", inplace=True)

    df.reset_index(drop=True, inplace=True)

    for i, row in inventory.iterrows():
        inventory.iloc[i, inventory.columns.get_loc("hostname")] = df.scan[i].hostname()

    return render_template("view.html", tables=[inventory.to_html()], titles=["na"])


if __name__ == "__main__":
    app.run(debug=True)
