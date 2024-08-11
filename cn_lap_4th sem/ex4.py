import socket

# Predefined DNS records
DNS_TABLE = {
    'example.com': '93.184.216.34',
    'google.com': '142.250.190.14',
    'yahoo.com': '98.137.246.7',
}

def start_dns_server(host='localhost', port=5353):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((host, port))
    print(f"DNS server started on {host}:{port}")

    while True:
        message, client_address = server_socket.recvfrom(512)
        domain_name = message.decode('utf-8').strip()
        print(f"Received query for {domain_name}")

        ip_address = DNS_TABLE.get(domain_name, '0.0.0.0')  # Return '0.0.0.0' if not found
        server_socket.sendto(ip_address.encode('utf-8'), client_address)
        print(f"Sent IP address {ip_address} for {domain_name} to {client_address}")

if __name__ == "__main__":
    start_dns_server()



import socket

def query_dns_server(host='localhost', port=5353, domain_name='example.com'):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(2)

    try:
        client_socket.sendto(domain_name.encode('utf-8'), (host, port))
        data, _ = client_socket.recvfrom(512)
        ip_address = data.decode('utf-8')
        print(f"The IP address for {domain_name} is {ip_address}")
    except socket.timeout:
        print("Request timed out")
    finally:
        client_socket.close()

if __name__ == "__main__":
    # Replace 'example.com' with the domain you want to query
    query_dns_server(domain_name='example.com')
