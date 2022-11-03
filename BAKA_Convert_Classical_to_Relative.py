import numpy as np
import matplotlib.pyplot as plt 
import math

#This is a ptogram use to convert the classical variables to relativistic variable
def Convert_Classical_to_Relative(t=0,v=0,x=0,v1=0):
 try:
  c=3*(10)**8
  #setting up a condition for the base case where  the velocity has to be less than C
  if(v>=c):
   print("The entered velocity can't be greater than speed of light that is '3*10^8' ")
  else:
   beta=1/math.sqrt(1-(v1/c)**2)                             #function for beta constant
   t1=t*beta                                                 #obtaining relative time, velocity and displacement 
   v2=v*beta
   x1=x*beta
       
   inp = int(input("To export relative values of time, displacement and velocity press 1 to exit press 2."))
   if inp == 1:
    file1 = open("Data.txt", "w")
    L = ["TIME-"+str(t)+"->"+str(t1)+"\n","DISTANCE"+str(x)+"->"+str(x1)+"\n","VELOCITY"+str(v)+"->"+str(v2)]
    file1.writelines(L)
    
   
   print("The time in Relative domain changes to ",t1)
   print("The distance in Relative domain changes to ",x1)
   print("The velocity in Relative domain changes to ",v2)
 
 except :
  print("==>Please give appropriate input :: Format {'int','int','int','int'}")