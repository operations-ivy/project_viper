import nmap
import time
import socket

cidr_range = "192.168.4.*"
port = 22


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(0)
    try:
        # doesn't even have to be reachable
        s.connect(('10.254.254.254', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

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


if __name__ == "__main__":
    keep_alive = True
    count = 0
    while keep_alive:
        port_payload = get_open_port_servers()
        print("\n##########################################")
        print("******************************************\n\n")
        for i in port_payload[0].keys():
            ip_addr = get_ip()
            if i != ip_addr:
                print(i)
        print(f"\n{time.time()}")

