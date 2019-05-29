import math
import random
import stdrandom
import sys
import stdstats
import stddraw
import stdaudio
hurst = 0.50

def recur(arr,i0,i1,variance,scale):
    if (i1-i0) <= 1 :
        return
    
    

    ym=(arr[i0]+arr[i1])/2
    delta = random.gauss(0,variance ** 0.5)
    tm=(i0+i1)//2
    arr[tm]=ym + delta
    
    new_scale = 2 ** (2.0 * scale)   
    new_variance = variance/new_scale
    recur(arr,i0,tm,new_variance, scale)
    recur(arr,tm,i1,new_variance, scale)

    return arr
arr = [0]*882000
variance = 0.05

counter=1
for i in range(20):
    recur(arr,i*44099,44099*counter,variance,hurst)
    counter+=1


whitearr = []
def generate_white():
    for i in range(882000):
        whitearr.append(random.uniform(float(-0.25),float(0.25)))
    return(whitearr)

whitearr= generate_white()
waves = 882000*[0]
for i in range(882000):
    blend= (math.sin(math.pi*0.20*i/44100)**6)
    waves[i]=((1-blend)*arr[i]+blend*whitearr[i])

stdaudio.playSamples(waves)



