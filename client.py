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
        print("質問を入力してください。")
        message = input()
        sock.settimeout(20)

        if "以上" in message:
            break

        sock.sendall(message.encode())

        data = sock.recv(1024)
        data_str = data.decode("utf-8")

        if data:
            print(data_str)

except TimeoutError:
    print("一定時間入力がなかったため、終了します。")

finally:
    print("接続を終了します。")
    sock.close()