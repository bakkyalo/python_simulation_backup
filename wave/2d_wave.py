# 2d_wave.py
# 2次元の波を描くコード

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

A = 1
T = 3
LAMBDA = 2
FPS = 20

fig, ax = plt.subplots()
# t = np.linspace(0, T, T * 50)
x = np.linspace(-1, 5, 100)
# y = np.sin(2 * np.pi * (t / T + x / LAMBDA))

# wave = ax.plot(x, y)
ax.set(xlim=[-2, 10], ylim=[-1.2, 1.2], xlabel='x', ylabel='y')

# frame には 0 からの整数値が入る (0, 1, 2, ..., frames)
def update(frame):
    t = frame / FPS

    ax.cla()
    ax.set(xlim=[-1, 5], ylim=[-1.2, 1.2], xlabel='x', ylabel='y')
    ax.set_aspect('equal')
    ax.grid(True, which='both', color='gray', linestyle='--', linewidth=0.5)
    ax.tick_params(direction='in')
    ax.axhline(y=0, color='black', linewidth=0.5)
    ax.axvline(x=0, color='black', linewidth=0.5)

    ax.title.set_text(f'T = {T}, λ = {LAMBDA}')
    # fig.suptitle(f't = {t:.2f}', ha='left')
    fig.suptitle(f't = {t:.2f}', fontsize=16)

    y =  A * np.sin(2 * np.pi * (t / T - x / LAMBDA))
    y0 = A * np.sin(2 * np.pi * t / T)

    wave, = ax.plot(x, y)
    dot, = ax.plot(0, y0, color='red', marker='o', markersize=10)



if __name__ == '__main__':

    ani = FuncAnimation(
        fig = fig,
        func = update,
        frames = T * FPS,
        interval = 1000 / FPS
    )
    ani.save('2d_wave.gif', writer='pillow')

