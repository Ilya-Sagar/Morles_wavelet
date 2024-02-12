import numpy as np
import matplotlib.pyplot as plt

# x = np.linspace(0, 6*np.pi, 1000)
# signal = np.sin(2*x) + 0.5*np.sin(30*x)
x1 = np.linspace(0, 2*np.pi, 333)
x2 = np.linspace(2*np.pi, 4*np.pi, 333)
x3 = np.linspace(4*np.pi, 6*np.pi, 334)
y1 = np.sin(3*x1)
y2 = np.sin(15*x2)
y3 = np.sin(23*x3)
x = np.concatenate((x1, x2, x3))
signal = np.concatenate((y1, y2, y3))

# morlet wavelet
def psi(t, w=1):
    A = 1
    return A*np.cos(w*t)*np.exp(-t**2/2)



z = np.empty((50, 1000))

for w in range(1, 51):
    tmpz = np.empty((1000))
    for i, t in enumerate(np.linspace(0, 6*np.pi, 1000)):
        tmpz[i] = np.sum(signal*psi(x-t, w))
    z[w-1] = tmpz





fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots(4, 1)

ax1.pcolor(x, np.arange(1, 51), z)
ax1.annotate('Частотно-временной график', xy=(2, 45))
ax2[0].plot(x, signal)
ax2[0].annotate('Исход. сигнал', xy=(0, 0.5))
ax2[1].plot(x, psi(x-9, 3))
ax2[1].annotate('Вейвлет Морле при w=3', xy=(0, 0.5))
ax2[2].plot(x, psi(x-9, 20))
ax2[2].annotate('Вейвлет Морле при w=20', xy=(0, 0.5))
ax2[3].plot(x, psi(x-9, 37))
ax2[3].annotate('Вейвлет Морле при w=37', xy=(0, 0.5))


plt.show()
