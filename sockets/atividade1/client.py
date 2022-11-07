import threading
from socket import *

class SendMessageClientThread(threading.Thread):
  def __init__(self, socket):
    threading.Thread.__init__(self)
    self.socket = socket
  
  def run(self):
    while(1):
      try:
        message = input("\n")
        self.socket.sendall(message.encode())
      except:
        self.socket.close()

class ReceiveMessageClientThread(threading.Thread):
  def __init__(self, socket):
    threading.Thread.__init__(self)
    self.socket = socket
  
  def run(self):
    while(1):
      try:
        response = self.socket.recv(2048)
        print(response.decode("utf-8") + "\n")
      except:
        return

HOST = "127.0.0.1"
PORT = 50007

sockObj = socket(AF_INET, SOCK_STREAM)

sockObj.connect((HOST, PORT))

threads = []

send = SendMessageClientThread(sockObj)
receive = ReceiveMessageClientThread(sockObj)

threads.append(send)
threads.append(receive)

send.start()
receive.start()

for thread in threads:
  thread.join()