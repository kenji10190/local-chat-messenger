import os
import socket
from faker import Faker

sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server_address = '../socket/socket_file'

try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print("サーバーを起動しました。別ターミナルで質問を入力してください。")

sock.bind(server_address)
sock.listen(1)

while True:
    connection, _ = sock.accept()

    try:

        while True:
            data = connection.recv(1024)

            if data:
                data_str = data.decode("utf-8")
                fake = Faker(["ja_JP"])
                
                if "名前" in data_str:
                    response = "私は" + fake.name() + "です。"

                elif "職業" in data_str or "仕事" in data_str:
                    response = fake.job() + "として仕事をしています。"

                elif "会社" in data_str:
                    response = fake.company() + "で働いています。"

                else:
                    response = "有効な質問ではないようです。"
                    
                connection.sendall(response.encode())

            else:
                print("クライアントからの接続が切れたので、終了します。")
                break

    finally:
        print("接続を切ります。")
        connection.close()
        break
        


