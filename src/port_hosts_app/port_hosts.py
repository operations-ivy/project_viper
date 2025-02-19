from flask import *
import json
import nmap

cidr_range = "192.168.4.*"
port = 22

app = Flask(__name__)
@app.route("/open_port_hosts")
def get_open_port_servers():
    nm = nmap.PortScanner()

    hosts_dict = nm.scan(cidr_range, str(port))
    port_servers = {}
    for k,v in hosts_dict['scan'].items():
        if v['tcp'][port]['state'] == "open":
            port_servers[k] = {'state': v['tcp'][port]['state'],
                              'server': v['tcp'][port]['product'],
                              'host_os': v['tcp'][port]['version'],
                              'host_platform': v['tcp'][port]['cpe']
                              }
        
    return port_servers, port

@app.route("/health")
def health():
    return jsonify(
        status="UP"
    )

@app.route('/')
def display_data():
    port_servers = get_open_port_servers()
    return render_template('index.html', port_servers=port_servers)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
