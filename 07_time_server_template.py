from datetime import datetime
import socket

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

    template = """\
HTTP/1.1 200 OK

<h1>The Time</h1>
<p>{time}<p>
"""

    current_time = datetime.now()
    values = {'time': current_time}
    http_response = template.format(**values)

    client_connection.sendall(http_response)
    client_connection.close()
