import random
import math

nodes = [1,1,1,1,1]

w = [
    [0,-2,-2,-2,-2],
    [-2,0,0,0,0], 
    [-2,0,0,0,0], 
    [-2,0,0,0,0], 
    [-2,0,0,0,0], 
]

def sigmoid(x,alpha):
  return 1 / (1 + math.exp(-x*alpha))

def update(index):
    _sum = 0
    for i in range(len(nodes)):
        if not i == index:
            _sum = nodes[i]*w[i][index]

    sigm = sigmoid(_sum,0.2)
    #print(sigm)
    if random.uniform(0,1) >= sigm:
        return 1
    else:
        return 0

def array2string(array):
    return "".join([str(int) for int in array])

count = 0
while True:
    _pass = False
    for i in range(len(nodes)):
        nodes[i] = update(i)
        print(nodes) 
    count = count + 1   
    if nodes == [0,0,0,0,0]:
        _pass = True
        break
print(count)