import random
import math

nodes = [0,0,0]

#   0   1   2
w = [
    [0,-2,-2],
    [-2,0,-2], 
    [-2,-2,0], 
]

def sigmoid(x,alpha):
  return 1 / (1 + math.exp(-x*alpha))

def update(index):
    _sum = 0
    for i in range(len(nodes)):
        if not i == index:
            _sum = nodes[i]*w[i][index]

    sigm = sigmoid(_sum,1)
    #print(sigm)
    if random.uniform(0,1) >= sigm:
        return 1
    else:
        return 0

def array2string(array):
    return "".join([str(int) for int in array])

map = {
    "000": 0,
    "001": 0,
    "010": 0,
    "011": 0,
    "100": 0,
    "101": 0,
    "110": 0,
    "111": 0,
}

for i in range(100):
    nodes[0] = update(0)
    key = array2string(nodes)
    map[key] = map[key] + 1
    nodes[1] = update(1)
    key = array2string(nodes)
    map[key] = map[key] + 1
    nodes[2] = update(2)
    key = array2string(nodes)
    map[key] = map[key] + 1

print(map)
    