# 2d_wave_multiple.py
# たくさんの 2次元の波を描くコード

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

A = 1
T_ARRAY = np.array([1, 2, 3])
LAMBDA_ARRAY = np.array([1, 2, 3])
FPS = 20

fig, ax = plt.subplots(nrows=len(T_ARRAY), ncols=len(LAMBDA_ARRAY), layout='constrained')
# t = np.linspace(0, T, T * 50)
x = np.linspace(-1, 5, 100)
# ax.set(xlim=[-2, 10], ylim=[-1.2, 1.2], xlabel='x', ylabel='y')
# plt.setp(ax, xlim=[-2, 10], ylim=[-1.2, 1.2], xlabel='x', ylabel='y')

# frame には 0 からの整数値が入る (0, 1, 2, ..., frames)
def update(frame):
    t = frame / FPS
    # fig.suptitle(f't = {t:.2f}', ha='left')
    fig.suptitle(f't = {t:.2f}', fontsize=16)


    for T_INDEX, T in enumerate(T_ARRAY):
        for LAMBDA_INDEX, LAMBDA in enumerate(LAMBDA_ARRAY):
            ax[T_INDEX][LAMBDA_INDEX].cla()
            ax[T_INDEX][LAMBDA_INDEX].set(xlim=[-1, 5], ylim=[-1.2, 1.2], xlabel='x', ylabel='y')
            ax[T_INDEX][LAMBDA_INDEX].set_aspect('equal')
            ax[T_INDEX][LAMBDA_INDEX].grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)
            ax[T_INDEX][LAMBDA_INDEX].tick_params(direction='in')
            ax[T_INDEX][LAMBDA_INDEX].axhline(y=0, color='black', linewidth=0.5)
            ax[T_INDEX][LAMBDA_INDEX].axvline(x=0, color='black', linewidth=0.5)
            ax[T_INDEX][LAMBDA_INDEX].title.set_text(f'T = {T}, λ = {LAMBDA}')

            y =  A * np.sin(2 * np.pi * (t / T - x / LAMBDA))
            y0 = A * np.sin(2 * np.pi * t / T)

            wave = ax[T_INDEX][LAMBDA_INDEX].plot(x, y)
            dot, = ax[T_INDEX][LAMBDA_INDEX].plot(0, y0, color='red', marker='o', markersize=5)



if __name__ == '__main__':

    ani = FuncAnimation(
        fig = fig,
        func = update,
        frames = np.lcm.reduce(T_ARRAY) * FPS,
        interval = 1000 / FPS
    )
    ani.save('2d_wave_multiple.gif', writer='pillow')

