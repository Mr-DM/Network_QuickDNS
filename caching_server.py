import socket
import json

Port_caching_server = 8000
Port_DNS_server = 9000
MAX_ITEMS_IN_CACHE = 10

last_url = ""
last_ip  = ""


# Cache functions
def update_cache(url, ip):
    # update the cache with the URL and IP (while not exceeding the max size of the cache!)
    if ip == "NOt_FOUND":
        pass
    
    else:
        last_url = url
        last_ip = ip
        print("Join into caching server")
        
        
def get_from_dns():
    server_socket = socket.socket()
    server_socket.bind(("localhost", Port_caching_server))
    
    # configure how many client the server can listen simultaneously
    server_socket.listen(1)
    while True: 
        conn, address = server_socket.accept()  # accept new connection
        # receive data stream. it won't accept data packet greater than 1024 bytes
        url = conn.recv(1024).decode()
        
        ip = search_url_in_cache(url)
        if ip == None:
            ip = translate_url_using_dns(url)
            update_cache(url,ip)
        conn.send(ip.encode())
        conn.close()
        
def search_url_in_cache(url):
    if url == last_url:
        return last_ip
       

# Translate using the DNS server
def translate_url_using_dns(url):
    host = "localhost"
    client_socket = socket.socket()
    client_socket.connect((host, Port_DNS_server))

    client_socket.send(url.encode())

    ip = client_socket.recv(1024).decode()
    client_socket.close()
    return ip




if __name__ == "__main__":
    get_from_dns()