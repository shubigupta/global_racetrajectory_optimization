import csv
import numpy as np

from numpy import genfromtxt


if __name__=="__main__":
    
    csv_file_path        =       "../outputs/traj_race_cl.csv"


    '''
    # s_m; x_m; y_m; psi_rad; kappa_radpm; vx_mps; ax_mps2

    s_m: float32, meter. Curvi-linear distance along the raceline.
    x_m: float32, meter. X-coordinate of raceline point.
    y_m: float32, meter. Y-coordinate of raceline point.
    psi_rad: float32, rad. Heading of raceline in current point from -pi to +pi rad. Zero is north (along y-axis).
    kappa_radpm: float32, rad/meter. Curvature of raceline in current point.
    vx_mps: float32, meter/second. Target velocity in current point.
    ax_mps2: float32, meter/second². Target acceleration in current point. We assume this acceleration to be constant from current point until next point.
    '''
    my_data = genfromtxt(csv_file_path, delimiter=';')
    

    # x_m; y_m; vx_mps; psi_rad; kappa_radpm
    my_array        =       np.vstack((my_data[:,1], my_data[:,2], my_data[:,5], my_data[:,3], my_data[:,4])).T

    np.save("../../trajectory.npy", my_array)