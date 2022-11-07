import threading
from socket import *

clientsConnections = []

class ThreadServer(threading.Thread):
  def __init__(self, conn, addr):
    threading.Thread.__init__(self)
    self.conn = conn
    self.addr = addr
  
  def run(self):
    global clientsConnections
    print(self.addr, "connected!")

    while(1):
      try:
        message = self.conn.recv(2048)
        data = f"<{addr[0]}> {message.decode('utf-8')}"
        if (message):
          self.broadcast(data, message)
        else:
          self.conn.close()
          self.removeClient(self.conn)
          print(self.addr, "finished!")
      except:
        continue
    

  def broadcast(self, data, message):
    global clientsConnections
    for connection in clientsConnections:
      if(connection != self.conn):
        if(message.decode() != "l"):
          connection.sendall(data.encode())
        else:
          self.conn.close()
          self.removeClient(self.conn)
  
  def removeClient(self, connection):
    global clientsConnections
    if (connection in clientsConnections):
      clientsConnections.remove(connection)


HOST = ""
PORT = 50007

sockObj = socket(AF_INET, SOCK_STREAM)
sockObj.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockObj.bind((HOST, PORT))
sockObj.listen()

while(1):
  conn, addr = sockObj.accept()
  clientsConnections.append(conn)
  thread = ThreadServer(conn, addr)
  thread.start()

"""Não tá saindo do chat na hora que digita, só saí depois de outra
pessoa digitar alguma coisa"""