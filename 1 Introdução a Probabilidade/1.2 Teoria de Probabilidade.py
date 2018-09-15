import numpy as np
import seaborn as sns
# simulacao de moedas 1 e -1, cara e coroa
def gera_contagens(k=1000,n=100):
    X= 2 * (np.random.rand(k,n)>0.5)-1
    S= np.sum(X,axis=0)
    return S
x = generate_counts(k=100000)
sns.distplot(x)
# menor valor da soma
np.round(4*np.sqrt(100000))