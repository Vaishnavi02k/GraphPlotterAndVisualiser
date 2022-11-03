import numpy as np
import matplotlib.pyplot as plt 
import math

# This function is used for the plotting of the 1-D wave form
def one_D(n=1,l=1):
 try:
  if l == 0:
    print("Please enter a positive value for l, not zero.")  
    return 0  

  x=np.arange(0,l,0.01*l)
  psi=math.sqrt(2/l)*np.sin(n*3.14*x/l)       #Expression for 1-d wave
  dict={}
  psi_list=psi.tolist()             

  #Storing the postion of the partile of the way in a dictionary correspoinding the positon on the x-axis
  for i in range(len(psi)):
   dict[(0.01*i/l)]=psi_list[i]

  print("The Wave function value corresponding to every x is shown ")
  print(dict)

  plt.plot(x,psi)
  plt.xlabel("Distance")
  plt.ylabel("Particle Position")
  plt.title("")

        
  inp = int(input("Enter 1 to export figure, 2 to exit"))
  if inp == 1:
        plt.savefig('plot.png', dpi=300, bbox_inches='tight')
  plt.show()        
 except :
  print("==>Inappropriate input :: Format {'int','int'}")