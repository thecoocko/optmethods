#методами половинного деления, золотого сечения, Фибоначчи
import math
import time


EPS = 0.0001
 
def f(x):
    return math.pow(x,3)/3+2*(math.exp(-x)-math.pow(x,2)+2*x)

def halfDivisionMethod(a,b):
    start_time = time.time()
    while (b-a) >= 2*EPS:
        x = (a + b) / 2
        y1, y2 = x - EPS/2, x + EPS/2
        f1, f2  = f(y1), f(y2)
        a, b = (y1,b) if f1 > f2 else (a,y2)
    return "--- %s seconds ---" % (time.time() - start_time)+ f"\nbisection method: {f((a + b) / 2)}"

def fibonacciNumbers(n):
    #recursive
    # n = 0 if n == 0 else n
    # n = 'Incorrect input' if n < 0 else n
    # return 1 if n==2 or n==1 else fibonacciNumbers(n-1)+fibonacciNumbers(n-2)
    
    fibonacciSeries = [0,1]
    if n > 2:
        for i in range(2, n):
            nextElement = fibonacciSeries[i-1] + fibonacciSeries[i-2]
            fibonacciSeries.append(nextElement)

    return fibonacciSeries

def fibonacciMethod(a,b,h = 0.1):
    start_time = time.time()
    n = int((b-a)/h)
    fib = fibonacciNumbers(n)
    while n !=1 :
        x1,x2 = a + (b-a)*fib[n-3]/fib[n-1], a + (b-a)*fib[n-2]/fib[n-1]
        y1, y2 = f(x1), f(x2)
        n = n - 1
        if y1 < y2:
            b = x2
            x2 = x1
            x1 = a + (b - x2)
        else:
            a = x1
            x1 = x2
            x2 = b - (x1 - a)
    return "--- %s seconds ---" % (time.time() - start_time)+ f"\nfibonacci method: {min(f(x1),f(x2))}" 


def goldenSectionMethod(a,b):
    start_time = time.time()
    while (b-a)>EPS:
        y1 = b - 0.618*(b - a)
        y2 = a + 0.618*(b - a)
        if f(y1) <= f(y2):
            b = y2
            y2 = y1
            y1 = b - 0.618*(b - a)
        else:
            a = y1
            y1 = y2
            y2  = a + 0.618*(b - a)

    return "--- %s seconds ---" % (time.time() - start_time)+ f"\ngolden section method: {f((y1 + y2)/2.0)}"


if __name__=='__main__':
    a = int(input("a: "))
    b =int(input("b: "))
    print(halfDivisionMethod(a,b))
    print(fibonacciMethod(a,b))
    print(goldenSectionMethod(a,b))
    