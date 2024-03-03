import socket
import sys

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = "../socket/socket_file"
print(server_address, "と接続中です…")

try:
    sock.connect(server_address)
except socket.error as err:
    print(err)
    sys.exit(1)

try:
    message = sys.argv[1]
    sock.sendall(message.encode())
    sock.settimeout(10)

    try:
        while True:
            data = sock.recv(32)
            data_str = data.decode("utf-8")

            if data:
                print(data_str)
            else:
                break

    except TimeoutError:
        print("質問が無いようなので、接続を切ります。")

finally:
    sock.close()