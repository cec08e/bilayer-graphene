import numpy as np
import matplotlib.pyplot as plt

def plot_radial_prob(ax = None):
    ''' Plots the radial probability distibution of the
        ground state of the hydrogen atom.
        :param ax: Optional Axes object to which the plot should be added. If not supplied, defaults to plotting on global plt object.
        :type ax: Axes instance.
    '''
    a_0 = 1.0
    r = np.linspace(0, 8, 100000)
    P = (1/a_0)*(4*(np.power(r,2)))*np.exp(-2*r)
    if not ax:
        plt.plot(r, P, 'k')
    else:
        ax.plot(r, P, 'k')

#def plot_radial_prob_flip(r_0 = 1, ax = None):
    ''' Plots the flipped radial probability distibution of the
        ground state of the hydrogen atom, centered at r_0.
        :param r_0: represents the effective bohr radius of the radial wavefunction. Defaults to 1.
        :type r_0: Float.
        :param ax: Optional Axes object to which the plot should be added. If not supplied, defaults to plotting on global plt object.
        :type ax: Axes instance.

        TODO: Work out mirror image plot. 
    '''
#    a_0 = 1.0
#    r = np.linspace(2, 6, 100000)
#    P = (1/a_0)*(4*(np.power(r-r_0,2)))*np.exp(-2*(r-r_0))
#    if not ax:
#        plt.plot(r, P, 'k')
#    else:
#        ax.plot(r, P, 'k')

if __name__ == "__main__":
    # Plotting hydrogen ground state radial
    # distribution with bohr radius = 1.
    #plot_radial_prob()
    #plt.ylabel("$P(r)$", fontsize = 16)
    #plt.xlabel("$r$", fontsize = 16)
    #plt.text(5, .4, "$a_{0} = 1$", fontsize = 18)
    #plt.show()
