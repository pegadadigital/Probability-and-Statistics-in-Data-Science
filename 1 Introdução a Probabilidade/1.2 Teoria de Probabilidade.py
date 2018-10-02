import numpy as np
import matplotlib.pyplot as plt

# simulacao de moedas 1 e -1, cara e coroa
def gera_contagens(k=1000,n=100):
    X= 2 * (np.random.rand(k,n)>0.5)-1  
    S= np.sum(X,axis=0)
    return S
k=1000
n=100
counts=gera_contagens(k=k,n=n)
plt.figure(figsize=[10,4]);
plt.hist(counts);
plt.xlim([-k,k]);
plt.xlabel("soma");
plt.ylabel("quant");
plt.title("Histograma da soma de valores de moeda jogadas %d vezes"%k);
plt.grid();

plt.figure(figsize=[13,3.5])
for j in range(2,5):
    k=10**j
    counts=gera_contagens(k=k,n=1000)
    plt.subplot(130+j-1)
    plt.hist(counts,bins=10);
    d=4*np.sqrt(k)
    plt.plot([-d,-d],[0,30],'r')
    plt.plot([+d,+d],[0,30],'r')
    plt.grid()
    plt.title('%d jogadas, faixa=+-%6.1f'%(k,d))


plt.figure(figsize=[13,3.5])
for j in range(2,5):
    k=10**j
    counts=gera_contagens(k=k,n=100)
    plt.subplot(130+j-1)
    plt.hist(counts,bins=10);
    plt.xlim([-k,k])
    d=4*np.sqrt(k)
    plt.plot([-d,-d],[0,30],'r')
    plt.plot([+d,+d],[0,30],'r')
    plt.grid()
    plt.title('%d jogadas, faixa=+-%6.1f'%(k,d))

# menor valor da soma
np.round(4*np.sqrt(1000))

# 1.3
# probabilidade de ser 507 caras
# soma S1000=507-493=14
# 14<<126

# Quiz
# probabilidade de ser 507 caras
# soma S1000=610-390=220
# 220>126
def seq_sum(n):
    """ input: n, generate a sequence of n random coin flips
        output: return the number of heads 
        Hint: For simplicity, use 1,0 to represent head,tails
    """
    X= 1 * (np.random.rand(n)>0.5)
    S= np.sum(X[X==1])
    return S

v=np.array([],dtype=int)
for j in range(0,1000):
   v=np.append(v,[seq_sum(100)])
S=len(v[np.logical_and(v>=45,v<55)])/1000
len(v[np.logical_and(v>=45,v<55)])