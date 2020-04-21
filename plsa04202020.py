# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 08:28:16 2020

@author: Professional
"""

topics = ['Computer  Science','Electrical  Engineering',  'Psychology',  'Mechanical  Engineering','Civil  Engineering',  'Medical  Science',  'biochemistry']


def init_matr(T, D, W):
    F = np.random.random((W,T))
    TH = np.random.random((T,D))
    
    return F, TH

def em_step(T,D,vocs,W,F,TH):
    convergeF = False
    convergeTH = False
    
    while (convergeF and convergeTH) == False:
        n_wt, n_dt, n_t, n_d = np.zeros((W, T)), np.zeros((D,T)), np.zeros((T,)), np.zeros((D,))
        
        for d in range(D):
            
            for w in vocs[d]:
                Z = 0
                n_dw = vocs[d].get(w)
                if w not in list(bag_of_words): index = list(bag_of_words).index('unknown')
                else: index = list(bag_of_words).index(w)
                for t in range(T): Z += np.dot(F[index,t],TH[t,d]) 
                
                for t in range(T):
                    delta = n_dw * np.dot(F[index,t],TH[t,d]) / Z
                    if delta > 0:
                        n_wt[index,t]+= delta
                        n_dt[d,t]+=delta
                        n_t[t]+=delta
                    #if n_t[t] == np.nan: print(delta)
                        n_d[d]+=delta
                
                for t in range(T): 
                    F[index, t] = n_wt[index,t] / n_t[t]
                    TH[t, d] = n_dt[d,t] / n_d[d] 
                 #   print(index,d,t,sep='******')
                    if abs(1-F[:, t].sum()) <= 1e-5: convergeF = True
                    if abs(1-TH[:, d].sum()) <= 1e-5: convergeTH = True
                    
                    print(F[:, t].sum())
                
    return F, TH           
                
T = len(topics)
D = len(texts)
W = len(bag_of_words)

F, TH = init_matr(T,D,W)
F_upd, TH_upd = em_step(T,D,vocs,W,F,TH)