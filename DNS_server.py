import socket
import json

PORT = 9000 # DNS Server port
 
# Test with
"""DNS_RECORDS = { 
    "google.com": "1.1.1.1",
    "facebook.com": "2.2.2.2"
}


def search_url_in_Dic():
    if url in DNS_RECORDS:
        return DNS_RECORDS.get(url) 
    else:
        return "NOT_FOUND"
"""

# return the IP of the URL
def search_url_in_database(url):
    with open("database.json", "r") as f:
        DNS_RECORDS = json.load(f)
        if DNS_RECORDS == None:
            print("DNS_RECORDS is empty or not connect")
        else:
            print("Open Json File")
            
    if url in DNS_RECORDS:
        return DNS_RECORDS.get(url) 
    else:
        return "NOT_FOUND"
    
        
# Handle requests from the DNS client
def handle_translation_request():
    server_socket = socket.socket()
    server_socket.bind(("localhost", PORT))
    
    # configure how many client the server can listen simultaneously
    server_socket.listen(1)
    while True: 
        conn, address = server_socket.accept()  # accept new connection
        # receive data stream. it won't accept data packet greater than 1024 bytes
        url = conn.recv(1024).decode()
        
        #ip = search_url_in_Dic(url)
        ip = search_url_in_database(url)
        
        print(f"Url: {url}")
        print(f"Ip: {ip}")
        
        conn.send(ip.encode())
        conn.close()
        print("-"*10)
        
        
    
# Handle requests from the caching server
def handle_translation_requests(url):
    pass


if __name__ == "__main__":
    handle_translation_request()
