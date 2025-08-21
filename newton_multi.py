import numpy as np
from scipy.differentiate import hessian
from scipy.optimize import rosen, rosen_hess

def optimize(x0, func, stop = 1e-4): 
    grad = np.gradient(func)(x0)
    hess = hessian(func, x0)

    xt = x0 - grad / hess
    x = x0

    while abs(xt - x) > stop: 
        x = xt
        xt = x0 - np.gradient(func)(x) / hessian(func, x)

    return xt

