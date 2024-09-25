#---¡THIS-PROGRAM-CALCULATE-AND-PLOT-THE-COSINE-TAYLOR-SERIE!

#---¡IMPORT-LIBRARIES!
import numpy as np
import matplotlib.pyplot as plt

#---¡IMPORT-LOCALS! 
import factorial as FACTORIAL

#---¡WE-DEFINE-COSINE-FUNCTION!
def Cosine(x,n):
    cosx = 0
    for i in range(n+1):
        cosx += ( ( (-1)**i ) / FACTORIAL.Factorial(2*i) )*x**(2*i)
    
    #---¡PLOT-THE-FUNCTION!    
    plt.figure(figsize=(8,6))
    plt.plot(x, cosx, '-', color = 'b', label = 'cos(x)')
    plt.legend()
    plt.xlabel('$x$')
    plt.ylabel('cos($x$)')
    plt.grid()
    plt.savefig('img/cosx.png')
    plt.show()

#---¡WE-DEFINE-x-IN-[0,10]-INTERVAL!
x = np.linspace(0, 10, 100)

#---¡WE-CALL-THE-FUNCTION-WITH-n=23-ITERATIONS!
Cosine(x, 23)
