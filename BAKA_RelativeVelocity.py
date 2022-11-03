import numpy as np
import matplotlib.pyplot as plt 
import math
#This function is to compare the realtive velocity and acceleration of 2objects
def RelativeVelocity(v1=0, v2=0, a1=0, a2=0):
 try:
   #Initialising the velovity ,distance of the objects
   time = np.arange(0, 100, 1)
   distance1 = v1 * time + 1 / 2 * a1 * (time) ** 2
   distance2 = v2 * time + 1 / 2 * a2 * (time) ** 2
   v_new1 = v1 + a1 * time
   v_new2 = v2 + a2 * time

   figure, axis = plt.subplots(2, 2)       #using subplot to plot various graph

   axis[0, 0].plot(time, distance1)
   axis[0, 0].plot(time, distance2)
   axis[0, 0].set_xlabel('Time', fontsize=6)
   axis[0, 0].set_ylabel('Distance', fontsize=6)
   axis[0, 0].set_title("Distance Vs Time")

   axis[0, 1].plot(distance1, v_new1)
   axis[0, 1].plot(distance2, v_new2)
   axis[0, 1].set_xlabel('Distance', fontsize=6)
   axis[0, 1].set_ylabel('Velocity', fontsize=6)
   axis[0, 1].set_title("Distance Vs Velocity")

   axis[1, 0].plot(time, v_new1)
   axis[1, 0].plot(time, v_new2)
   axis[1, 0].set_xlabel('Time', fontsize=6)
   axis[1, 0].set_ylabel('Velocity', fontsize=6)
   axis[1, 0].set_title("Velocity Vs Time")
   figure.delaxes(axis[1][1])

   plt.tight_layout()
   figure.legend(["Object 1", "Object 2"], loc=1)
        
   inp = int(input("Enter 1 to export figure, 2 to exit"))
   if inp == 1:
        plt.savefig('plot.png', dpi=300)
   plt.show()     
 except :
   print("==>Inappropriate input :: Format {'int','int','int','int'}")
