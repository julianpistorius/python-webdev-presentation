import socket

HOST, PORT = '', 8888

# Create a new socket.
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Set the socket options:
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Bind the socket to address. The socket must not already be bound.
listen_socket.bind((HOST, PORT))
# Listen for connections made to the socket. The backlog argument specifies the number of
# unaccepted connections that the system will allow before refusing new connections.
listen_socket.listen(5)

print 'Serving HTTP on port %s ...' % PORT
while True:
    # Accept a connection, returning new socket and client address.
    client_connection, client_address = listen_socket.accept()
    # Receive data - 1024 is the buffer size.
    request = client_connection.recv(1024)
    print request

    http_response = """\
HTTP/1.1 200 OK

<h1>Hello, World!</h1>
"""
    client_connection.sendall(http_response)
    client_connection.close()
