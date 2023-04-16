import numpy as np
import matplotlib.pyplot as plt


x = np.array([5, 7, 8, 9, 10, 12, 14, 16, 17])

off1 = np.array([-32.71, -74.03, -18.99, -18.17, -21.24, -62.85, -15.49, -15.2, -20.41])
on1 = np.array([0, 0.22, 14.06, 13.93, 12.73, 13.72, 13.89, 14.15, 13.54])
off2 = np.array([-32.86, -74.35, -18.52, -17.84, -21.16, -62.25, -15.47, -15.19, -20.40])
on2= np.array([0.07, 0.05, 14.22, 13.72, 13.24, 13.65, 13.74, 14.10, 13.45])



# plt.plot(x, p1, x, p2, x, p3)
# plt.plot(x, z1, x, z2, x, z3)
plt.plot(x, on1, "bx")
plt.plot(x, on2, "bx")

plt.plot(x, off1, "rv")
plt.plot(x, off2, "rv")

plt.xticks(x)

plt.xlabel("Numer Materiału")
plt.ylabel("mm")


plt.show()
