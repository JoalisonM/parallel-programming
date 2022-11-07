import threading
from socket import *

class SendMessageClientThread(threading.Thread):
  def __init__(self, socket, clientName):
    threading.Thread.__init__(self)
    self.socket = socket
    self.clientName = clientName
  
  def run(self):
    while(1):
      try:
        message = input("\n")
        data = f"<{self.clientName}>: {message}"
        if(message == "l"):
          break
        self.socket.sendall(data.encode())
      except:
        self.socket.close()
        break
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

HOST = "192.168.0.123"
PORT = 50007

sockObj = socket(AF_INET, SOCK_STREAM)

threads = []

try:
  clientName = input("Write your name: ")

  print("\n*+*+*+*+*+*+ Welcome %s!!! *+*+*+*+*+*+"%(clientName))
  print("Write 'l' to leave the chat")

  sockObj.connect((HOST, PORT))

  send = SendMessageClientThread(sockObj, clientName)
  receive = ReceiveMessageClientThread(sockObj)

  send.start()
  receive.start()

  threads.append(send)
  threads.append(receive)

  for thread in threads:
    thread.join()
except:
  print("deu ruim")
