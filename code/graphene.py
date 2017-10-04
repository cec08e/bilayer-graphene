import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import sympy as sp

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

def calc_a(kxa):
    # when ky = 0, a = a*
    return 1 + np.exp((0+1j)*kxa/2.0) + np.exp((0-1j)*kxa/2.0)

def bilayer_determinant():
    g_0, g_d, g_1 = sp.symbols("g_0 g_d g_1")
    E, EA1, EA2, EB1, EB2 = sp.symbols("E EA1 EA2 EB1 EB2")
    b_d, b_nd, b_nn = sp.symbols("b_d b_nd b_nn")
    #ES = sp.Matrix([[E, E*a*g_0, 0, 0],
    #              [E*a_s*g_0, E, E*g_d, 0],
    #              [0, E*g_d, E, E*a*g_0],
    #              [0, 0, E*a_s*g_0, E]])
    ES_simple = sp.Matrix([[E, 0, 0, 0],
                 [0, E, 0, 0],
                 [0, 0, E, 0],
                 [0, 0, 0, E]])
    ka_space = np.linspace(-3*np.pi/2.0, 3*np.pi/2.0, 30)

    E_vals_list = []
    for kxa in ka_space:
        #a, a_s = sp.symbols("a a_s")
        a = calc_a(kxa)
        a_s = calc_a(kxa)


        #H = sp.Matrix([[EA1, -a*g_1, a*b_nd, -a_s*b_nn],
        #               [-a_s*g_1, EB1, b_d,a*b_nd],
        #               [a_s*b_nd, b_d , EA2, -a*g_1],
        #               [-a*b_nn, a_s*b_nd, -a_s*g_1, EB2]])
        #M = H - ES
        H_simple = sp.Matrix([[0, -a*(3.16), a*(.14), -a_s*(.38)],
                       [-a_s*(3.16), 0, .381 ,a*(.14)],
                       [a_s*(.14), .381 , 0, -a*(3.16)],
                       [-a*(.38), a_s*(.14), -a_s*(3.16), 0]])
        M = H_simple - ES_simple
        M_d = M.det()
        #print "M: ", M
        #print "Determinant: ", M_d
        #print "******"
        #print "Factored determinant: ", sp.factor(M_d)
        #print "Simplified determinant: " , sp.simplify(M_d)
        # Make a space of ka values

        sols = sp.solve(M_d,E)
        print sols
        E_vals_list.append(sols)


        #print sp.solve((E**7 - 29.9956*E**5*a*a_s - 0.145161*E**5 - 0.07584*E**4*a**3 + 0.5779008*E**4*a*a_s - 0.07584*E**4*a_s**3 + 0.381*E**3*a**3 + 299.23668544*E**3*a**2*a_s**2 + 1.4509712916*E**3*a*a_s + 0.381*E**3*a_s**3 + 0.757307904*E**2*a**4*a_s - 5.77068622848*E**2*a**2*a_s**2 + 0.757307904*E**2*a*a_s**4 - 3.8045136*E*a**4*a_s - 992.816576856064*E*a**3*a_s**3 - 0.014495196816*E*a**2*a_s**2 - 3.8045136*E*a*a_s**4), E)
    print "Before: ", E_vals_list
    #E_vals_list = np.array(E_vals_list)
    #print "After: ", E_vals_list
    plt.plot(ka_space, [E_vals_list[i][0] for i in range(len(E_vals_list))])
    #plt.plot([kxa]*len(E_vals_list), [E_vals_list[i][1] for i in range(len(E_vals_list))])
    #plt.plot([kxa]*len(E_vals_list), [E_vals_list[i][2] for i in range(len(E_vals_list))])
    #plt.plot([kxa]*len(E_vals_list), [E_vals_list[i][3] for i in range(len(E_vals_list))])
    plt.show()

if __name__ == "__main__":
    #plot_monolayer_disp()
    #plt.show()
    bilayer_determinant()
