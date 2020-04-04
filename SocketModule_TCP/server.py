import socket

host = socket.gethostname()
port = 9337

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(1)

print("\nServer Started...\n")

conn, address = sock.accept()
print("Connection established with: ", str(address))

message="\nThank you for connecting "+str(address)
conn.send(message.encode("ascii"))
conn.close()