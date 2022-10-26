#convolve2D może pomóc
#najrozsądniej jest to trzymać w numpy
#generator po krokach ma coś zwracać

from distutils.command.config import config
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
import matplotlib
from scipy.sparse import spdiags,linalg,eye
import sys
from time import sleep
from tqdm import tqdm
from PIL import Image
import glob


#parametry -> N (lattice),
#             st (steps),
#             J (integral),
#             Beta (1/temp),
#              B (magnetic field)   


class Ising():
    ''' Simulating the Ising model '''    
    def __init__(self) -> None:
        self.Magnetization = 0.0
        self.N = int(sys.argv[1])
        self.st = int(sys.argv[2])
        self.J = float(sys.argv[3])
        self.Beta =  float(sys.argv[4])
        self.temp = 1/self.Beta
        self.B = int(sys.argv[5])
        
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
    
    def magnet(self, config):
        for i in range(self.N):
            for j in range(self.N):
                self.Magnetization += config[i, j]
        #self.Magnetization = self.Magnetization/self.N
        print(self.Magnetization/(self.N*self.N))

    
    def simulate(self):   
        ''' This module simulates the Ising model'''
        config = 2*np.random.randint(2, size=(self.N,self.N))-1
        f = plt.figure(figsize=(15, 15), dpi=80);
        g = plt.figure(figsize=(15, 15), dpi=80); 
        lattice_dim =  64
        for step in tqdm(range(self.st + 1)):
            self.savePlot(g, config, step, self.N, step +1)
            #self.configPlot(f, config, step, self.N, step +1)
            for i in range(lattice_dim):
                self.mcmove(config, self.N, 1.0/self.temp)
        self.gifGenerate()
        self.magnet(config)

    def savePlot(self, g, config, i, N, n_):
        X, Y = np.meshgrid(range(N), range(N))    
        plt.pcolormesh(X, Y, config, cmap=plt.cm.PiYG)
        plt.title('Makro step=%d'%i); plt.axis('tight')   
        plt.savefig('Step%d.png'%i)
    
    def gifGenerate(self):
        # Create the frames
        frames = []
        imgs = sorted(glob.glob("*.png"))
        for i in imgs:
            new_frame = Image.open(i)
            frames.append(new_frame)
        # Save into a GIF file that loops forever
        frames[0].save('animejszyn.gif', format='GIF',
            append_images=frames[1:],
            save_all=True,
            duration=300, loop=0)

#    def configPlot(self, f, config, i, N, n_):
#        ''' This modules plts the configuration once passed to it along after some steps '''
#        X, Y = np.meshgrid(range(N), range(N))
#        sp =  f.add_subplot(3, 3, n_ )  
#        plt.setp(sp.get_yticklabels(), visible=False)
#        plt.setp(sp.get_xticklabels(), visible=False)      
#        plt.pcolormesh(X, Y, config, cmap=plt.cm.PiYG)
#        plt.title('Makro step=%d'%i); plt.axis('tight')    
#        plt.savefig('walka.png')

rm = Ising()
rm.simulate()