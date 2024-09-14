import socket
import paramiko
import threading
import logging
import os
import dotenv
import requests

logging.basicConfig(filename="ssh/ssh_logs/ssh.log", level=logging.INFO)
# dotenv()

ip_logger = logging.getLogger("ip_logger")
ip_handler = logging.FileHandler("ssh/ssh_logs/clients_ip.log")
ip_logger.addHandler(ip_handler)
ip_logger.setLevel(logging.INFO)


class SSHServer(paramiko.ServerInterface):
    def check_auth_password(self, username, password):
        # u = os.getenv('USER')
        # p = os.getenv('PASSWORD')
        tries = f"{username}:{password}"
        os.system(f"echo {tries} >> ssh/ssh_logs/tries.log")
        print(tries)
        logging.info(tries)
        return paramiko.AUTH_FAILED


def get_ip_location(client_addr):
    response = requests.get(f"http://ipinfo.io/{client_addr}/json")
    if response.status_code == 200:
        data = response.json()
        return data
    return "Unknown"


def handle_conn(client_sock, client_addr):
    ip_logger.info(client_addr)
    ip_info = get_ip_location(client_addr[0])
    ip_logger.info(f"Connection from {client_addr[0]} ({ip_info})")
    transport = paramiko.Transport(client_sock)
    server_key = paramiko.RSAKey.from_private_key_file("/app/ssh/key")
    transport.add_server_key(server_key)
    ssh = SSHServer()
    transport.start_server(server=ssh)


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(("0.0.0.0", 2222))
    server.listen(222)
    print("Server has started")

    while True:
        client_sock, client_addr = server.accept()
        print(f"connection recieved from {client_sock}:{client_addr}")
        t = threading.Thread(target=handle_conn, args=(client_sock, client_addr))
        t.start()


if __name__ == "__main__":
    main()
