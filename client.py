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
    while True:
        print("次の質問を入力してください。")
        message = input()
        if "以上" in message:
            break

        sock.sendall(message.encode())

        data = sock.recv(1024)
        data_str = data.decode("utf-8")

        if data:
            print(data_str)
        else:
            print("有効な質問ではないようです。")

finally:
    print("接続を終了します。")
    sock.close()