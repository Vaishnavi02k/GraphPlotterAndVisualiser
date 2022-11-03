"""
Team name - BAKA
Project Name - Graph plotter and Equation visualizer
Members - Khushi Chaudhary 2006319
          Atharva Bhanage 2004207
          Vaishnavi 2003328          
"""
#import libraries 
import BAKA_Convert_Classical_to_Relative
import BAKA_equationVisualizer
import BAKA_OneDimension
import BAKA_RelativeVelocity
import BAKA_shm

print("Welcome to Baka plotter. Please enter the number corresponding to your desired tool.")  #Welcome and instructions 
print(" 1. Equation Visualizer \n 2. Graph of realtive velocity and acceleration of 2 objects \n 3. Graph of 1-D waveform \n 4. Graph and Calculator for Simple Harmonic iMotion \n 5.convert the classical variables to relativistic variable ")

inp,s =0,""                              
while inp ==0:                                                                      #input user's choice
  try:
   inp = int(input())
   try:
    if(inp == 1):                                                                   #if else if ladder
      BAKA_equationVisualizer.EquationVisualizer()                                       #Calling General polynomial function
    elif(inp == 2):
      v1 = int(input("Enter Velocity of first object"))                             #Taking input from user
      v2 = int(input("Enter Velocity of second object"))                    
      a1 = int(input("Enter Accelerate of first object"))
      a2 = int(input("Enter Accelerate of first object"))
      BAKA_RelativeVelocity.RelativeVelocity(v1,v2,a1,a2)                                  #Function call
    elif(inp == 3):
      n = int(input("Enter the value of n"))                                          #Taking input from user
      l = int(input("Enter the value of l"))                          
      BAKA_OneDimension.one_D(n,l)                                                                     #Function call
    elif(inp == 4):
      w = int(input("Enter the value of angular velocity w"))
      A = int(input("Enter the Amplitude"))
      phi = int(input("Enter the phase difference phi"))
      BAKA_shm.shm(w,A,phi)                                                                        #function call
    elif(inp == 5):
      v1= int(input("Enter the velocity of the frame"))                #Taking input from user
      t = int(input("Enter the time"))
      v = int(input("Enter the velocity"))
      x = int(input("Enter the x coordinate"))
      BAKA_Convert_Classical_to_Relative.Convert_Classical_to_Relative(t,v,x,v1)                                        #Function call
    else:                                                                           
      print("INVALID INPUT \n To try again enter 0 to exit enter 6")              #Error message 
      inp = int(input())
   except:
      print("==>Inppropriate input!")  
  except:                                                                            #Error message 
    print("==>Inppropriate input!")

print("Thank you for using baka plotter. Please visit us again")           #Thank you message