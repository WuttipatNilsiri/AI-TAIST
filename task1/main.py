import random
import math

import matplotlib.pyplot as plt 

def sigmoid(x,alpha):
  return 1 / (1 + math.exp(-x*alpha))

def gen_rng_uniform(seed,x,y,count):
    w = []
    random.seed(seed) 
    for i in range(count): 
        rng = random.uniform(x,y) 
        w.append(rng) 
    return w
def gen_rng(seed,count):
    w = []
    random.seed(seed) 
    for i in range(count): 
        rng = random.random() 
        w.append(rng) 
    return w


input_ = gen_rng_uniform(0,-1,1,6)
layer_w = [1,-1,2,-1,2,-1]

print("input_: "+str(input_))
print("layer_w: "+str(layer_w))

sum = 0
for i in range(5):
    sum = sum + input_[i]*layer_w[i]
print(sum)

ans = sigmoid(sum,10)
max_v = max(input_)
print("sigmoid: " + str(ans))



def test(count):
    rng_arr = gen_rng(None,count)
    _max = max(rng_arr)
    print("max_rand: " + str(_max))
    arr = []
    for i in range(count):
        if rng_arr[i] <= ans*_max:
            arr.append(1)
        else:
            arr.append(0)
    return arr

def plot_g(rag,show=True):
    plt.style.use('seaborn-whitegrid')
    y = test(rag)
    x = range(rag)
    plt.plot(x, y, 'o', color='black')
    print("count 1: " + str(y.count(1)))
    if show:
        plt.show()

for i in range(50):
    plot_g(1000,False)
            
        

