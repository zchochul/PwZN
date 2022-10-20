#convolve2D może pomóc
#najrozsądniej jest to trzymać w numpy
#generator po krokach ma coś zwracać

import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
import matplotlib
from scipy.sparse import spdiags,linalg,eye
import sys
from time import sleep
from tqdm import tqdm

#parametry -> N (lattice), st (steps) 

class Ising():
    ''' Simulating the Ising model '''    
    
    def __init__(self) -> None:
        self.temp = .4
        self.N = int(sys.argv[1])
        self.st = int(sys.argv[2])
        print('Set parameters:')
        print('1. N =', int(sys.argv[1]))
        print('2. steps =', int(sys.argv[2]))
        print('We are starting the simulation!')

    ## monte carlo moves
    def mcmove(self, config, N, beta): #config-> | N, N -> lattice | Beta -> 1/temp
        ''' This is to execute the monte carlo moves'''
        for i in range(N):
            for j in range(N):            
                    a = np.random.randint(0, N)
                    b = np.random.randint(0, N)
                    s =  config[a, b]
                    nb = config[(a+1)%N,b] + config[a,(b+1)%N] + config[(a-1)%N,b] + config[a,(b-1)%N]
                    cost = 2*s*nb
                    if cost < 0:	
                        s *= -1
                    elif rand() < np.exp(-cost*beta):
                        s *= -1
                    config[a, b] = s
        return config
    

    
    def simulate(self):   
        ''' This module simulates the Ising model'''
        config = 2*np.random.randint(2, size=(self.N,self.N))-1
        f = plt.figure(figsize=(15, 15), dpi=80);    
        
        
        lattice_dim =  64
        for step in tqdm(range(self.st + 1)):
            self.configPlot(f, config, step, self.N, step +1)
            for i in range(lattice_dim):
                self.mcmove(config, self.N, 1.0/self.temp)
            
        
    def configPlot(self, f, config, i, N, n_):
        ''' This modules plts the configuration once passed to it along after some steps '''
        X, Y = np.meshgrid(range(N), range(N))
        sp =  f.add_subplot(3, 3, n_ )  
        plt.setp(sp.get_yticklabels(), visible=False)
        plt.setp(sp.get_xticklabels(), visible=False)      
        plt.pcolormesh(X, Y, config, cmap=plt.cm.PiYG)
        plt.title('Makro step=%d'%i); plt.axis('tight')    
        plt.savefig('walka.png')

rm = Ising()
rm.simulate()