import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def f(x, a):
    return (x**(2/3) + np.e/3 * ((np.pi - x**2)**(1/2)) * np.sin(a * np.pi * x))*4

def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1,line2

def update(frame):
    a = frame * 1 
    y = f(x, a)
    line1.set_data(-x, y)
    line2.set_data(x, y)
    return line1,line2

x = np.linspace(0, np.pi, 1000)

fig, ax = plt.subplots()
ax.set_xlim(-3, 3)
ax.set_ylim(-10, 10)
line1, = ax.plot([], [], color='r')
line2, = ax.plot([], [], color='r')
plt.xticks([], [])
plt.yticks([], [])

plt.title('This is for you!❤')

ani = FuncAnimation(fig, update, frames=range(40), init_func=init, blit=True)

ani.save('heart.mp4', fps=10, extra_args=['-vcodec', 'libx264'])

plt.show()
