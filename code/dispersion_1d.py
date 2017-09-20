import numpy as np
import matplotlib.pyplot as plt

def plot_1d_mono_disp(ax = None):
    """ Plots the dispersion relation E/t for the one-dimensional
        monoatomic chain with interatomic distance a. By default,
        the ground state energy and cross term shift are 0.
        :param ax: Optional Axes object to which the plot should be added. If not supplied, defaults to plotting on global plt object.
        :type ax: Axes instance.
    """
    ka = np.linspace(-np.pi, np.pi, 1000000)
    E_over_t = -2*np.cos(ka)   # Dispersion relation in units of t
    if not ax:
        plt.plot(ka, E_over_t, 'k')
    else:
        ax.plot(ka, E_over_t, 'ka')

if __name__ == "__main__":
    # Plotting dispersion relation for 1d monoatomic chain
    # with interatomic distance a.
    plot_1d_mono_disp()
    plt.axis([-np.pi, np.pi, -2.5, 2.5])
    plt.ylabel("$E/t$", fontsize = 18)
    plt.xlabel("$ka$", fontsize = 18)
    plt.show()
