# 3d_plane_wave_multiple.py
# たくさんの 3次元平面波を描くコード

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

A = 1
OMEGA_ARRAY = np.array( [1, 1, 1] )
OMEGA = 1
K1_ARRAY = np.array( [1, 2, 3] )
K2_ARRAY = np.array( [1, 2, 3] )

FPS = 10
PERIOD = 2 * np.pi / OMEGA
NUM_FRAMES = int(PERIOD * FPS)

fig, ax = plt.subplots(nrows=len(K1_ARRAY), ncols=len(K2_ARRAY), figsize=(12, 9), layout='constrained', subplot_kw={'projection': '3d'})

# t = np.linspace(0, T, T * 50)
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
# ax.set(xlim=[-2, 10], ylim=[-1.2, 1.2], xlabel='x', ylabel='y')
# plt.setp(ax, xlim=[-2, 10], ylim=[-1.2, 1.2], xlabel='x', ylabel='y')

# frame には 0 からの整数値が入る (0, 1, 2, ..., frames)
def update(frame):
    t = frame / FPS
    print(f'Now frame  {frame} / {NUM_FRAMES}')
    fig.suptitle(rf'$t = {t:.2f}$', fontsize=16)


    for K1_INDEX, K1 in enumerate(K1_ARRAY):
        for K2_INDEX, K2 in enumerate(K2_ARRAY):


            ax[K1_INDEX][K2_INDEX].cla()
            ax[K1_INDEX][K2_INDEX].set(xlim=[-5, 5], ylim=[-5, 5], zlim=[-3, 3], xlabel=r'$x_1$', ylabel=r'$x_2$', zlabel=r'$u$')
            ax[K1_INDEX][K2_INDEX].set_aspect('equal')
            ax[K1_INDEX][K2_INDEX].grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)
            ax[K1_INDEX][K2_INDEX].tick_params(direction='in')
            ax[K1_INDEX][K2_INDEX].title.set_text(rf'$(k_1, k_2) = ({K1}, {K2})$')

            u =  A * np.cos(OMEGA * t - K1 * X - K2 * Y)

            wave = ax[K1_INDEX][K2_INDEX].plot_surface(
                X, Y, u,
                cmap = 'viridis'
            )



if __name__ == '__main__':

    ani = FuncAnimation(
        fig = fig,
        func = update,
        frames = NUM_FRAMES,
        interval = 1000 / FPS
    )
    ani.save('3d_plane_wave_multiple.gif', writer='pillow')

