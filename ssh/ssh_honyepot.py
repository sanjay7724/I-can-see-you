import socket
import paramiko
import threading
import logging
import os

logging.basicConfig(filename='ssh_logs/ssh.log',level=logging.INFO)

ip_logger = logging.getLogger('ip_logger')
ip_handler = logging.FileHandler('ssh_logs/clients_ip.log')
ip_logger.addHandler(ip_handler)
ip_logger.setLevel(logging.INFO)

class SSHServer(paramiko.ServerInterface):
    def check_auth_password(self,username,password):
        tries = f"{username}:{password}"
        os.system(f"echo {tries} >> ssh_logs/tries.log")
        print(tries)
        logging.info(tries)
        return paramiko.AUTH_FAILED

def handle_conn(client_sock,client_addr):
    ip_logger.info(client_addr)
    transport = paramiko.Transport(client_sock)
    server_key = paramiko.RSAKey.from_private_key_file('key')
    transport.add_server_key(server_key)
    ssh = SSHServer()
    transport.start_server(server=ssh)

def main():
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(('',2222))
    server.listen(222)
    print("Server has started")

    while True:
        client_sock,client_addr = server.accept()
        print(f"connection recieved from {client_sock}:{client_addr}")
        t = threading.Thread(target=handle_conn,args=(client_sock,client_addr))
        t.start()
        
   
if __name__ == "__main__":
    main()