import socket

from parse import parse

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(5)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    request = client_connection.recv(1024)
    print request
    user_name = 'Anonymous'
    request_format = 'GET /?name={user_name} HTTP{everything_else}'
    request_values = parse(format=request_format, string=request)
    if request_values:
        user_name = request_values.named.get('user_name', 'Anonymous')

    template = """\
HTTP/1.1 200 OK

<h1>Hello, {name}!</h1>
"""

    values = {'name': user_name}
    http_response = template.format(**values)

    client_connection.sendall(http_response)
    client_connection.close()
