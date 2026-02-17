import socket

Server_port = 8000


def translate_url(url):
    host = "localhost"
    client_socket = socket.socket()
    client_socket.connect((host, Server_port))

    client_socket.send(url.encode())

    ip = client_socket.recv(1024).decode()
    client_socket.close()
    return ip


def run_dns_client():
    while True:
        url = input("Enter a URL address to translate: ")
        ip = translate_url(url)
        
        if (ip == "NOT_FOUND"):
            print("The website does not exist in the database.")
        else:
            print(f"The IP is: {ip}")
        
        print("-"*20)


if __name__ == "__main__":
    run_dns_client()
