from socket import *
import threading

class ThreadServer(threading.Thread):
  def __init__(self, conn, addr):
    threading.Thread.__init__(self)
    self.conn = conn
    self.addr = addr
  
  def run(self):
    print(self.addr, "conectou!")
    data = self.conn.recv(1024)
    while(data):
      print("Recebeu:", data.decode())
      self.conn.sendall(data) # Manda de volta tudo o que recebeu
      data = self.conn.recv(1024)
    self.conn.close()
    print(self.addr, "encerrou!")

ADDR = ""
PORT = 50007

sockObj = socket(AF_INET, SOCK_STREAM)
sockObj.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # Kernel usa um socket ainda em TIME_WAIT
sockObj.bind((ADDR, PORT))
sockObj.listen()

while(True):
  conn, addr = sockObj.accept()
  thread = ThreadServer(conn, addr)
  thread.start()