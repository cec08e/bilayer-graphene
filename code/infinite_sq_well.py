import numpy as np
import matplotlib.pyplot as plt

def plot_isw_state(L = 1, n = 1, ax = None):
    ''' Plots the states of the infinite square well. Optional
        parameters can be passed to control width and excitation
        level.
        :param L: width of the infinite square well, from x = 0 to x = L. Must be positive, defaults to 1.
        :type L: integer.
        :param n: excitation level. Must be positive, defaults to 1.
        :type n: integer.
        :param ax: Optional Axes object to which the plot should be added. If not supplied, defaults to plotting on global plt object.
        :type ax: Axes instance.
    '''
    # Linear space of 0 to L in .00001 increments
    x = np.arange(0, L, .00001)
    psi = np.sqrt(2.0/L)*np.sin(np.pi*x/L)
    if not ax:
        plt.plot(x, psi, 'k')
    else:
        ax.plot(x, psi, 'k')

if __name__ == "__main__":
    # Plotting ISW ground state with L = 1
    # on x = [-.5, 1.5] and y = [0, 2]
    # TO DO: Add shading to infinite potential locations
    plot_isw_state()
    plt.axis([-.5, 1.5, 0, 2])
    plt.show()
