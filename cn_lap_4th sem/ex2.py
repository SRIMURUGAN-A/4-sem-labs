import socket 
import sys

def http_get(host, path):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host ,80))
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    client_socket.send_all(request.encode())


    response = b""
    while True:
        data = client_socket.recv(4096)
        if not data :
            break
        response += data

    client_socket.close()
    return response.decode()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <host> <path>")
        sys.exit(1)

    # Get host and path from command line arguments
    host = sys.argv[1]
    path = sys.argv[2]
    
    # Get the web page
    response = http_get(host, path)
    
    # Print the response
    print(response)