import numpy as np
import matplotlib.pyplot as plt 
import math

#SHM calculator and plotter
def shm(w=0,A=0, phi=0):
  try:
    #Taking input from user
    k=int(input("Enter the spring Constant or its equivalent(k):"))
    m=int(input("Enter the  mass of object(m):"))
    w=math.sqrt(k/m)                                                            #defining angular velocity of shm
    period = 2 * math.pi / w                                                    #defining angular time period of SHM
    frequency = 1 / period                                                      #defining angular frequency of shm
    v_max=A*w                                                                   #defining maxiumum velocity of shm
    total_ene=(1/2)*k*A*A                                                       #defining Total energy of shm
    a_max=A*w*w                                                                 #defining maximum accleraration of shm
    time = np.arange(0, 100, 0.01)
    displacement = A * np.sin(w * time + phi)


    figure, axis = plt.subplots(2, 2)                             #plot graphs

    axis[0, 0].plot(time,displacement)
    axis[0, 0].set_xlabel("x=time")
    axis[0, 0].set_ylabel("y=displacement")
    axis[0, 0].set_title("Displacement vs time graph")


    velocity = A * w * np.cos(w * time + phi)

    axis[0, 1].plot(time, velocity)
    axis[0, 1].set_xlabel("x=time")
    axis[0, 1].set_ylabel("y=velocity")
    axis[0, 1].set_title("velocity vs time graph")

    acceleration = -A * (w ** 2) * np.sin(w * time + phi)

    axis[1, 0].plot(time, acceleration)
    axis[1, 0].set_xlabel("x=time")
    axis[1, 0].set_ylabel("y=acceleration")
    axis[1, 0].set_title("acceleration vs time graph")
    
    figure.delaxes(axis[1][1])
    plt.tight_layout()
    
    inp = int(input("Enter 1 to export figure, 2 to exit"))
    if inp == 1:
      plt.savefig('plot.png', dpi=300)
            
    plt.show()

    print("The following information is also available")
    
    i=0
    while 1:
      i+=1
      #storing the value of all the above defined elements in dictionary
      elements={1:period , 2:frequency, 3:w ,4:v_max , 5:A , 6:a_max , 7:total_ene  }
      #making list of all the above defined elements
      list=[ '1-Time period' ,'2-Frequency' ,'3-Angular velocity','4-Maximum velocity','5-Amplitude of SHM' ,'6-Maximum acceleration','7-Total energy']
      for item in list:
        print(item)
      j=int(input("Press the number corresponding to the information required:"))
      #printing desire output of user
      print(list[j-1])
      print(elements[j])
      print("Press 'q ' to exit") 
      print("press 'y ' to continue")
      n=input()
      if n=='q':
        break
      elif n!='y':
        print("==>Inappropriate input! Exiting the program")
        break
          
  except:
     print("==>Inappropriate input!")