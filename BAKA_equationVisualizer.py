import numpy as np
import matplotlib.pyplot as plt 


#Function to visualize the graph a given equation
def EquationVisualizer():
  try: 
   print("Enter constants of polynomial array")
   l = list(map(int, input().split()))

   print("Enter coefficient of sin,cos,tan terms.")
   temp_2,temp_3,temp_4=list(map(int, input().split()))

   print("Enter coefficient of exponential")
   temp_5 = int(input())

   print("Enter the constant term if present else enter 0.")
   temp_6 = int(input())

   f = int(input("Enter the x bound of the graph"))
   x = np.linspace(start = 0, stop= f, endpoint = True) 
   y,temp_1 = 0*x, x 
   for i in range(0,len(l)):                                 #Generates expression with entered polynomials
     y= y + l[i]*temp_1
     temp_1=x*temp_1

   y = y+temp_2*np.sin(x)                                   #adds the sin term to expression
   y = y+temp_3*np.cos(x)                                   #adds the cos term
   y = y+temp_4*np.tan(x)                                   #adds the tan term
   y = y+temp_5*np.exp(x)                                   #adds the exponential
   y = y+temp_6                                             #adds the constant term 
   plt.plot(x, y, '-g', label=r"Equation's graph")

   plt.xlabel('x')
   plt.ylabel('y')
   plt.title('Polynomial Curve')
   plt.legend(loc='upper left')
        
   inp = int(input("Enter 1 to export figure, 2 to exit"))
   if inp == 1:
        plt.savefig('plot.png', dpi=100)
     
   plt.show()
  except:
    print("==>Inappropriate Input! :: input format{'int array','int','int','int','int','int','int'}")