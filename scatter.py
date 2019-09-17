#!/usr/bin/python3

import matplotlib.pyplot as plt

x_axis1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_axis1 = [5, 16, 34, 56, 32, 56, 32, 12, 76, 89]

x_axis2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 50]
y_axis2 = [53, 6, 46, 36, 15, 64, 73, 25, 82, 9] 

plt.title("Prices over 10 years")

plt.scatter(x_axis1, y_axis1, color='darkblue', marker='x', label="item 1")
plt.scatter(x_axis2, y_axis2, color='darkred', marker='x', label="item 2")

plt.xlabel("Time (years)")
plt.ylabel("Price (dollars)")

plt.grid(True)
plt.legend()

plt.show()


import numpy as np
import matplotlib.pyplot as plt2
from matplotlib import style

# t = np.arange(0.0, 3.0, 0.01)
# s = np.sin(2.5 * np.pi * t)
# plt2.plot(t, s)
style.use('ggplot')

t,s = np.loadtxt('data.txt', unpack=True, delimiter = ',')
plt2.plot(t, s)
 
plt2.xlabel('time (s)')
plt2.ylabel('voltage (mV)')

plt2.title('Sine Wave')
plt2.grid(True)

plt2.show()
# plt2.savefig('wave.png')

from matplotlib import pyplot as plt3
from matplotlib import style

style.use('ggplot')

x = [0, 1, 2, 3, 4, 5]
y = [46, 38, 29, 22, 13, 11]

fig, ax = plt3.subplots()

ax.bar(x, y, align='center')

ax.set_title('Olympic Gold medals in London')
ax.set_ylabel('Gold medals')
ax.set_xlabel('Countries')

ax.set_xticks(x)
ax.set_xticklabels(("USA", "China", "UK", "Russia", 
    "South Korea", "Germany"))

plt3.show()

import matplotlib.pyplot as plt4
 
labels = ['Oranges', 'Pears', 'Plums', 'Blueberries']
quantity = [38, 45, 24, 10]

colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

plt4.pie(quantity, labels=labels, colors=colors, autopct='%1.2f%%', 
    shadow=True, explode=(0.05, 0.05, 0.05, 0.05), startangle=90)

plt4.axis('equal')

plt4.show()