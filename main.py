import csv

import numpy as numpy
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression



h = 4.135667 * 10**(-15)
e = 1.6 * 10**(-19)
c = 3 * 10**8

def theoretical_A(metal_name):
    switcher = {
        "Gold": 5.285,
        "Calcium": 2.87,
        "Nickel": 5.195
    }
    result = switcher.get(metal_name, "Invalid name")
    return result

file = open("Nickel.csv", encoding='utf-8')
filereader = csv.reader(file, delimiter=";")
row_count = sum(1 for row in filereader) - 1
count = 0
frequency = numpy.zeros(row_count)
voltage = numpy.zeros(row_count)
file.seek(0)
metal_name = ""
for row in filereader:
    if count == 0:
        count = count + 1
        continue
    metal_name = row[1]
    voltage[count - 1] = row[2]
    frequency[count - 1] = c / (float(row[5]) * 10**(-9))
    count = count + 1
A = (h * frequency[count - 2]- voltage[count - 2])
A_theoretical = theoretical_A(metal_name)

print("Рассматриваемый металл : ", metal_name, "\n")
print("Экспериментальное значение работы выхода : ", round(A, 4), " эВ")
print("Теоретическое значение работы выхода : ", round(A_theoretical, 4), " эВ\n")
print("Относительная погрешность работы выхода : ", round(abs(1 - (A / A_theoretical)), 4))
print("Абсолютная погрешность работы выхода : ", round(abs(A - A_theoretical), 4), " эВ\n")

figure = plt.figure()
plt.plot(frequency, voltage)
plt.grid(True)
plt.title("Uз(v) для " + metal_name)
plt.ylabel("Uз, (В)")
plt.xlabel("v ,(Гц)")
frequency = frequency.reshape(-1, 1)
model = LinearRegression().fit(frequency, voltage)
y_pred = model.predict(frequency)
plt.plot(frequency, y_pred, 'r--')
h_exp = (y_pred[count - 2] - y_pred[0]) / (frequency[count - 2] - frequency[0])
print("Экспериментальное значение постоянной Планка: ", round(h_exp[0], 20), " эВ")
print("Теоретическое значение постоянной Планка : ", h, " эВ\n")
print("Относительная погрешность постоянной Планка : ", round(abs(1 - (h_exp[0] / h)), 4))
print("Абсолютная погрешность постоянной Планка : ", round(abs(h - h_exp[0]), 20), " эВ")
plt.show()
