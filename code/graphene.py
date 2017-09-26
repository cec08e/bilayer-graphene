import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def plot_monolayer_disp(ax = None):
    """ Plots the dispersion relation E/t for monolayer
        graphene. By default
        the atomic 2pz energy is taken to be 0.
        :param ax: Optional Axes object to which the plot should be added. If not supplied, defaults to plotting on global plt object.
        :type ax: Axes instance.
    """
    fig = plt.figure()
    ax = fig.gca( projection='3d')
    kxa = np.linspace(-2*np.pi, 2*np.pi, 1000)
    kya = np.linspace(-2*np.pi, 2*np.pi, 1000)
    Kx, Ky = np.meshgrid(kxa,kya)
    E_plus = np.sqrt(1 + 4*np.cos(Ky*(np.sqrt(3)/2.0))*np.cos(Kx/2.0) + 4*np.power(np.cos(Kx/2.0), 2))
    E_minus = -1*E_plus
    ax.plot_surface(Kx, Ky, E_plus, cmap = cm.gnuplot2, alpha = .5)
    ax.plot_surface(Kx, Ky, E_minus, cmap = cm.gnuplot2_r, alpha = .5)
    ax.set_xlabel('$k_{x}a$', fontsize = 22)
    ax.set_ylabel('$k_{y}a$', fontsize = 22)
    ax.set_zlabel('$E/t$', fontsize = 22)
    
if __name__ == "__main__":
    plot_monolayer_disp()
    plt.show()
