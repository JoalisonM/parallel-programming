from multiprocessing import shared_memory
import os

def merge(vetor, p, meio, u):
  aux = [0] * len(vetor)
  for k in range(p, u + 1):
    aux[k] = vetor[k]
  t = p
  i = meio + 1
  for k in range(p, u + 1):
    if t > meio:
      vetor[k] = aux[i]
      i += 1
    elif i > u:
      vetor[k] = aux[t]
      t += 1
    elif aux[i] < aux[t]:
      vetor[k] = aux[i]
      i += 1
    else:
      vetor[k] = aux[t]
      t += 1

def mergeSort(vetor, p, u):
  if(p < u):
    meio = int((p+u)//2)
    mergeSort(vetor, p, meio)
    mergeSort(vetor, meio+1, u)
    merge(vetor, p, meio, u)

print("Informe um vetor de número: ", end=" ")
vetor = list(map(int, input().split()))
vetor = shared_memory.ShareableList(vetor)

primeiroElemento = 0
ultimoElemento = len(vetor)-1
meio = int((primeiroElemento+ultimoElemento)//2)

if(os.fork() == 0): # ordena até o meio do vetor
  mergeSort(vetor, primeiroElemento, meio) 
  exit(0)

if(os.fork() == 0): # ordena depois da metade do vetor
  mergeSort(vetor, meio+1, ultimoElemento)
  exit(0)

if(os.fork() == 0): # faz a junção das duas metades
  merge(vetor, primeiroElemento, meio, ultimoElemento)
  exit(0)

os.wait()
print(vetor)
vetor.shm.unlink()