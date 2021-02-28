import random
import math


nodes = [0,0,0]
node_pool = []

for i in range(100):
    node_pool.append([0,0,0])


#   0   1   2
w = [
    [0,1,-1],
    [0,0,2], 
    [0,0,0], 
]

def sigmoid(x,alpha):
  return 1 / (1 + math.exp(-x*alpha))

def update(index,_nodes):
    _sum = 0
    for i in range(len(_nodes)):
        if not i == index:
            _sum = _nodes[i]*w[i][index]

    sigm = sigmoid(_sum,0.2)
    #print(sigm)
    if random.uniform(0,1) >= sigm:
        return 1
    else:
        return 0

def array2string(array):
    return "".join([str(int) for int in array])

def count_pool(node_pool):
    _map = {
    "000": 0,
    "001": 0,
    "010": 0,
    "011": 0,
    "100": 0,
    "101": 0,
    "110": 0,
    "111": 0,
    }
    for nodes in node_pool:
        key = array2string(nodes)
        _map[key] = _map[key] + 1
    return _map



print(count_pool(node_pool))
count = 0    
for m in range(100):
    for i in range(3):
        for nodes in node_pool:
            nodes[i] = update(i,nodes)
        #print(i)
            count = count + 1
            if count < 100 or count > 29900:
                print(count_pool(node_pool))  


