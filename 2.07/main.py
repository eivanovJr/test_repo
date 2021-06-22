import math
import matplotlib.pyplot as plt

g = 9.81
gamma = 1.4
x0 = 30


m = 15 * 0.001
V = 8 * 0.001
D = 1.6 * 0.01

P0 = 105000


S = math.pi * D * D / 4
omega = math.sqrt(gamma * ((P0 + m * g / S) * S * S) / (m * V))
T = 2 * math.pi / omega
beta = T / (2 * m) / 100


times = []
height = []
height.append(x0)
times.append(0)
time = 0.0
while time < 20:
    x = x0 * math.exp(-beta * time) * math.cos(omega * time + math.pi)
    height.append(x)
    times.append(time)
    time = time + 0.001
figure = plt.figure()
plt.plot(times, height)
plt.grid(True)
plt.title("График движения груза")
plt.ylabel("положение в трубке, (см)")
plt.xlabel("Время, (с)")
plt.show()