import threading

count20 = 0
count30 = 0
count40 = 0
count60 = 0
count70 = 0
count100 = 0


class MeuThread(threading.Thread):
  contaThread = -1

  def __init__(self, maxThread, pings):
    self.pings = pings
    self.maxThread = maxThread
    threading.Thread.__init__(self)

    MeuThread.contaThread += 1
    self.indice = MeuThread.contaThread

  def contarIntervalos(self):
    global count20, count30, count40, count60, count70, count100
    for i in range(self.indice, len(self.pings), self.maxThread):
      if (self.pings[i] >= 20 and self.pings[i] < 30):
        count20 += 1
      elif (self.pings[i] >= 30 and self.pings[i] < 40):
        count30 += 1
      elif (self.pings[i] >= 40 and self.pings[i] < 60):
        count40 += 1
      elif (self.pings[i] >= 60 and self.pings[i] < 70):
        count60 += 1
      elif (self.pings[i] >= 70 and self.pings[i] < 100):
        count70 += 1
      else:
        count100 += 1

  def run(self):
    self.contarIntervalos()

arquivo = open("file1", "r")
data = arquivo.readlines()
pings = []

for i in range(0, len(data)):
  ping = data[i].split(" ")

  pings.append(int(ping[1]))

arquivo.close()

threads = []
maxThread = int(input("Digite o número de threads: "))

for numero in range(0, maxThread):
  thread = MeuThread(maxThread, pings)
  threads.append(thread)
  thread.start()

for thread in threads:
  thread.join()

print("20:", count20)
print("30:", count30)
print("40:", count40)
print("60:", count60)
print("70:", count70)
print("100:", count100)
