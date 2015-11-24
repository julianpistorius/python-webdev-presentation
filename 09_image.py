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

    image = open('kit-kat.jpg', 'rb')
    image_data = image.read()
    image.close()

    headers = '''HTTP/1.1 200 OK
Content-Type:image/jpg
Content-Length:%d

''' % len(image_data)
    client_connection.send(headers)
    client_connection.sendall(image_data)
    client_connection.close()
