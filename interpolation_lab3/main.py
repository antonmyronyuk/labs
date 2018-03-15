import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from interpolation import Interpolation as Itp

if __name__ == "__main__":
    itp = Itp(function=lambda x: np.cos(x)**2)
    print(itp.args)
    t1 = np.arange(-3.0, 3.1, 0.01)
    t2 = np.arange(0.0, 1.01, 0.01)
    plt.figure(figsize=(15, 7))
    plt.subplot(211)
    #plt.plot(itp.args, itp.func(itp.args), 'go', t1, itp.func(t1), 'r', t1, itp.newton(t1), 'b')
    #plt.plot(itp.args, itp.func(itp.args), 'go', t1, itp.func(t1), 'r', t1, itp.lagrange(t1), 'b')
    # function graph
    plt.plot(itp.args, itp.func(itp.args), 'go', t1, itp.func(t1), 'r', t1, itp.eitken(t1), 'b')
    plt.subplot(212)
    # absolute error
    plt.plot(t2, np.abs(itp.func(t2) - itp.eitken(t2)), 'b')
    plt.show()
