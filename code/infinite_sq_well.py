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

def plot_isw_prob(L = 1, n = 1, ax = None):
    ''' Plots the probability distribution of the infinite square well. Optional
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
        plt.plot(x, np.power(psi, 2), 'k')
    else:
        ax.plot(x, np.power(psi, 2), 'k')

if __name__ == "__main__":
    # Plotting ISW ground state with L = 1
    # on x = [-.5, 1.5] and y = [0, 2]
    # with shaded regions of potential
    # plot_isw_state()
    # plt.ylabel("$\psi(x)$", fontsize = 15)
    # plt.xlabel("$x$", fontsize = 15)
    # plt.axis([-.5, 1.5, 0, 2])
    # plt.fill([-.5, 0, 0, -.5], [0, 0, 2, 2], 'b', [1.0, 1.5, 1.5, 1.0], [0, 0, 2, 2], 'b', alpha=0.2)
    # plt.text(.6, 1.7, "$L = 1$", fontsize = 14)

    # Plotting ISW ground state with L = 2
    # on x = [-.5, 2.5] and y = [0, 2]
    # with shaded regions of potential
    #plot_isw_state(L = 2)
    #plt.ylabel("$\psi(x)$", fontsize = 15)
    #plt.xlabel("$x$", fontsize = 15)
    #plt.axis([-.5, 2.5, 0, 2])
    #plt.fill([-.5, 0, 0, -.5], [0, 0, 2, 2], 'b', [2.0, 2.5, 2.5, 2.0], [0, 0, 2, 2], 'b', alpha=0.2)
    #plt.text(.6, 1.7, "$L = 2$", fontsize = 14)

    # Single spin arrows, centered on psi
    # plt.arrow(.5, 1.4-.05, 0, .18) # Spin up arrow
    # plt.arrow(.5, 1.4+.13, 0, -.18) # Spin down arrow

    # Double spin arrows
    #plt.arrow(1-.03, 1.0-.05, 0, .18) # Spin up arrow
    #plt.arrow(1+.03, 1.0+.13, 0, -.18) # Spin down arrow

    # Plotting ISW probability distribution with L = 1
    # on x = [-.5, 1.5] and y = [0, 2.5]
    # with shaded regions of potential
    plot_isw_prob()
    plt.ylabel("$P(x)$", fontsize = 18)
    plt.xlabel("$x$", fontsize = 18)
    plt.axis([-.5, 1.5, 0, 2.5])
    plt.fill([-.5, 0, 0, -.5], [0, 0, 2.5, 2.5], 'b', [1.0, 1.5, 1.5, 1.0], [0, 0, 2.5, 2.5], 'b', alpha=0.2)
    plt.text(.75, 1.7, "$L = 1$", fontsize = 18)

    plt.show()
