from multiprocessing import shared_memory
import os

def particao(vetor, l, h):
  pivo = h
  pa = l
  for i in range(l, h):
    if(vetor[i] < vetor[pivo]):
      (vetor[i], vetor[pa]) = (vetor[pa], vetor[i])
      pa += 1
  
  (vetor[pivo], vetor[pa]) = (vetor[pa], vetor[pivo])
  return pa

def quicksort(vetor, l=0, h=None):
  if(h==None):
    h = len(vetor)-1
  
  if(h>l):
    pivo = particao(vetor, l, h)
    quicksort(vetor, l, pivo-1)
    quicksort(vetor, pivo+1, h)

print("Informe um vetor de número: ", end=" ")
vetor = list(map(int, input().split()))
vetor = shared_memory.ShareableList(vetor)
pivo = particao(vetor, 0, len(vetor)-1)

print(pivo)

if(os.fork == 0): # Ordena a metade inferior
  quicksort(vetor, 0, pivo-1)
  exit(0)

if(os.fork() == 0): # Ordena a metade superior
  quicksort(vetor, pivo+1, len(vetor)-1)
  exit(0)
os.wait()
print(vetor)
vetor.shm.unlink()