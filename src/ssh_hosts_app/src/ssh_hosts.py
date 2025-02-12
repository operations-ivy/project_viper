from flask import *
import json
import nmap

cidr_range = "172.19.0.*"
port = 22

app = Flask(__name__)
@app.route("/open_ssh_hosts")
def get_open_ssh_servers():
    nm = nmap.PortScanner()

    hosts_dict = nm.scan(cidr_range, str(port))
    ssh_servers = {}
    for k,v in hosts_dict['scan'].items():
        if v['tcp'][22]['state'] == "open":
            ssh_servers[k] = {'ssh_state': v['tcp'][22]['state'],
                              'ssh_server': v['tcp'][22]['product'],
                              'host_os': v['tcp'][22]['version'],
                              'host_platform': v['tcp'][22]['cpe']
                              }
        
    return ssh_servers

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route('/')
def display_data():
    ssh_servers = get_open_ssh_servers()
    return render_template('index.html', ssh_servers=ssh_servers)

if __name__ == "__main__":
    app.run(debug=True, host=('0.0.0.0'))