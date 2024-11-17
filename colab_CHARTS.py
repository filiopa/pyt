# Google colab CHARTS!!!
# CHECK THE FOLLOWING LINK FOR EASIER USE! --> https://colab.research.google.com/notebooks/charts.ipynb#scrollTo=08RTGn_xE3MP

import matplotlib.pyplot as plt
 

# Line plots!
x  = [1, 2, 3, 4, 5, 6, 7, 8, 9]
y1 = [0, 2, 5, 3, 8, 3, 5, 3, 1]
y2 = [2, 4, 6, 4, 2, 4, 6, 4, 2]
plt.plot(x, y1, label="Blue line")
plt.plot(x, y2, label="Orange line")
plt.plot()

plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Line Graph Example")
plt.legend()
plt.show()


# Bar plots!
# Colors: https://matplotlib.org/api/colors_api.html
x1 = [1, 3, 4, 5, 6, 7, 9]
y1 = [4, 7, 2, 4, 7, 8, 3]

x2 = [2, 4, 6, 8, 10]
y2 = [5, 6, 2, 6, 2]

plt.bar(x1, y1, label="Blue Bar", color='b')
plt.bar(x2, y2, label="Green Bar", color='g')
plt.plot()

plt.xlabel("bar number")
plt.ylabel("bar height")
plt.title("Bar Chart Example")
plt.legend()
plt.show()


# Scatter plots!
# Markers: https://matplotlib.org/api/markers_api.html
x1 = [2, 3, 4]
y1 = [5.2, 5.6, 5]

x2 = [1, 2, 3, 4, 5]
y2 = [2, 3, 2, 4.5, 4]
y3 = [6.2, 8, 7, 8, 7]

plt.scatter(x1, y1)
plt.scatter(x2, y2, marker='+', color='r')
plt.scatter(x2, y3, marker='^', color='m')
plt.xlabel("x number")
plt.ylabel("y height")
plt.title('Scatter Plot Example ;)')
plt.show()


# Stack plots!
idxes = [ 1,  2,  3,  4,  5,  6,  7,  8,  9]
arr1  = [23, 40, 28, 43,  8, 44, 43, 18, 17]
arr2  = [17, 30, 22, 14, 17, 17, 29, 22, 30]
arr3  = [15, 31, 18, 22, 18, 19, 13, 32, 39]
# Adding legend for stack plots is tricky.
plt.plot([], [], color='r', label = 'D 1')
plt.plot([], [], color='g', label = 'D 2')
plt.plot([], [], color='b', label = 'D 3')

plt.stackplot(idxes, arr1, arr2, arr3, colors= ['r', 'g', 'b'])
plt.title('Stack Plot Example')
plt.legend()
plt.show()


# Pie charts!
labels = 'cyan', 'green', 'red', 'yellow'
sections = [56, 66, 24, 11]
colors = ['c', 'g', 'r', 'y']

plt.pie(sections, labels=labels, colors=colors,
        startangle=90,
        explode = (0.0, 0.1, 0.05, 0.05),
        autopct = '%1.2f%%')

plt.axis('equal') # Try commenting this out.
plt.title('Pie Chart Example')
plt.show()


# fill_between and alpha!
#Subplotting using Subplot2grid!
# Histograms!

# 3D STUFF!!!
# 3D Scatter Plots!
import numpy as np
from mpl_toolkits.mplot3d import axes3d

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y1 = np.random.randint(10, size=10)
z1 = np.random.randint(10, size=10)

x2 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
y2 = np.random.randint(-10, 0, size=10)
z2 = np.random.randint(10, size=10)

ax.scatter(x1, y1, z1, c='c', marker='o', label='cyan')
ax.scatter(x2, y2, z2, c='orange', marker='D', label='orange')

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
plt.title("3D Scatter Plot Example")
plt.legend()
plt.tight_layout()
plt.show()


# 3D Bar Plots!
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [1, 2, 0, 3, 0+1, 6.6, 7, 8, 9, 10]
z = np.zeros(10)

dx = np.ones(10)
dy = np.ones(10)
dz = [1, 2, 0, 4, 5, 6, 7, 8, 9, 10]

ax.bar3d(x, y, z, dx, dy, dz, color='g')

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z axis')
plt.title("3D Bar Chart Example")
plt.tight_layout()
plt.show()


# Wireframe plots!
# Heatmaps!
# Altair!
# And many more!!!