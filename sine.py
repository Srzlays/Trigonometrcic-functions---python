#---¡THIS-PROGRAM-CALCULATE-AND-PLOT-THE-SINE-TAYLOR-SERIE!

#---¡IMPORT-LIBRARIES!
import numpy as np
import matplotlib.pyplot as plt

#---¡IMPORT-LOCALS! 
import factorial as FACTORIAL

#---¡WE-DEFINE-SINE-FUNCTION!
def Sine(x, n):
    sinx = 0
    for i in range(n+1):
        sinx += ( ((-1)**i) / FACTORIAL.Factorial(2*i +1) ) * x**(2*i +1)
    #---¡PLOT-FUNCTION!
    plt.figure(figsize = (8, 6))
    plt.plot(x, sinx, '-', color = 'b', label = 'sin($x$)')
    plt.legend()
    plt.xlabel('$x$')
    plt.ylabel('sin($x$)')
    plt.grid()
    plt.savefig('img/sinx.png')
    plt.show()

#---¡WE-DEFINE-x-IN-[0,10]-INTERVAL!
x = np.linspace(0, 10, 100)

#---¡WE-CALL-SINE-FUNCTION-WITH-N=25-ITERATIONS!
Sine(x, 25)
