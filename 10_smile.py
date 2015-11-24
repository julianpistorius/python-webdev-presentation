from datetime import datetime
import io
import socket
import time

import picamera

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

    byte_stream = io.BytesIO()
    with picamera.PiCamera(resolution=(640, 480), sensor_mode=7) as camera:
        camera.annotate_background = picamera.Color('black')
        camera.annotate_text = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        time.sleep(1)  # Warm-up time
        camera.capture(byte_stream, 'jpeg')

    client_connection.sendall(byte_stream.getvalue())
    client_connection.close()
