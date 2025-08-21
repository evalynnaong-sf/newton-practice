#Newton's method as a Python function
# test respond to issuesimport newton
#import numpy as np

def optimize(x0, func, stop = 1e-4): 
    """Implementation of Newton's method for optimization

    Initiate xt and x. Loop until reach stopping point
    """
    xt = x0 - (deriv(func, x0) / deriv2(func, x0))
    x = x0

    while abs(xt-x) > stop: 
        x = xt
        xt = x - (deriv(func, x) / deriv2(func, x))
        
    return xt


def deriv(func, x, h=1e-6): #h as in epsilon; small steps
    """Derivative helper to run Newton's method optimization function

        Parameters
        -----------
        func: callable
        x: variable
        h: 
    """
    return (func(x+h)-func(x-h)/(2*h))

def deriv2(func, x, h = 1e-6): 
    return (deriv(func,x+h,h) - deriv(func,x,h)) / h

def func(x):
    """function to test newton method"""
    return x**2 + 2*x + 1
    
if __name__ == "__main__":
    """main method"""
    x0= 5.0
    stop = 1e-6
    res = optimize(x0,func,stop)
    print(res)
    