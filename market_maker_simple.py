import numpy
import matplotlib.pyplot as plt
import math
import scipy.linalg
import pandas as pd


S0 = 100.00 # for midprice
T  = 30 # terminal date
std = 0.01
alpha = 0.0001
#alpha=0
N = 30 # inventory ??
drifts = [-0.2,0,0.2]
q_up = 3 # upper bound
q_low = -3
q = 1        
kappa = 100
#phi = 0
phi = 0.00001
lambda_pos = 1
lambda_neg = 1


#hack
delta_t=1

def makeWienerIncrements(delta_t,N):
    return float(math.sqrt(delta_t))*numpy.random.randn(N)

def makeAssetMidprices(S0, std, delta_t,N,drift):
	dS=std*makeWienerIncrements(delta_t,N)
	dD=drift*numpy.full(N,delta_t)
	dS[0]=0
#    return S0+numpy.cumsum(dS)+numpy.cumsum(dD)
	return S0 +numpy.cumsum(dS)







def sell_optimal_depth(t,q,kappa):
   	#return getSellOptimalDepth(t,q,kappa)
   return (1.0/kappa - h(t,q-1) + h(t,q))

def buy_optimal_depth(t,q,kappa):
    #return getBuyOptimalDepth(t,q,kappa)
    return (1.0/kappa -h(t,q+1) + h(t,q))

def h(t,q):
    return (math.log(w(t,q))*1.0/kappa)

#this part is not coded well and the equations are misplaced. The upper
#and lower bounds are also manipulated everywhere making it harded to debug. 
#this code is basically useless.
def w(t,q):
    index = range(-3,3)#range(q_low,q_up+1)
    df = pd.DataFrame(index=index, columns=index)
    df = df.fillna(0)
    for i in range(-3,3): #range(q_low,q_up+1):
        for q in range(-3,3): #range(q_low,q_up+1):
             if i == q:
                             df.loc[i,q] = -1*q*q  #phi scaled 
             elif i == q-1:
                 df.loc[i,q] = lambda_pos/math.e
             elif i == q+1:
                 df.loc[i,q] = lambda_neg/math.e
            #                 else:
            #                     0
                 return df
                 
                 
#	temp = df*(T-t)
#	z = pd.DataFrame(index=['0'], columns=index)
#	z = z.fillna(0)
#	for i in range(q_low,q_up+1):
#		z.ix[0,i] = math.exp(-1*alpha*kappa*i*i)
#	tempnp = temp.as_matrix()
#	znp = z.as_matrix().ravel()
#	temp2 = numpy.dot(scipy.linalg.expm(tempnp),znp)
#	return temp2.ix[q]







def u(t,q):
    return lambda_neg*math.exp(-1*kappa*buy_optimal_depth(t,q,kappa)) - lambda_pos*math.exp(-1*kappa*sell_optimal_depth(t,q,kappa))

def get_sell_fill_rate(t,q):
    return lambda_pos*math.exp(-1*kappa*sell_optimal_depth(t,q,kappa))

def get_buy_fill_rate(t,q):
    return lambda_neg*math.exp(-1*kappa*buy_optimal_depth(t,q,kappa))



# Graph 10.1

fig1 = plt.figure()

rngt = list(range(30+1))
rng = list(range(q_low+1, q_up+1))
graph101 = pd.DataFrame(index=rngt, columns=rng)

for x in rngt:
    for y in rng:
	graph101[x,y] = df
     #graph101[x,y] = sell_optimal_depth(x,y,kappa)

graph101.plot()







